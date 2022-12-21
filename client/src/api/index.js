import axios from 'axios';

export function authenticate (userData) {
    return axios.post(`${process.env.VUE_APP_BASE_URL}/login/`, userData)
  }
  
export function register (userData) {
    return axios.post(`${process.env.VUE_APP_BASE_URL}/register/`, userData)
}