import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from './components/Login.vue';
import DashboardPage from './components/Dashboard.vue';

// Aquí no redirigimos aún. Haremos la lógica en los componentes directamente.
const routes = [
  { path: '/', component: LoginPage, name:'login' },
  { path: '/dashboard', component: DashboardPage, name:'dashboard' },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Verificar si el usuario tiene token antes de cargar las rutas
router.beforeEach((to, from, next) => {
  const accessToken = localStorage.getItem('access_token');

  if (to.path === '/dashboard' && !accessToken) {
    next('/'); // Redirige al login si no hay un token
  } else {
    next(); // Permite la navegación
  }
});

export default router;
