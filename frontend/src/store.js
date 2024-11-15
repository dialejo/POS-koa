// src/store.js
import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    accessToken: localStorage.getItem('access_token') || '',
  },
  mutations: {
    setAccessToken(state, token) {
      state.accessToken = token;
      localStorage.setItem('access_token', token);
    },
    clearAccessToken(state) {
      state.accessToken = '';
      localStorage.removeItem('access_token');
    },
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await axios.post('http://localhost:8000/api/token/', credentials);
        commit('setAccessToken', response.data.access);
        return response.data;
      } catch (error) {
        throw new Error('Invalid credentials');
      }
    },
    logout({ commit }) {
      commit('clearAccessToken');
    },
  },
  getters: {
    isAuthenticated: state => !!state.accessToken,
  },
});
