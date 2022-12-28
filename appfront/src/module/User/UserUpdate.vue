<template>
    <div class="row" id="MainCSS">
        <div class="col-1"></div>
        <div class="col-8">
            <div class="space" />
            <div class='Comment'>
                <div class='Elem'>
                    <el-row>
                        <el-col :span="24">
                            <h2>用户评论</h2>
                        </el-col>
                    </el-row>
                    <div class="space"></div><!--占位-->
                    <!-- 无评论是显示当前用户没有评论 -->
                    <div v-if="comment.length == 0">
                        <h4>该用户没有评论</h4>
                    </div>
                    <div v-for="cmt in comment" :key="cmt" class='CommentElem'>
                        <el-row>
                            <el-col>
                                <el-row :gutter="20" style="width: 100%;">
                                    <el-col :span="1" style='min-width: 3em;'>
                                        <i class="bi bi-person-circle" style="font-size: 2em;"></i>
                                    </el-col>
                                    <el-col :span="1"
                                        :style="'min-width: ' + (username.length + cmt.fields.AnimeTitle.length + 8) + 'em;'">
                                        <el-row>
                                            <el-col>
                                                <div class="space" style="height: .5em;" />
                                            </el-col>
                                        </el-row>
                                        <el-row style="width: 60em;">
                                            <el-col :span="1"
                                                :style="'min-width: ' + (username.length / 2 + 1) + 'em;'">
                                                <div>{{ username }}</div>
                                            </el-col>
                                            <el-col :span="1" style="min-width: 15em">
                                                <div>
                                                    于 {{ cmt.fields.Created }}
                                                </div>
                                            </el-col>
                                            <el-col :span="1"
                                                :style="'min-width: ' + (cmt.fields.AnimeTitle.length + 6) + 'em;'">
                                                <div class="CommentBody">
                                                    评论了
                                                    <a :href="'/MainPage/#/AnimePage?media_id=' + cmt.fields.mediaId">
                                                        {{ cmt.fields.AnimeTitle }}
                                                    </a> ：
                                                </div>
                                            </el-col>
                                        </el-row>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col>
                                <div class='space' style="height: 1em;"></div>
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
                                <div class="CommentRate">
                                    <el-rate disabled v-model="cmt.fields.Rating"></el-rate>
                                </div>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col>
                                <div class='space'></div>
                            </el-col>
                        </el-row>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
// import {GetUid} from "@/module/User/UserFunctionLib";

export default {
    name: "UserUpdate",
    data() {
        return {
            uid: '',
            username: '',
            comment: [],
        }
    },
    created() {
        // alert('1');
        this.$data.uid = this.$route.query.uid;
        if (this.$data.uid == null || this.$data.uid == '') {
            window.location.href = '/NotFoundPage';
            return;
        }
        this.axios.get('Comment/api/GetCommentByUser/' + this.$data.uid).then((res) => {
            //
            if (res.data.code === 'ok') {
                this.$data.comment = res.data.data;
            }
            else {
                window.location.href = '/NotFoundPage';
                return;
            }
        });
        this.axios.get('AppUser/api/GetUserInformation/' + this.$data.uid).then((res) => {
            if (res.data.code === 'ok') {
                this.$data.username = res.data.result[0].fields.open_name;
            } else {
                window.location.href = '/NotFoundPage';
                return;
            }
        })
    }
}
</script>

<style scoped>
.space {
    height: 2em;
    width: 2em;
}

.Comment {
    display: inline;
}

#MainCSS{
    background-color: white; 
    border-radius: 8px 8px 8px 8px;
}
</style>