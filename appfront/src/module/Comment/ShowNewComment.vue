<template>
    <div>
        <el-row>
            <el-col :span="24">
                <h2>精选评论</h2>
            </el-col>
        </el-row>
        <div class="space" style="height: 3em;"></div><!--占位-->
        <!-- 无评论是显示当前用户没有评论 -->
        <div v-for="cmt in AllComment" :key="cmt" style="margin: auto 2em;">
            <div>
                <el-row>
                    <el-col>
                        <div>
                            <el-row :gutter="20" style="width: 100%;">
                                <el-col :span="1" style='min-width: 3em;'>
                                    <i class="bi bi-person-circle" style="font-size: 2em;"></i>
                                </el-col>
                                <el-col :span="1"
                                        :style="'min-width: ' + (cmt.fields.CommentUserName.length + cmt.fields.AnimeTitle.length + 8) + 'em;'">
                                    <el-row>
                                        <el-col>
                                            <div class="space" style="height: .5em;"/>
                                        </el-col>
                                    </el-row>
                                    <el-row style="width: 60em;">
                                        <el-col :span="1"
                                                :style="'min-width: ' + (cmt.fields.CommentUserName.length / 2 + 1) + 'em;'">
                                            <div>{{ cmt.fields.CommentUserName }}</div>
                                        </el-col>
                                        <el-col :span="1" style="min-width: 15em">
                                            <div>
                                                于 {{ cmt.fields.Created }}
                                            </div>
                                        </el-col>
                                        <el-col :span="1"
                                                :style="'min-width: ' + (cmt.fields.AnimeTitle.length + 6) + 'em;'">
                                            <div class="CommentBody">
                                                评论了 <a
                                                :href="'/MainPage/#/AnimePage?media_id=' + cmt.fields.mediaId">{{cmt.fields.AnimeTitle}}</a>
                                                ：
                                            </div>
                                        </el-col>
                                    </el-row>
                                </el-col>
                            </el-row>
                        </div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col>
                        <div class='space' style="height: 0.5em;"></div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="1" style="min-width: 2em">
                        <div class='space' style="height: 1em;"></div>
                    </el-col>
                    <el-col :span="20">
                        <div class="CommentBody">
                            {{ cmt.fields.CommentBody }}
                        </div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col>
                        <div class='space'></div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="1" style="min-width: 3em;">
                        <div>评分：</div>
                    </el-col>
                    <el-col :span="18">
                        <div>
                            <el-rate disabled v-model="cmt.fields.Rating" show-score></el-rate>
                        </div>
                    </el-col>
                </el-row>
                <!--          <el-row>-->
                <!--            <el-col>-->
                <!--              评论时间 ：{{cmt.fields.Created}}-->
                <!--            </el-col>-->
                <!--          </el-row>-->
                <el-row>
                    <el-col>
                        <div class='space'></div>
                    </el-col>
                </el-row>
            </div>
        </div>
    </div>
</template>

<script>
// import {GetMediaId} from "@/module/Comment/CommentFunctionLib";
import {ElMessage} from "element-plus";

export default {
    name: "ShowNewComment",
    data() {
        return {
            mediaId: '',
            AllComment: [],
        }
    },
    created() {
        // 获取media_id
        // this.$data.mediaId = GetMediaId();
        // alert(this.$data.mediaId);
        this.axios.get('/Comment/api/GetNewComment').then((res) => {
            if (res.data.code === 'ok') {
                this.$data.AllComment = res.data.data;
            } else {
                ElMessage.error('没有评论');
            }
        })
    }
}
</script>

<style scoped>
.space {
    height: 1em;
    width: 1em;
}
</style>