<template>
    <div class="user-form-container">
      <h2 class="form-title">{{ isEditMode ? 'Editar Usuario' : 'Crear Usuario' }}</h2>
      
      <!-- Formulario para crear o editar un usuario -->
      <form @submit.prevent="submitForm" class="user-form">
        <div class="form-group">
          <label for="username">Nombre de usuario:</label>
          <input 
            type="text" 
            id="username" 
            v-model="user.username" 
            placeholder="Ingresa el nombre de usuario" 
            required 
          />
        </div>
        <div class="form-group">
          <label for="email">Correo Electrónico:</label>
          <input 
            type="email" 
            id="email" 
            v-model="user.email" 
            placeholder="Ingresa el correo electrónico" 
            required 
          />
        </div>
        <div class="form-group">
          <label for="password">Contraseña:</label>
          <input 
            type="password" 
            id="password" 
            v-model="user.password" 
            placeholder="Ingresa la contraseña" 
            :required="!isEditMode" 
          />
        </div>
        <button type="submit" class="submit-button">{{ isEditMode ? 'Actualizar' : 'Crear' }}</button>
      </form>
      
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success-message">{{ successMessage }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        user: {
          username: '',
          email: '',
          password: '',
        },
        errorMessage: '',
        successMessage: '',
        isEditMode: false,  // True si estamos editando un usuario existente
      };
    },
    props: {
      // Propiedades opcionales si estás usando este componente para edición
      userToEdit: { 
        type: Object, 
        default: () => null 
      },
    },
    watch: {
      userToEdit(newUser) {
        if (newUser) {
          this.isEditMode = true;
          this.user = { ...newUser };  // Rellenar con los datos del usuario a editar
        }
      },
    },
    methods: {
      async submitForm() {
        if (this.isEditMode) {
          // Llamada para actualizar usuario
          this.updateUser();
        } else {
          // Llamada para crear usuario
          this.createUser();
        }
      },
      
      async createUser() {
        try {
          const response = await fetch('http://tu-api/usuarios/register/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.user),
          });
          
          if (response.ok) {
            this.successMessage = 'Usuario creado exitosamente';
            this.errorMessage = '';
            this.user = { username: '', email: '', password: '' };  // Limpiar campos
          } else {
            const errorData = await response.json();
            this.errorMessage = errorData.message || 'Error al crear el usuario.';
          }
        } catch (error) {
          this.errorMessage = 'Error de conexión. Inténtalo nuevamente.';
        }
      },
  
      async updateUser() {
        try {
          const response = await fetch(`http://tu-api/usuarios/${this.user.id}/`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(this.user),
          });
  
          if (response.ok) {
            this.successMessage = 'Usuario actualizado exitosamente';
            this.errorMessage = '';
          } else {
            const errorData = await response.json();
            this.errorMessage = errorData.message || 'Error al actualizar el usuario.';
          }
        } catch (error) {
          this.errorMessage = 'Error de conexión. Inténtalo nuevamente.';
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Aquí se pueden agregar estilos CSS para el formulario */
  .user-form-container {
    max-width: 500px;
    margin: auto;
  }
  
  .user-form {
    display: flex;
    flex-direction: column;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .submit-button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px;
    cursor: pointer;
  }
  
  .error-message {
    color: red;
  }
  
  .success-message {
    color: green;
  }
  </style>
  