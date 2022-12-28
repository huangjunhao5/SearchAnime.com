<template>
    <div class="sss">
        <el-row>
            <el-col>
                <div class = 'space' style="height: 2em;"/>
            </el-col>
        </el-row>
        <div class='row justify-content-md-center'>
            <el-row id="MainCSS" class="col-md-auto">
                <!-- <el-col :span="4">
                    <div class="space"></div>
                </el-col> -->
                <el-col :offset="1">
                    <div class="space" style="height:3em;"></div>
                    <ShowNewComment></ShowNewComment>
                    <div class="space"/>
                </el-col>
                <!-- <el-col :span="2">
                    <div class="space"></div>
                </el-col> -->
            </el-row>
        </div>
        <div class="space" style="height: 3em;"/>
    </div>
</template>

<script>
import ShowNewComment from "@/module/Comment/ShowNewComment.vue";

export default {
    name: "NewCommentPage",
    components: {
        ShowNewComment,
    },
    data() {
        return {
            //
        }
    },
    created() {
        //
        document.title = "精选评论";
    },
}
</script>

<style scoped>

.space {
    height: 1em;
    width: 1em;
}
#MainCSS{
    background-color: white; 
    border-radius: 8px 8px 8px 8px;
}
</style>