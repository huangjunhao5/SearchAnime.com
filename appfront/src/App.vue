<template>
    <!--  <img src="./assets/logo.png">-->
    <div>
        <router-view></router-view>
        <p>
            If Element Plus is successfully added to this project, you'll see an
            <code v-text="'<el-button>'"></code>
            below
        </p>
        <el-button type="primary" @click="loginPage()">el-button</el-button>
    </div>
    <!--  <HelloWorld msg="Welcome to Your Vue.js App"/>-->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import router from "./router/index.js";

export default {
    name: 'App',
    components: {
        // HelloWorld,
    },
    data() {
        return {}
    },
    methods: {
        loginPage() {
            router.push('/login')
        }
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
