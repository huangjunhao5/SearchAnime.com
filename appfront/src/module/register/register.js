import { createApp } from 'vue'
import App from './register.vue'
import installElementPlus from '../../plugins/element'
import store from "@/store";
// import router from "@/router";

import axios from 'axios'
import VueAxios from 'vue-axios'

import $ from 'jquery'


// 引入bootstrap样式
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'


axios.defaults.baseURL='http://api.studyserver.icu'

const app = createApp(App)
installElementPlus(app)
app.use(VueAxios,axios)
app.use($)
app.config.globalProperties.$axios = axios
app.use(store).mount('#app')