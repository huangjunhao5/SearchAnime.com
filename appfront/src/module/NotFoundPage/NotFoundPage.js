import { createApp } from 'vue'
import App from '@/module/NotFoundPage/NotFoundPage.vue'
import installElementPlus from '../../plugins/element'
import store from "@/store";
// import router from "@/router";
import router from '@/router';

import axios from 'axios';
import VueAxios from 'vue-axios'

import VForm3 from 'vform3-builds'  //引入VForm3库
import 'bootstrap'
import $ from 'jquery'
import '/src/assets/style.scss'
import '@popperjs/core'
import "bootstrap/dist/css/bootstrap.css"
import 'vform3-builds/dist/designer.style.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import 'bootstrap/dist/js/bootstrap'



axios.defaults.baseURL='http://api.studyserver.icu';

const app = createApp(App)

installElementPlus(app)
app.use(VueAxios,axios)

app.config.globalProperties.$axios = axios

app.use(VForm3)

app.use(router)

app.use($)

app.use(store).mount('#app')