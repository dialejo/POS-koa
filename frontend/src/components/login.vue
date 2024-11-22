<template>
  <div class="page-container">
    <!-- Barra de navegación -->
    <nav class="navbar">
      <ul class="nav-list">
        <li><router-link to="/inicio" exact>Inicio</router-link></li>
        <li><router-link to="/servicios">Servicios</router-link></li>
        <li><router-link to="/" exact>Login</router-link></li>
        <li><router-link to="/register">Registro</router-link></li>
      </ul>
    </nav>

    <!-- Contenido principal -->
    <div class="login-container">
      <div class="login-box">
        <h1 class="login-title">Iniciar Sesión</h1>
        <form @submit.prevent="submitLogin" class="login-form">
          <div class="form-group">
            <label for="username">Usuario: </label>
            <input 
              type="text" 
              v-model="username" 
              id="username" 
              placeholder="Ingresa tu usuario" 
              required 
              class="form-input" 
            />
          </div>
          <div class="form-group">
            <label for="password">Contraseña: </label>
            <input 
              type="password" 
              v-model="password" 
              id="password" 
              placeholder="Ingresa tu contraseña" 
              required 
              class="form-input" 
            />
          </div>
          <button type="submit" class="login-button">Entrar</button>
        </form>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </div>
    </div>

    <!-- Pie de página -->
    <footer class="footer">
      <p>&copy; 2024 KOA POS. Todos los derechos reservados.</p>
      <ul class="footer-links">
        <li><a href="#">Política de privacidad</a></li>
        <li><a href="#">Términos y condiciones</a></li>
        <li><a href="#">Contacto</a></li>
      </ul>
    </footer>
  </div>
</template>

  <script>
  import axios from 'axios';
  
  export default {
    name:'LoginPage',
    data() {
      return {
        username: '',
        password: '',
        errorMessage: '',
      };
    },
    methods: {
      async submitLogin() {
        try {
          const response = await axios.post('http://localhost:8000/api/token/', {
            username: this.username,
            password: this.password,
          });
          console.log('Token recibido:',response.data.access);
          localStorage.setItem('access_token', response.data.access);
          console.log('login successfull redierecting to dashboard');
          this.$router.push('/dashboard');  // Redirige al dashboard
          console.log('redirigiendo a dashboard');
        } catch (error) {
          this.errorMessage = 'credenciales no validas';
          console.log(error);
        }
      },
    },
  };
  </script>
  
<style scoped>
.navbar {
  margin-top: 10px;
  background-color: #4d4729;
  border-radius: 10px;
  padding: 10px;
  position: fixed;
  width: 90%;
  top: 0;
  z-index: 1000;
}

.nav-list {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 30px;
}

.nav-list li {
  display: inline;
}

.nav-list li a {
  color: white;
  font-family: sans-serif;
  font-weight: bold;
  text-decoration: none;
  padding: 10px 15px;
  font-size: 18px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.nav-list li a:hover {
  background-color: #c7c9a9;
}

.router-link-active {
  background-color: #c7c9a9; /* Color para la página activa */
}

.error-message {
  margin-top: 1rem;
  color: white;
  font-size: 0.9rem;
}
.login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 20px;
}
.login-box {
  flex: 1;
  background-image: url('/src/assets/backgroundKOA.jpg');
  background-size:cover;
  background-position: center;
  padding: 3rem;
  border-radius: 2vh;
  box-shadow: 0 20px 10px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 300px;
  text-align: center;
}

.login-title {
  margin-top: 0.2rem;
  font-size: 2rem;
  font-weight: bold;
  font-family: sans-serif;
  color: white;
}

.login-form {
  display: flex;
  flex-direction: column;
}
  
.form-group {
  margin-bottom: 1rem;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-size: 1.4rem;
  color: white;
}

.form-input {
  width: 90%;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 10px;
  font-size: 1rem;
  color: #333;
  outline: none;
  transition: border-color 0.3s;
}

.form-input:focus {
  border-color: #c7c9a9;
}

.login-button {
  width: 100%;
  padding: 0.8rem;
  background: #7e8341;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  margin-top: 20px;
  transition: background 0.3s;
}

.login-button:hover {
  background: #4d4729;
}

.footer {
  background-color: #4d4729;
  color: white;
  text-align: center;
  padding: 80px 30px;
}
.footer p {
  margin: 0;
  font-size: 14px;
}

.footer-links {
  list-style: none;
  display: flex;
  justify-content: center;
  gap: 15px;
  margin: 10px 0 0;
  padding: 0;
}
  
.footer-links li {
  margin: 0;
}
  
.footer-links a {
  text-decoration: none;
  color: #4CAF50;
  font-size: 14px;
}
  
.footer-links a:hover {
  color: #80e27e;
}

</style>  