<template>
  <div id="app">
    <!-- Aquí se montarán las rutas -->
    <router-view></router-view> <!-- Esto es el contenedor donde se renderizarán los componentes de las rutas -->
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
