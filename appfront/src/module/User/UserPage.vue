<template>
    <div class="Nav" style="height: 100%">

        <el-container class="Main" style="height:100%">
            <el-aside style="height: 100%;overflow:hidden" class="Nav">
                <el-row gutter="0" class="tac" style="height: 100%">
                    <el-col :span="16" type="flex" style="height: 100vh">
                        <el-menu router
                                 :uniqueOpened="true"
                                 :default-active="default_active"
                                 class="el-menu-vertical-demo"
                                 @open="handleOpen"
                                 @close="handleClose"
                                 background-color="#545c64"
                                 text-color="#fff"
                                 active-text-color="#ffd04b"
                                 style="height: 100%"
                        >
                            <!--        <h5>自定义颜色</h5>-->
                            <!--        这里放网站logo-->
                            <!--              <h2 @click="alert('11')" class="logo">SAW</h2>-->
                            <el-sub-menu index="1111" style="height: 100%">
                                <el-menu-item-group>
                                    <el-menu-item index="1" :route="{path: '/UserInfo', query: {uid: this.$route.query.uid}}">
                                        <i class="el-icon-s-home"></i>
                                        <template #title>主页</template>
                                    </el-menu-item>
                                    <el-menu-item index="2" :route="{path: '/UserSetting', query: {uid: this.$route.query.uid}}">
                                        <i class="el-icon-s-custom"></i>
                                        <template #title>个人信息</template>
                                    </el-menu-item>
                                    <el-menu-item index="3" :route="{path: '/UserUpdate', query: {uid: this.$route.query.uid}}">
                                        <i class="el-icon-date"></i>
                                        <template #title>用户评论</template>
                                    </el-menu-item>
                                </el-menu-item-group>
                            </el-sub-menu>
                        </el-menu>
                    </el-col>
                </el-row>
            </el-aside>
        </el-container>
    </div>
    <div style="margin: 5% 300px; " class="route">
        <router-view></router-view>
    </div>
</template>

<script>
// import UserInfo from "@/module/User/UserInfo";
import router from "./router/UserRouter.js";
// import {GetUid} from "@/module/User/UserFunctionLib";
import {onMounted, ref, computed, getCurrentInstance, watchEffect} from 'vue'
import {useRoute} from "vue-router";

export default {
    name: 'App',
    components: {
        // UserInfo,
    },
    data() {
        return {
            // user_id: '',
            default_active: 0,
        };
    },
    created() {
        // this.$data.user_id = this.$router.query.uid;
        // console.log(this.$route.query);
        watchEffect(() => {
            router.getRoutes().map((item, index) => {
                if (item.path === router.currentRoute.value.path) {
                    if (index == 0) index++;
                    this.$data.default_active = index;
                    // console.log(router.currentRoute.value.path)
                    // console.log(index);
                }
            })
        });
    },
    mounted() {
        // this.$data.user_id = this.$router.query.uid;
        // console.log(this.$route.query);
    },
    methods: {
        // handleOpen(key, keyPath) {
        //     console.log(key, keyPath)
        // },
        // handleClose(key, keyPath) {
        //     console.log(key, keyPath)
        // },
    },
}
</script>

<style>
/*el-col el-menu{*/
/*  height: 800px;*/
/*}*/
.Nav {
    height: 100%;
    position: fixed;
    width: 250px;
    top: 0;
    left: 0;
}

.Nav el-col el-menu el-menu-item {
    top: 0;
    left: 0;
}

</style>