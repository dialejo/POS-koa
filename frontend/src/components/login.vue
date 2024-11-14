<template>
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
</template>

<script>
import axios from 'axios';

export default {
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
        localStorage.setItem('access_token', response.data.access);
        this.$router.push('/dashboard');  // Redirige al dashboard
      } catch (error) {
        this.errorMessage = 'Invalid credentials';
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