import { createRouter, createWebHistory } from 'vue-router'
import Layout from '../layout/index.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'layout',
      component: Layout,
      children: [
        {
          path: '/',
          redirect: '/xray'
        },
        {
          path: '/xray',
          name: 'xray',
          meta: {
            title: 'X光诊断'
          },
          component: () => import('../views/xray/index.vue')
        },
        {
          path: '/pathological',
          name: 'pathological',
          meta: {
            title: '病理/生化分析诊断'
          },
          component: () => import('../views/pathological/index.vue')
        },
        {
          path: '/electrocardiograph',
          name: 'electrocardiograph',
          meta: {
            title: '心电图分析诊断'
          },
          component: () => import('../views/electrocardiograph/index.vue')
        },
        // {
        //   path: '/history',
        //   name: 'history',
        //   meta: {
        //     title: '诊断历史'
        //   },
        //   component: () => import('../views/history/index.vue')
        // }
      ]
    },
   
  ]
})

export default router
