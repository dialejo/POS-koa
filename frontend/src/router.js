import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from './components/Login.vue';
import DashboardPage from './components/Dashboard.vue';
import UserList from './components/User/UserList.vue';  // Ruta para listar usuarios
import UserForm from './components/User/UserForm.vue';
import RegisterPage from './components/Register.vue'; 

// Aquí no redirigimos aún. Haremos la lógica en los componentes directamente.
const routes = [
  { path: '/', component: LoginPage, name:'login' },
  { path: '/dashboard', component: DashboardPage, name:'dashboard' },
  { path: '/users', component: UserList, name: 'user-list' },
  { path: '/users/create', component: UserForm, name: 'user-create' },
  { path: '/users/edit/:id', component: UserForm, name: 'user-edit' },
  { path: '/register', component: RegisterPage, name: 'register' },
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
