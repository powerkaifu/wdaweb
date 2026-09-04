import { createRouter, createWebHashHistory, type RouteRecordRaw } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: { title: '課程特色' }
  },
  {
    path: '/curriculum',
    redirect: '/'
  },
  {
    path: '/showcase',
    name: 'showcase',
    component: () => import('@/views/ShowcaseView.vue'),
    meta: { title: '學員專題成果' }
  },
  {
    path: '/admission',
    name: 'admission',
    component: () => import('@/views/AdmissionView.vue'),
    meta: { title: '招生時程與報名' }
  },
  {
    path: '/faq',
    name: 'faq',
    component: () => import('@/views/FaqView.vue'),
    meta: { title: '常見問題 FAQ' }
  },
  {
    path: '/community',
    name: 'community',
    component: () => import('@/views/CommunityView.vue'),
    meta: { title: 'Discord 線上諮詢' }
  },
  {
    path: '/kaifu-lab',
    name: 'kaifu-lab',
    component: () => import('@/views/GlowLabView.vue'),
    meta: { title: 'Kaifu 視覺與動效實驗室' }
  },
  {
    path: '/glow-lab',
    redirect: '/kaifu-lab'
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
  scrollBehavior(_to, _from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    }
    return { top: 0, behavior: 'smooth' }
  }
})

export default router
