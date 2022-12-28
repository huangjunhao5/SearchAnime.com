<template>
    <div id="sss">
        <el-row>
            <el-col>
                <div class='space' style="height: 2em;" />
            </el-col>
        </el-row>
        <el-row>
            <el-col>
                <ListAnime v-bind:title="'排行榜(按B站评分排序)'" v-bind:url="'/Anime/api/GetAllAnime'" />
            </el-col>
        </el-row>
    </div>
</template>

<script>
import { defineComponent } from 'vue'
import ListAnime from "@/module/MainPage/ListAnime/ListAnime.vue";

export default defineComponent({
    name: "RankPage",
    components: {
        ListAnime,
    },
    data() {
        return {
            //
        }
    },
    created() {
        document.title = "排行榜";
    },
    methods: {
        //
    },
})
</script>

<style scoped>
.img img {
    height: 100%;
    width: 100%;
}
</style>