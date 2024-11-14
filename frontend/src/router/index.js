import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/Login.vue';
import Dashboard from '../components/HelloWorld.vue';  // Asume que tienes una página de dashboard

const routes = [
  { path: '/', component: Login },
  { path: '/dashboard', component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;