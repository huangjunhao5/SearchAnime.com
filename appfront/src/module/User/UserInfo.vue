<template>
    <div class="container-fluid" style="width: 100%;">
        <div class="row" id="MainCSS">
            <div class="space" style="height: 2em;" />
            <el-row>
                <el-col :offset="1">
                    <div>
                        <i class="bi bi-person-circle" style="font-size: 2em;">{{ openname }}</i>
                    </div>
                </el-col>

            </el-row>
            <div class="space" />
            <el-row>
                <el-col v-if="is_admin" :offset="1">
                    管理员
                </el-col>
                <el-col v-else :offset="1">
                    普通用户
                </el-col>
            </el-row>
            <div class="space" />
            <el-row>
                <el-col :offset="1">
                    <div>{{ about }}</div>
                </el-col>
            </el-row>
            <div class="space" style="height: 2em;" />
        </div>
        <div class="row">
            <div class="space"/>
        </div>
        <div class='row'>
            <div class="col" id="MainCSS">
                <el-row>
                    <el-col class='RankPage' :span="16">
                        <div class="space" />
                        <el-row>
                            <!-- <el-col :span="8">
                            <div class="space"></div>
                        </el-col> -->
                            <el-col :offset="2">
                                <h2>最近浏览</h2>
                            </el-col>
                        </el-row>
                        <el-row>
                            <div class="space" style="height: 4em;"></div>
                        </el-row>
                        <div v-for="(anime, key) of animeList.slice(0, 4)" :key="key">
                            <div @click="divClick(anime.fields.media_id)" class="AnimeList">
                                <el-row class='animeElem' style="width: 100em;">
                                    <el-col :span="2" :offset="2">
                                        <div class='img'>
                                            <img :src="anime.fields.cover">
                                        </div>
                                    </el-col>
                                    <el-col :span="1">
                                        <div class="space"></div>
                                    </el-col>
                                    <el-col :span="16">
                                        <el-row>
                                            <el-col>
                                                <div class="space"></div>
                                            </el-col>
                                        </el-row>
                                        <el-row>
                                            <el-col :span="1"
                                                :style="'min-width:' + (anime.fields.title.length + 1) + 'em'">
                                                <div class='AnimeTitle'>
                                                    {{ anime.fields.title }}
                                                </div>
                                            </el-col>
                                        </el-row>
                                        <el-row>
                                            <el-col>
                                                <div class="space"></div>
                                            </el-col>
                                        </el-row>
                                        <el-row>
                                            <el-col :span="2">
                                                <div>B 站评分</div>
                                            </el-col>
                                            <el-col :span="3">
                                                <el-rate disabled :model-value="anime.fields.score / 2"></el-rate>
                                            </el-col>
                                            <el-col :span="3">
                                                {{ anime.fields.score }}
                                            </el-col>
                                        </el-row>
                                        <el-row>
                                            <el-col :span="2">
                                                <div>站内评分：</div>
                                            </el-col>
                                            <el-col :span="3">
                                                <el-rate disabled
                                                    :model-value="anime.fields.user_sumScore / 2"></el-rate>
                                            </el-col>
                                            <el-col :span="3">
                                                {{ (anime.fields.user_sumScore).toFixed(1) }}
                                            </el-col>
                                        </el-row>
                                    </el-col>
                                </el-row>
                                <el-row>
                                    <el-col>
                                        <div class="space"></div>
                                    </el-col>
                                </el-row>
                            </div>
                        </div>
                    </el-col>
                    <el-col :span="4">
                        <div class="space"></div>
                    </el-col>
                </el-row>
                <div v-if="NoElem" style="text-align: center;">
                    <img src="@/../public/static/image/404.png">
                    <h3>啥都没有</h3>
                    <div class="space" />
                </div>
                <el-row>
                    <div class="space" style="height:1em;" />
                </el-row>
            </div>
        </div>
    </div>
</template>

<script>
// import {GetUid} from './UserFunctionLib';
import ListAnime from "@/module/MainPage/ListAnime/ListAnime.vue";

export default {
    name: "UserInfo",
    components: {
        // ListAnime,
    },
    data() {
        return {
            username: '',
            uid: '',
            openname: '',
            is_admin: '',
            about: '',
            NoElem: 0,
            animeList: [],
        }
    },
    created() {
        let uid = this.$route.query.uid;
        if (uid == null || uid === '') {
            //跳转到用户404界面
            // alert('a');
            window.location.href = '/NotFoundPage';
        }
        // alert(uid);
        this.axios.get('/AppUser/api/GetUserInformation/' + uid).then((res) => {
            // alert(res.data.code);
            if (res.data.code === "error") {
                //跳转到用户404界面
                // alert('b');
                window.location.href = '/NotFoundPage';
            } else {
                //
                // alert('c');
                let userData = res.data.result[0].fields;
                this.$data.openname = userData.open_name;
                this.$data.about = userData.about;
                this.$data.uid = userData.uid;
                this.$data.is_admin = userData.is_admin;
                this.$data.username = userData.username;

            }
            this.axios.get('/AppUser/api/GetVisited/' + uid).then((res) => {
                if (res.data.code === 'ok') {
                    this.$data.animeList = res.data.data;
                } else {
                    // alert(res.data.message);
                    this.NoElem = 1;
                    this.$message({
                        message: '啥都没有',
                        type: 'error',
                        center: true,
                    })
                }
            });
        })
    },

    methods: {
        divClick(routeLink) {
            // alert(routeLink);
            // window.location.href = '/#/AnimePage?media_id=' + routeLink;
            this.$router.push({ path: '/AnimePage', query: { media_id: routeLink } });
        },
    },
}
</script>

<style scoped>
*{
    overflow-x: hidden;
}

.row{
    margin-left: 0;
    margin-right: 0;
}

#MainCSS {
    background-color: white;
    border-radius: 8px 8px 8px 8px;
}

.UserInfo {
    float: left;
    left: 20%;
    margin: auto 5em;
}

.icon {
    float: left;
    left: 20%;
}

.name {
    float: left;
    text-align: right;
    margin: 2em 2em;
}

.space1 {
    height: 5em;
}

.img img {
    height: 100%;
    width: 100%;
}

.space {
    height: 2em;
    width: 2em;
}

.AnimeList {
    cursor: pointer;
}

.provider {
    display: flex;
}
</style>