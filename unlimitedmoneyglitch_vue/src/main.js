import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import axios from 'axios'

axios.defaults.baseURL = 'https://api.unlimitedmoneyglitch.com'
//axios.defaults.baseURL = ''http://127.0.0.1:8000' 'https://api.unlimitedmoneyglitch.com'
loadFonts()

createApp(App)
  .use(router, axios)
  .use(store)
  .use(vuetify)
  .mount('#app')
