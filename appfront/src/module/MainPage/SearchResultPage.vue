<template>
    <!-- <div id="sss"> -->
    <el-row>
        <el-col>
            <div class='space' style="height: 6em;" />
        </el-col>
    </el-row>
    <el-row>
        <el-col>
            <list-anime v-bind:url="'Anime/api/SearchAnime/' + keyword" v-bind:title="keyword + ' - 搜索结果'"></list-anime>
        </el-col>
    </el-row>
    <!-- </div> -->
</template>

<script>
import ListAnime from "@/module/MainPage/ListAnime/ListAnime.vue";
export default {
    name: "SearchResultPage",
    components: {
        ListAnime,
    },
    data() {
        return {
            //
            keyword: '',
        }
    },
    created() {
        //
        this.$data.keyword = this.$route.query.keyword;
        // alert(this.$data.keyword);
        document.title = this.$data.keyword + ' - 搜索结果';
    },
    methods: {
        //
    }
}
</script>

<style scoped>

</style>