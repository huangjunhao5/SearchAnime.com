import { createApp } from 'vue'
import App from './Comment/Test'
import installElementPlus from '../plugins/element'
import store from "@/store";
// import router from "@/router";
import axios from 'axios'
import VueAxios from 'vue-axios'

import VForm3 from 'vform3-builds'  //引入VForm3库


import 'vform3-builds/dist/designer.style.css'  //引入VForm3样式


axios.defaults.baseURL='http://localhost'

const app = createApp(App)

installElementPlus(app)
app.use(VueAxios,axios)

app.config.globalProperties.$axios = axios

app.use(VForm3)

app.use(store).mount('#app')