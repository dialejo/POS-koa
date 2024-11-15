<!-- src/components/Dashboard.vue -->
<template>
  <div class="dashboard">
    <h1>Welcome to the Dashboard</h1>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
export default {
  name: 'DashboardPage',
  methods: {
    logout() {
      // Elimina el token del almacenamiento local
      localStorage.removeItem('access_token');
      // Redirige al login
      this.$router.push('/');
    },
  },
};
</script>

<style scoped>
button {
  background-color: #ff4d4d;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
}

button:hover {
  background-color: #ff3333;
}
</style>