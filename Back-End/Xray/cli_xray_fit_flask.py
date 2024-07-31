# -*- encoding: utf-8 -*-

import os
import sys
import torch
import argparse
from transformers import AutoTokenizer
from sat.model.mixins import CachedAutoregressiveMixin

from model import VisualGLMModel, chat
from finetune_XrayGLM import FineTuneVisualGLMModel
from sat.model import AutoModel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_length", type=int, default=2048, help='max length of the total sequence')
    parser.add_argument("--top_p", type=float, default=0.4, help='top p for nucleus sampling')
    parser.add_argument("--top_k", type=int, default=100, help='top k for top k sampling')
    parser.add_argument("--temperature", type=float, default=.8, help='temperature for sampling')
    parser.add_argument("--english", action='store_true', help='only output English')
    parser.add_argument("--quant", choices=[8, 4], type=int, default=None, help='quantization bits')
    parser.add_argument("--from_pretrained", type=str, default="visualglm-6b", help='pretrained ckpt')
    parser.add_argument("--prompt_zh", type=str, default="描述这张图片。", help='Chinese prompt for the first round')
    parser.add_argument("--prompt_en", type=str, default="Describe the image.", help='English prompt for the first round')
    parser.add_argument("--image_path", type=str, required=True, help='Path to the image file')
    args = parser.parse_args()

    # load model
    model, model_args = AutoModel.from_pretrained(
        args.from_pretrained,
        args=argparse.Namespace(
            fp16=True,
            skip_init=True,
            use_gpu_initialization=True if (torch.cuda.is_available() and args.quant is None) else False,
            device='cuda' if (torch.cuda.is_available() and args.quant is None) else 'cpu',
        ),
        url='local'
    )
    model = model.eval()

    if args.quant:
        import deepspeed
        model = deepspeed.init_inference(model, mp_size=1, dtype=torch.half, replace_method='auto')

    model.add_mixin('auto-regressive', CachedAutoregressiveMixin())

    tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
    
    with torch.no_grad():
        history = None
        cache_image = None
        image_path = args.image_path
        if len(image_path) > 0:
            query = args.prompt_en if args.english else args.prompt_zh
        else:
            if not args.english:
                query = input("用户：")
            else:
                query = input("User: ")
        while True:
            if query == "clear":
                break
            if query == "stop":
                sys.exit(0)
            try:
                response, history, cache_image = chat(
                    image_path, 
                    model, 
                    tokenizer,
                    query, 
                    history=history, 
                    image=cache_image, 
                    max_length=args.max_length, 
                    top_p=args.top_p, 
                    temperature=args.temperature,
                    top_k=args.top_k,
                    english=args.english,
                    invalid_slices=[slice(63823, 130000)] if args.english else []
                )
            except Exception as e:
                print(e)
                break
            sep = 'Agent:' if args.english else '答：'
            print(response.split(sep)[-1].strip())
            return  # Exit after first response


if __name__ == "__main__":
    main()
