import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

import Layout from './components/layout.vue'
import Card from './components/card.vue'
import Upload from './components/upload.vue'
import Image from './components/image.vue'

import App from './App.vue'
import router from './router'

import i18n from './i18n'

const app = createApp(App)

app.component('Layout',Layout)
app.component('Card',Card)
app.component('IUpload', Upload)
app.component('Image', Image)


for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}

app.use(i18n)
app.use(ElementPlus)
app.use(createPinia())
app.use(router)

app.mount('#app')
