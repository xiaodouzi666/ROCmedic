import json
import os

# 定义诊断意见，根据不同的类型
diagnosis_suggestions = {
    "Myocardial Infarction detected.": [
        "Medications such as antiplatelets and thrombolytics may be required.",
        "Adopt lifestyle changes: quit smoking, limit alcohol, eat healthy, and exercise regularly.",
        "Even before reaching the hospital, emergency personnel may begin treatment of a suspected heart attack with:\n"
        "Aspirin, clopidogrel, heparin, or other anticlotting agents to prevent new clots\n"
        "Thrombolytic drugs to dissolve existing clots ('clot-busting' drugs such as tPA)\n"
        "Oxygen to protect heart tissue\n"
        "Nitroglycerin to widen coronary vessels\n"
        "Drugs to decrease the heart's workload and pain, relieve anxiety, or regulate heart rhythm"
    ],
    "This ECG is normal.": [
        "Continue regular check-ups.",
        "Maintain a healthy lifestyle.",
        "No immediate action needed."
    ],
    "Abnormal heartbeat detected.": [
        "Monitor heart rate regularly.",
        "Consult a cardiologist for further evaluation.",
        "Consider lifestyle changes to improve heart health.",
        "You may need one or more medicines to treat a slow, fast, or irregular heartbeat. Sometimes medicines are used together with other treatments. If your dose is too high, medicines to treat arrhythmias can make your arrhythmia worse. This happens more often in women than in men. Talk to your doctor if your symptoms get worse.",
        "Medicine to treat a slow heartbeat (such as atropine) may be given by emergency medical services (EMS) or in the emergency room (ER). Atropine may cause difficulty swallowing.",
        "Medicines to treat a fast heartbeat include:\n"
        "Adenosine, which can cause some chest pain, flushing, shortness of breath, and atrial fibrillation and may be given by EMS or in the ER\n"
        "Beta blockers, which can cause fatigue, stomach or sleep problems, and sexual dysfunction, and can make some conduction disorders worse\n"
        "Calcium channel blockers, which can cause digestive trouble, swollen feet, or low blood pressure\n"
        "Digoxin, which is used to treat atrial fibrillation, and can cause nausea, vomiting, and diarrhea\n"
        "Potassium channel blockers, which can cause low blood pressure, problems with your thyroid levels, lung conditions, or another type of arrhythmia\n"
        "Sodium channel blockers, which raise the risk of sudden cardiac arrest in people who have heart disease"
    ],
    "History of Myocardial Infarction detected.": [
        "Medications such as antiplatelets and thrombolytics may be required.",
        "Adopt lifestyle changes: quit smoking, limit alcohol, eat healthy, and exercise regularly.",
        "Even before reaching the hospital, emergency personnel may begin treatment of a suspected heart attack with:\n"
        "Aspirin, clopidogrel, heparin, or other anticlotting agents to prevent new clots\n"
        "Thrombolytic drugs to dissolve existing clots ('clot-busting' drugs such as tPA)\n"
        "Oxygen to protect heart tissue\n"
        "Nitroglycerin to widen coronary vessels\n"
        "Drugs to decrease the heart's workload and pain, relieve anxiety, or regulate heart rhythm"
    ],
    # 这里可以增加更多类型的诊断意见
}

# 定义文件路径
json_file_path = '/home/azuki/ECG/data/ecg_data.json'

def update_json_with_diagnosis_suggestions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    for entry in data:
        label = entry.get('label', "")
        suggestions = diagnosis_suggestions.get(label, [])
        entry['diagnosis_suggestions'] = suggestions

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"Updated JSON file with diagnosis suggestions: {file_path}")

if __name__ == "__main__":
    if os.path.exists(json_file_path):
        update_json_with_diagnosis_suggestions(json_file_path)
    else:
        print(f"JSON file not found: {json_file_path}")
