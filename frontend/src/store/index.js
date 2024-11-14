import { createStore } from 'vuex';

export default createStore({
  state: {
    accessToken: localStorage.getItem('access_token') || '',
  },
  mutations: {
    setAccessToken(state, token) {
      state.accessToken = token;
    },
  },
  actions: {
    login({ commit }, token) {
      commit('setAccessToken', token);
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },
});