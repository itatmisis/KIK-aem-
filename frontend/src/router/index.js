import { createRouter, createWebHistory } from 'vue-router'
import Recomendation from '../views/Recomendation.vue'
import Auth from '../views/Auth.vue'
import Profile from '../views/Profile.vue'
import Analytics from '../views/Analytics.vue'

const routes = [
  {
    path: '/recomendation',
    name: 'Recomendation',
    component: Recomendation
  },
  {
    path: '/',
    name: 'Analytics',
    component: Analytics
  },
  {
    path: '/authication',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
