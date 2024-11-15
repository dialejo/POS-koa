<template>
    <div class="login-container">  <!-- Agrega un contenedor raíz -->
      <div class="login">
        <h1>Login</h1>
        <form @submit.prevent="submitLogin">
          <div>
            <label for="username">Username</label>
            <input type="text" v-model="username" id="username" required />
          </div>
          <div>
            <label for="password">Password</label>
            <input type="password" v-model="password" id="password" required />
          </div>
          <button type="submit">Login</button>
        </form>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
      </div>
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
          this.errorMessage = 'Invalid credentials';
          console.log(error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .error {
    color: red;
  }
  </style>  