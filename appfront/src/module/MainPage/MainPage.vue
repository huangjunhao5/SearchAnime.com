<template>
    <div class="MainPage">
        <MainNavigation />
        <div class="mainNaviSpace"></div>
        <div class="content">
            <router-view class="router-view" v-slot="{ Component }">
                <transition :name="transitionName">
                    <component :is="Component" />
                </transition>
            </router-view>
        </div>
    </div>
</template>

<script>
// 加密
// import { encrypt } from '@/utils/rsaEncrypt'
// import Cookies from 'js-cookie'


import MainNavigation from "@/module/MainNavigation/MainNavigation.vue";
import { ref, watch } from 'vue'
import { useRoute } from 'vue-router'


export default {
    name: 'App',
    components: {
        MainNavigation,
    },
    data() {
        return {
            // vis: 0,
        }
    },
    created() {
        //
    },
    mounted() {
        // this.$data.vis = 1;
    },
    methods: {
        //
    },
    setup() {

        const transition = ['slide-left', 'slide-right']
        let transitionName = ref(transition[0])

        const route = useRoute()

        // 监控路由的变化
        watch(
            () => route.meta.index,
            (newIndex, oldIndex) => {
                if (newIndex > oldIndex) {
                    transitionName.value = transition[0]
                } else {
                    transitionName.value = transition[1]
                }
            }
        )

        return { transitionName }
    },
}
</script>

<style lang="scss" scoped>
.mainNaviSpace {
    height: 60px;
}

// * {
//     overflow-x: hidden;
// }


.router-view {
    // width: 100%;
    // height: 100%;
    // position: absolute;
    // top: 0;
    // bottom: 0;
    // margin: 0 auto;
    // overflow-y: auto;
    overflow-x: hidden;
    // -webkit-overflow-scrolling: touch;
}

.slide-left-enter-active,
.slide-left-leave-active,
.slide-right-enter-active,
.slide-right-leave-active {
	width: 100%;
    height: 100%;
    will-change: transform;
    transition: all 300ms cubic-bezier(.55,0,.1,1);
    position: absolute;
    backface-visibility: hidden;
}
.slide-right-enter-active {
    opacity: 0;
    transform: translate3d(-100%, 0, 0);
}
.slide-right-leave-active {
    opacity: 0;
    transform: translate3d(3%, 0, 0);
}
.slide-left-enter-active{
    opacity: 0;
    transform: translate3d(100%, 0, 0);
}
.slide-left-leave-active{
    opacity: 0;
    transform: translate3d(-3%, 0, 0);
}
</style>

