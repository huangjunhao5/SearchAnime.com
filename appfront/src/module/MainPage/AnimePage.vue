<template>
    <div id="sss">
        <el-row>
            <el-col>
                <div class='space' style="height: 5em;" />
            </el-col>
        </el-row>
        <div class="row justify-content-md-center">
            <div class="col-md-auto" style="width: 60em;">
                <el-row id="MainCSS" style="height: 115%; ">
                    <el-col :span="6">
                        <el-row>
                            <div class="space" style="height: 3em;"></div>
                        </el-row>
                        <div class="row justify-content-md-center">
                            <div class="col col-lg"></div>
                            <div id='img' class="col-md-auto">
                                <img :src="animeData.cover">
                            </div>
                        </div>

                    </el-col>
                    <el-col :span="18">
                        <el-row>
                            <div class="space" style="height: 6vh;width: 4em;"></div>
                        </el-row>
                        <el-row>
                            <el-col :span="2">
                                <div class="space"></div>
                            </el-col>
                            <el-col :span="20">
                                <h2 class="AnimeTitle">
                                    {{ animeData.title }}
                                </h2>
                            </el-col>
                        </el-row>
                        <el-row>
                            <div class="space"></div>
                        </el-row>
                        <el-row>
                            <el-col :span="2">
                                <div class="space"></div>
                            </el-col>
                            <el-col :span="20">
                                <h5 class="subTitle">
                                    {{ animeData.subTitle }}
                                </h5>
                            </el-col>
                        </el-row>
                        <el-row>
                            <div class="space"></div>
                        </el-row>
                        <el-row>
                            <el-col :span="2">
                                <div class="space"></div>
                            </el-col>
                            <el-col :span="20">
                                <a :href="animeData.link" target="_blank">观看链接</a>
                            </el-col>
                        </el-row>
                        <el-row>
                            <div class="space"></div>
                        </el-row>
                        <el-row>
                            <el-col :span="2">
                                <div class="space"></div>
                            </el-col>
                            <el-col :span="20">
                                <div class="state">
                                    <div v-if='animeData.is_finish === 1'>
                                        已完结，{{ animeData.index_show }}
                                    </div>
                                    <div v-else>
                                        {{ animeData.index_show }}
                                    </div>
                                </div>
                            </el-col>
                        </el-row>
                        <el-row>
                            <div class="space"></div>
                        </el-row>
                        <el-row>
                            <el-col :span="2">
                                <div class="space"></div>
                            </el-col>
                            <el-col :span="20">
                                <el-row>
                                    <el-col :span="5">
                                        <div class="Text">
                                            B 站评分 ：
                                        </div>
                                    </el-col>
                                    <el-col :span="8">
                                        <div class="rate">
                                            <el-rate disabled v-model="bilibiliScore"></el-rate>
                                        </div>
                                    </el-col>
                                    <el-col :span="7">
                                        <div class="Text">
                                            {{ animeData.score }}
                                        </div>
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col :span="5">
                                        <div class="Text">
                                            站内评分 ：
                                        </div>
                                    </el-col>
                                    <el-col :span="8">
                                        <div class="rate">
                                            <el-rate disabled v-model="scoreRes"></el-rate>
                                        </div>
                                    </el-col>
                                    <el-col :span="7">
                                        <div class="Text">
                                            {{ userScore }}
                                        </div>
                                    </el-col>
                                </el-row>
                            </el-col>
                        </el-row>
                    </el-col>
                </el-row>
            </div>
        </div>
        <el-row>
            <div class="space" style="height: 6em; width: 64em;"></div>
        </el-row>
        <div class="row justify-content-md-center">
            <div class="col-md-auto" id="MainCSS" style="width: 58.5em;">
                <div class="space" style="height: 2em;"></div>
                <el-row>
                    <el-col :span="2">
                        <div class="space"></div>
                    </el-col>
                    <el-col :span="14">
                        <div id="CommentForm" v-if="userId" style="height: 21.5em;">
                            <comment></comment>
                        </div>
                        <div v-else>
                            <h3>请<a href='/login'>登陆</a>后评论</h3>
                            <div class="space" style="height: 1.5em;" />
                        </div>
                    </el-col>
                </el-row>
            </div>
        </div>
        <el-row>
            <el-col>
                <div class="space" style="height:3em;"></div>
            </el-col>
        </el-row>
        <div class="row justify-content-md-center">
            <el-row class="col-md-auto" id="MainCSS" style="width: 58.8em;">
                <el-col :span="10" :offset="2">
                    <div class="ShowComment">
                        <div class="space" style="height: 4em;"></div>
                        <ShowComment></ShowComment>
                    </div>
                </el-col>
            </el-row>
        </div>
        <div class="space" />
        <div class="space" />
    </div>
</template>

<script>
import comment from "@/module/Comment/comment";
import ShowComment from "@/module/Comment/ShowComment.vue";
// import {GetMediaId} from "@/module/Comment/CommentFunctionLib";

export default {
    name: "AnimePage",
    data() {
        return {
            mediaId: '',
            userId: '',
            animeData: {},
            score: {},
            scoreRes: 0,
            bilibiliScore: 0,
            userScore: 0,
        };
    },
    components: {
        comment,
        ShowComment,
    },
    created() {
        this.$data.mediaId = this.$route.query.media_id;
        if (this.$data.mediaId == null || this.$data.mediaId == '') {
            window.location.href = '/NotFoundPage';
        }
        // console.log(this.$route.query)
        this.axios.get('/AppUser/api/GetNowUser/').then((res) => {
            if (res.data.code === 'ok') {
                this.$data.userId = res.data.result[0].fields.uid;
            }
        })
        this.axios.get('/Anime/api/GetAnimeByMediaId/' + this.$data.mediaId).then((res) => {
            if (res.data.code === 'ok') {
                this.$data.animeData = res.data.data[0].fields;
                this.$data.score = res.data.score[0].fields;
                this.$data.bilibiliScore = Math.ceil(this.$data.animeData.score / 2 - 0.5);

                document.title = this.$data.animeData.title + ' - 动漫详情';
                if (!this.$data.score.cnt) {
                    this.$data.scoreRes = 0;
                } else {
                    this.$data.scoreRes = Math.ceil((this.$data.score.sumScore / this.score.cnt - 0.5));
                    this.$data.userScore = (this.$data.score.sumScore / this.score.cnt) * 2;
                    this.$data.userScore = this.$data.userScore.toFixed(1);
                }
            } else {
                //跳转到Anime404页面
                window.location.href = '/NotFoundPage';
            }
        });
    }
}
</script>

<style scoped>
#MainCSS {
    background-color: white;
    border-radius: 8px 8px 8px 8px;
}

#img img {
    height: 100%;
    width: 100%;
    border-radius: 8px 8px 8px 8px;
}

#img {
    height: 85%;
    width: 85%;
}

.space {
    height: 1em;
    width: 1em;
}
</style>