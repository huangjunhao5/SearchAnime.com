<template>
    <!-- 主界面信息 -->
    <div id="Home">
        <div id="homeBanner"> <!--Banner-->
            <el-carousel trigger="click" :height="bannerHeight" id="bannerCarousel">
                <el-carousel-item v-for="(item, index) in bannerImgArray" :key="index">
                    <img :src="item.address" :alt=item.text @click="clickBannerEvent(item.link)">
                </el-carousel-item>
            </el-carousel>
        </div>
        <!-- <div class="space" style="height: 1em;"/> -->
        <div id="recommendedForYou">
            <el-row>
                <div class="space" style="height: 1.5em;"/>
            </el-row>
            <el-row>
                <el-col :span="8" :offset="1"><span>为你推荐</span></el-col>
                <el-col :xs="7" :sm="10" :md="11" :lg="12" :xl="12"></el-col>
                <el-col :span="2">
                    <el-button size="small" icon="el-icon-refresh-right" type="changeButton" @click="clickChangeButton"
                               round>换一批
                    </el-button>
                </el-col>
            </el-row>
            <div id="pleaseLogin" v-show="!isLogin"><span @click="clickLoginEvent">请登录</span></div>
            <el-row>
                <div class="space" style="height: 2em;"></div>
            </el-row>
            <el-row justify="space-around">
                <el-col v-for="item in recommendedAnimeList" :key="item.fields.media_id" :span="3">
                    <el-image :src="item.fields.cover" :fit="cover" @click="clickAnimeEvent(item.fields.media_id)"
                              style="cursor: pointer;"/>
                </el-col>
            </el-row>
            <el-row justify="space-around">
                <el-col v-for="item in recommendedAnimeList" :key="item.fields.media_id" :span="3"
                        style="text-align: center;">
                    <span class="homeAnimeTitle" :title="item.fields.title"
                          @click="clickAnimeEvent(item.fields.media_id)" style="font-size: small;">
                        {{ item.fields.title }}
                    </span>
                </el-col>
            </el-row>
            <el-row>
                <div class="space" style="height:2em;"/>
            </el-row>
        </div>
        <div id="updatedThisWeek">
            <el-row>
                <el-col :span="8" :offset="1"><span>本周更新</span></el-col>
            </el-row>
            <el-row>
                <div class="space" style="height: 2em;"></div>
            </el-row>
            <el-row>
                <el-carousel indicator-position="none" id="UpElem" :height="screenheight"
                             :autoplay="false" :key="updateElem.length">
                    <el-carousel-item v-for="(items, key) in updateElem" :key="key">
                        <el-row>
                            <el-col
                                v-for="item in items"
                                :key="item.fields.media_id"
                                :span="3"
                                :offset="1"
                            >
                                <el-image :src="item.fields.cover" :fit="cover"
                                    @click="clickAnimeEvent(item.fields.media_id)" style="cursor: pointer;"/>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col
                                v-for="item in items"
                                :key="item.fields.media_id"
                                :span="3"
                                style="text-align: center;"
                                :offset="1"
                            >
                                <span class="homeAnimeTitle" :title="item.fields.title"
                                    @click="clickAnimeEvent(item.fields.media_id)" style="font-size: small;">
                                    {{ item.fields.title }}
                                </span>
                            </el-col>
                        </el-row>
                    </el-carousel-item>
                </el-carousel>
            </el-row>
            <el-row>
                <div class="space"/>
            </el-row>
        </div>
        <div id="recentHotAnime">
            <el-row>
                <el-col :span="8" :offset="1"><span>最近热门</span></el-col>
            </el-row>
            <el-row>
                <div class="space" style="height: 2em;"></div>
            </el-row>
            <el-row justify="space-around">
                <el-col v-for="item in recentHotAnimeList" :key="item.fields.media_id" :span="3">
                    <el-image :src="item.fields.cover" :fit="cover" @click="clickAnimeEvent(item.fields.media_id)"
                              style="cursor: pointer;"/>
                </el-col>
            </el-row>
            <el-row justify="space-around">
                <el-col v-for="item in recentHotAnimeList" :key="item.fields.media_id" :span="3"
                        style="text-align: center;">
                    <span class="homeAnimeTitle" :title="item.fields.title"
                          @click="clickAnimeEvent(item.fields.media_id)"
                          style="font-size: small;">
                        {{ item.fields.title }}
                    </span>
                </el-col>
            </el-row>
            <el-row>
                <div class="space" style="height: 2em;"/>
            </el-row>
        </div>
    
        <div class="foot"></div>
    </div>
</template>

<script>
// import { before } from 'lodash';
import {ArrowLeft, ArrowRight} from '@element-plus/icons-vue';

import {fill} from 'lodash';

export default {
    name: "HomePage",
    data() {
        return {
            bannerHeight: (document.documentElement.clientWidth * 800 * 0.7) / 2400 + "px",    //屏幕自适应高度
            pleaseLoginHeight: (document.documentElement.clientWidth * 310 * 0.7) / 1286 + "px",   //为你推荐模糊自适应高度
            recommendedForYouHeight: (document.documentElement.clientWidth * 370 * 0.7) / 1250 + "px",
            screenheight: document.documentElement.clientHeight / 4 + 'px',         //本周更新自适应高度
            bannerImgArray: [   //banner图片
                {
                    text: '间谍过家家',
                    address: require('../../../src/assets/bannerImage/间谍过家家banner.png'),
                    link: '/AnimePage?media_id=28237119',
                    // isActivated: true
                },
                {
                    text: '灵能百分百第三季',
                    address: require('../../../src/assets/bannerImage/灵能百分百第三季banner.png'),
                    link: '/AnimePage?media_id=28339709',
                    // isActivated: false
                },
                {
                    text: '孤独摇滚',
                    address: require('../../../src/assets/bannerImage/孤独摇滚banner.png'),
                    link: '/AnimePage?media_id=28339735',
                    // isActivated: false
                },
                {
                    text: '因为是反派大小姐所以养了魔王',
                    address: require('../../../src/assets/bannerImage/因为是反派大小姐所以养了魔王banner.png'),
                    link: '/AnimePage?media_id=28339714',
                    // isActivated: false
                },
                {
                    text: 'JOJO的奇妙冒险 石之海',
                    address: require('../../../src/assets/bannerImage/JOJO的奇妙冒险 石之海banner.png'),
                    link: '/AnimePage?media_id=28235123',
                    // isActivated: false
                }
            ],
            recommendedAnimeList: [],    //为你推荐
            allAnimeList: [],
            listLength: 0,
            updatedAnimeList: [],      //每周更新
            //currentUpdatedAnimePage: 1,
            //updatedAnimePageSize: 5,
            updateElem: [],
            isLogin: false,
            recentHotAnimeList: [],     //最近热门
        }
    },
    components: {
        //
    },
    created() {
        //
        document.title = "首页";
        this.axios.get("/Anime/api/GetAllAnime").then((res) => {
            if (res.data.code === "ok") {
                this.$data.allAnimeList = res.data.data;
                this.$data.listLength = this.$data.allAnimeList.length;
                for (let i = 0; i < 5; i++) {
                    let n = Math.floor(Math.random() * this.listLength);
                    if (this.$data.allAnimeList[n].fields.score >= 8) {
                        this.$data.recommendedAnimeList.push(this.$data.allAnimeList[n]);
                    } else {
                        i--;
                    }
                }
            }

        });
        this.axios.get("/Anime/api/GetUnFinishedAnime").then((res) => {
            if (res.data.code === "ok") {
                this.$data.updatedAnimeList = res.data.data;
                let tres = [];
                let tlen = this.$data.updatedAnimeList.length;
                for (let i = 0; i * 5 < tlen; i++) {
                    let temp = [];
                    for (let j = 0; j < 5 && i * 5 + j < tlen; j++) {
                        let pos = i * 5 + j;
                        temp.push(this.$data.updatedAnimeList[pos]);
                    }
                    tres.push(temp);
                }
                this.$data.updateElem = tres;
            }
        });
        this.axios.get("/AppUser/api/GetNowUser").then((res) => {
            if (res.data.code === "ok") {
                this.$data.isLogin = true;
            } else {
                this.$data.isLogin = false;
            }
        });
        this.axios.get("/Anime/api/GetMostHotAnime").then((res) => {
            if (res.data.code === "ok") {
                this.$data.recentHotAnimeList = res.data.data;
            }
        });
    },
    methods: {
        clickBannerEvent(item) {
            this.$router.push(item);
        },
        clickChangeButton() {
            for (let i = 0; i < 5; i++) {
                let n = Math.floor(Math.random() * this.listLength);
                if (this.$data.allAnimeList[n].fields.score >= 8) {
                    this.$data.recommendedAnimeList[i] = this.$data.allAnimeList[n];
                } else {
                    i--;
                }
            }
        },
        clickAnimeEvent(item) {
            let link = "/AnimePage?media_id=" + item;
            this.$router.push(link);
        },
        clickLoginEvent() {
            window.location.href = '/login';
        },
    },
    mounted() {
        window.onresize = () => {
            return (() => {
                if (document.documentElement.clientWidth > 960) {
                    this.bannerHeight = (document.documentElement.clientWidth * 800 * 0.7) / 2400 + "px";
                    this.pleaseLoginHeight = (document.documentElement.clientWidth * 320 * 0.7) / 1286 + "px";
                    this.screenheight = document.documentElement.clientHeight / 4 + 'px';
                    this.recommendedForYouHeight = (document.documentElement.clientWidth * 370 * 0.7) / 1250 + "px"
                }
            })();
        }
    },
}
</script>

<style scoped>
* {
    margin: 0px;
    padding: 0px;
}

/*#UpElem[data-v-6344c61c] {*/
/*    width: 100%;*/
/*}*/

#UpElem[class]{
    width: 100%;
}

#UpElem[id]{
    width: 100%;
}

.el-carousel__item{
    width:100%;
}

.el-carousel__container {
    border-radius: 8px 8px 8px 8px;
    width: 100%;
}

.el-carousel__item {
    border-radius: 8px 8px 8px 8px;
}

#UpElem .el-carousel__container{
    height: 300px;
}

.el-image {
    border-radius: 8px 8px 8px 8px;
}

#bannerCarousel {
    width: 70%;
    margin: auto;
}

#homeBanner {
    border-radius: 8px 8px 8px 8px;
    overflow: hidden;
}

#homeBanner img {
    width: 100%;
    height: 100%;
    cursor: pointer;
}

.space {
    width: 1em;
    height: 1em;
}

#pleaseLogin {
    position: absolute;
    margin: auto;
    width: 70%;
    height: v-bind(pleaseLoginHeight);
    background-color: rgba(255, 255, 255, 0.973);
    z-index: 8;
    text-align: center;
    line-height: v-bind(pleaseLoginHeight);
    border-radius: 8px 8px 8px 8px;

}

#pleaseLogin span {
    cursor: pointer;
}



#recommendedForYou {
    width: 70%;
    margin: auto;
    margin-top: 60px;
    background-color: white;
    border-radius: 8px 8px 8px 8px;
    height: v-bind(recommendedForYouHeight);
}

#recommendedForYou span {
    font-size: 24px;
    font-family: "微软雅黑";
    font-weight: bold;
}

.el-button--changeButton.is-active,
.el-button--changeButton:focus,
.el-button--changeButton:active {
    background-color: #fdbff3;
    border-color: #cacaca;
    color: #494949;
}


.el-button--changeButton:hover {
    background-color: #fff;
    border-color: #f16bdb;
    color: #f548d8;
}

.el-button--changeButton {
    color: #494949;
    background-color: #fdbff3;
    border-color: #cacaca;
}

.homeAnimeTitle {
    font-size: small;
    cursor: pointer;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
}

#updatedThisWeek {
    width: 70%;
    margin: auto;
    margin-top: 60px;
    background-color: white;
    border-radius: 8px 8px 8px 8px;
    padding: 1.5em 0 1.5em 0;
}

#updatedThisWeek span {
    font-size: 24px;
    font-family: "微软雅黑";
    font-weight: bold;
}

#recentHotAnime {
    width: 70%;
    margin: auto;
    margin-top: 60px;
    background-color: white;
    border-radius: 8px 8px 8px 8px;
    padding: 1.5em 0 1.5em 0;
}

#recentHotAnime span {
    font-size: 24px;
    font-family: "微软雅黑";
    font-weight: bold;
}
#UpElem .el-row {
    margin-left: 110px;
}
@media screen and (max-width: 768px) {
    #pleaseLogin {
        height: 150px;
        line-height: 120px;
    }
    #recommendedForYou{
        height: 220px;   
    }
    #UpElem .el-row {
        margin-left: 25px;
    }
}

.foot {
    height: 100px;
}
</style>