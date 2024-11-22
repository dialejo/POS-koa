<template>
    <div class="register-container">
      <!-- Barra de navegación -->
      <nav class="navbar">
        <ul class="nav-list">
          <li><router-link to="/inicio" exact>Inicio</router-link></li>
          <li><router-link to="/servicios">Servicios</router-link></li>
          <li><router-link to="/" exact>Login</router-link></li>
          <li><router-link to="/register" exact>Registro</router-link></li>
        </ul>
      </nav>
  
      <!-- Formulario de registro -->
      <div class="register-box">
        <h1 class="register-title">Crear Cuenta</h1>
        <form @submit.prevent="submitRegister" class="register-form">
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
            <label for="name">Nombre: </label>
            <input 
              type="text" 
              v-model="name" 
              id="name" 
              placeholder="Ingresa tu nombre" 
              required 
              class="form-input" 
            />
          </div>
          <div class="form-group">
            <label for="email">Correo Electrónico: </label>
            <input 
              type="email" 
              v-model="email" 
              id="email" 
              placeholder="Ingresa tu correo" 
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
              placeholder="Crea una contraseña" 
              required 
              class="form-input" 
            />
          </div>
          <div class="form-group">
            <label for="confirm-password">Confirmar Contraseña: </label>
            <input 
              type="password" 
              v-model="confirmPassword" 
              id="confirm-password" 
              placeholder="Confirma tu contraseña" 
              required 
              class="form-input" 
            />
          </div>
          <button type="submit" class="register-button">Registrar</button>
        </form>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
        <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RegisterPage',
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        errorMessage: '',
        successMessage: '',
      };
    },
    methods: {
      async submitRegister() {
        // Validación de contraseñas
        if (this.password !== this.confirmPassword) {
          this.errorMessage = "Las contraseñas no coinciden.";
          this.successMessage = '';
          return;
        }
  
        // Limpiar mensajes previos
        this.errorMessage = '';
        this.successMessage = '';
  
        // Llamada a la API
        try {
          const response = await fetch('http://localhost:8000/api/usuarios/register/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              username: this.username,
              email: this.email,
              password: this.password,
              name: this.name,
            }),
          });
  
          if (!response.ok) {
            const errorData = await response.json();
            this.errorMessage = errorData.message || 'Error al registrar.';
          } else {
            this.successMessage = 'Registro exitoso. Ahora puedes iniciar sesión.';
            this.username = '';
            this.email = '';
            this.password = '';
            this.confirmPassword = '';
            // Redirigir al login después de un registro exitoso
          setTimeout(() => {
            this.$router.push('/'); // Redirige al login
            }, 2000); // 2 segundos de espera
          }
        } catch (error) {
          this.errorMessage = 'Error de conexión. Inténtalo nuevamente.';
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .register-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 20px;
  }
  
  .register-box {
    flex: 1;
    background-image: url('/src/assets/backgroundKOA.jpg');
    background-size: cover;
    background-position: center;
    padding: 3rem;
    border-radius: 2vh;
    box-shadow: 0 20px 10px rgba(0, 0, 0, 0.1);
    max-width: 300px;
    text-align: center;
  }
  
  .register-title {
    font-size: 2rem;
    font-weight: bold;
    color: white;
    margin-bottom: 1rem;
  }
  
  .register-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 1rem;
  }
  
  .form-group label {
    color: white;
  }
  
  .form-input {
    padding: 1rem;
    border-radius: 10px;
    width: 100%;
    font-size: 1rem;
  }
  
  .register-button {
    background: #7e8341;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.8rem;
    font-size: 1.1rem;
    cursor: pointer;
  }
  
  .error-message {
    margin-top: 1rem;
    color: red;
  }
  
  .success-message {
    margin-top: 1rem;
    color: green;
  }
  </style>
  