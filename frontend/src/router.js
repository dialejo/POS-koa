import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from './components/Login.vue';
import DashboardPage from './components/Dashboard.vue';

// Aquí no redirigimos aún. Haremos la lógica en los componentes directamente.
const routes = [
  { path: '/', component: LoginPage },
  { path: '/dashboard', component: DashboardPage },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Verificar si el usuario tiene token antes de cargar las rutas
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token');
  
  if (to.path === '/' && token) {
    // Si hay token y el usuario intenta acceder al login, redirigir al dashboard
    next('/dashboard');
  } else if (to.path === '/dashboard' && !token) {
    // Si no hay token y el usuario intenta acceder al dashboard, redirigir al login
    next('/');
  } else {
    // De lo contrario, continuar con la navegación
    next();
  }
});

export default router;
