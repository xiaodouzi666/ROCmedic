import { createI18n } from 'vue-i18n';
 
const messages = {
  en: {
    menu: {
        xray: 'X-ray Diagnosis',
        pathological: 'BreastTumor Analysis',
        electrocardiogram: 'ECG Analysis',
    },
    tab: {
        scanResult: 'Result',
        suggestion: 'Condition Advice',
        history: 'Diagnosis History',
        // diagnosis: 'Diagnosis suggestion'
    }
  },
  zh: {
    menu: {
        xray: 'X光诊断',
        pathological: '病理/生化分析诊断',
        electrocardiogram: '心电图分析诊断',
    },
    tab: {
        scanResult: '扫描结果',
        suggestion: '病情建议',
        history: '诊断历史'
    }
  }
};
 
const i18n = createI18n({
  locale: 'en', // set default locale
  fallbackLocale: 'en', // set fallback locale
  messages, // set locale messages
});
 
export default i18n;