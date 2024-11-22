<template>
    <div class="user-list-container">
      <h2>Lista de Usuarios</h2>
      
      <!-- Mostrar la lista de usuarios -->
      <table v-if="users.length">
        <thead>
          <tr>
            <th>Nombre de Usuario</th>
            <th>Correo Electrónico</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>
              <button @click="editUser(user)">Editar</button>
              <button @click="deleteUser(user.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        users: [],
        errorMessage: '',
      };
    },
    mounted() {
      this.fetchUsers();
    },
    methods: {
      async fetchUsers() {
        try {
          const response = await fetch('http://tu-api/usuarios/');
          const data = await response.json();
          if (response.ok) {
            this.users = data;  // Asumiendo que la respuesta tiene la lista de usuarios
          } else {
            this.errorMessage = 'No se pudieron cargar los usuarios';
          }
        } catch (error) {
          this.errorMessage = 'Error de conexión. Inténtalo nuevamente.';
        }
      },
  
      editUser(user) {
        this.$router.push({ name: 'edit-user', params: { userId: user.id } });
      },
  
      async deleteUser(userId) {
        const confirmDelete = confirm('¿Estás seguro de que deseas eliminar este usuario?');
        if (confirmDelete) {
          try {
            const response = await fetch(`http://tu-api/usuarios/${userId}/`, {
              method: 'DELETE',
            });
            if (response.ok) {
              this.fetchUsers();  // Volver a cargar la lista de usuarios
            } else {
              this.errorMessage = 'Error al eliminar el usuario';
            }
          } catch (error) {
            this.errorMessage = 'Error de conexión. Inténtalo nuevamente.';
          }
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Estilos CSS para la lista de usuarios */
  .user-list-container {
    max-width: 800px;
    margin: auto;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    padding: 10px;
    text-align: left;
  }
  
  button {
    margin: 0 5px;
    padding: 5px 10px;
    cursor: pointer;
  }
  
  .error-message {
    color: red;
  }
  </style>
  