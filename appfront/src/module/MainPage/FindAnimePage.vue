<template>
    <div class = 'FindAnimePage'>
        <!-- 占位 -->

    </div>
</template>

<script>

export default{
    name: 'FindAnimePage',
    data(){
        return {
            ShowElemNum: 10,
            allAnimeList: [],
            showAnimeList: [],
            
        }
    },
    created(){
        //
        document.title = "找动漫";
        this.axios.get("/Anime/api/GetAllAnime").then((res) => {
            if (res.data.code === "ok") {
                this.$data.allAnimeList = res.data.data;
            }
        });
    },
    mounted(){
        //
    },
    methods:{
        //
    }
}
</script>

<style>
.space{
    height: 1em;
    width: 1em;
}
</style>