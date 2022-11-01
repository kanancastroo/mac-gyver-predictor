import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css'
import '@mdi/font/css/materialdesignicons.css'

Vue.config.productionTip = false
Vue.use(Vuetify)

const opts = {
  theme: {
    themes: {
      light: {
        //
      },
    },
  },
  icons: {
    iconfont: 'mdi',
  },
};

export default new Vuetify(opts)

new Vue({
  router,
  vuetify: new Vuetify({}),
  store,
  render: h => h(App)
}).$mount('#app')
