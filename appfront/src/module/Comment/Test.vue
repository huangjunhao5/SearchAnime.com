<template>
    <!-- <img :src="bannerImgArray[0].address"> -->
    <!-- {{ updateElem }} -->
    <el-carousel :loop="false" :autoplay="false" height="204px" :key="updateElem.length">
        <el-carousel-item class="el-car-item" v-for="(list, index) in updateElem" :key="index">
            <!-- <img v-for="(imgList,index2) in list" :key="index2" class="top-img" :src="imgList.fields.cover" :alt="imgList.feilds.title" /> -->
            <el-row >
                <el-col id="img" :span="4" v-for="(anime ,index) in list" :key="index"><img :src="anime.fields.cover"></el-col>
            </el-row>
        </el-carousel-item>
    </el-carousel>
</template>


<script>
// import { before } from 'lodash';
import { ArrowLeft, ArrowRight } from '@element-plus/icons-vue';

import { fill } from 'lodash';

export default {
    name: "HomePage",
    data() {
        return {
            bannerHeight: (document.documentElement.clientWidth * 800 * 0.7) / 2400 + "px",    //屏幕自适应高度
            pleaseLoginHeight:(document.documentElement.clientWidth*300 * 0.67) / 1286 +"px",   //为你推荐模糊自适应高度
            bannerImgArray: [   //banner图片
                {
                    text: '间谍过家家',
                    address: require('../../../src/assets/bannerImage/间谍过家家banner.png'),
                    link: '/AnimePage?media_id=28237119',
                    temp:[
                        {
                            a: 1,
                        }
                    ]
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
            currentUpdatedAnimePage: 1,
            updatedAnimePageSize: 5,
            updateElem: [],
            bannerShow: false,
        }
    },
    components: {
        //
    },
    created() {
        //
        document.title = "首页";
        // this.axios.get("/Anime/api/GetAllAnime").then((res) => {
        //     if (res.data.code === "ok") {
        //         this.$data.allAnimeList = res.data.data;
        //         this.$data.listLength = this.$data.allAnimeList.length;
        //         for (let i = 0; i < 5; i++) {
        //             let n = Math.floor(Math.random() * this.listLength);
        //             if (this.$data.allAnimeList[n].fields.score >= 8) {
        //                 this.$data.recommendedAnimeList.push(this.$data.allAnimeList[n]);
        //             } else {
        //                 i--;
        //             }
        //         }
        //     }

        // });
        this.axios.get("http://api.studyserver.icu/Anime/api/GetUnFinishedAnime").then((res) => {
            if (res.data.code === "ok") {
                this.$data.updatedAnimeList = res.data.data;
                // console.log(res.data.data);
                let tres = [];
                let tlen = this.$data.updatedAnimeList.length;
                for (let i = 0; i * 5 < tlen;i ++) {
                    let temp = [];
                    for (let j = 0; j < 5 && i * 5 + j < tlen; j++) {
                        let pos = i * 5 + j;
                        temp.push(this.$data.updatedAnimeList[pos]);
                    }
                    tres.push(temp);
                    // console.log(temp);
                }
                this.$data.updateElem = tres;
                console.log(this.$data.updateElem);
                this.$data.bannerShow = true;
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
        clickPreviousPage() {

        },
        clickNextPage() {

        }
    },
    mounted() {
        window.onresize = () => {
            return (() => {
                if (document.documentElement.clientWidth > 960) {
                    this.bannerHeight = (document.documentElement.clientWidth * 800 * 0.7) / 2400 + "px";
                    this.pleaseLoginHeight = (document.documentElement.clientWidth * 300 * 0.67) / 1286 + "px"
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
#img img{
    height: 100%;
    width: 100%;
}

#UpElem{
    position: absolute;
    left: 1rem;
    bottom: 2rem;
}
.el-carousel__container {
    background-color: #e0e0e0;
    overflow: hidden;
    border-radius: 8px 8px 8px 8px;
    box-shadow: 0px 10px 20px #e0e0e0;
}

.el-carousel__item {
    background-color: #e0e0e0;
    overflow: hidden;
    box-shadow: 0px 10px 20px #e0e0e0;
    border-radius: 8px 8px 8px 8px;
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
    /* box-shadow:0px 10px 20px #ccc; */
    overflow: hidden;
}

#homeBanner img {
    width: 100%;
    height: 100%;
    cursor: pointer;
    /* border-radius: 8px 8px 8px 8px; */
}

.space {
    width: 1em;
    height: 1em;
}
#pleaseLogin{
    position: absolute;
    width: 67%;
    height: v-bind(pleaseLoginHeight);
    background-color: rgba(160, 160, 160, 0.973);
    z-index: 8;
    -webkit-filter: blur(10px);
    -moz-filter: blur(10px);
    -ms-filter: blur(10px);    
    filter: blur(10px);
}
#pleaseLogin span{
    -webkit-filter: blur(0px);
    -moz-filter: blur(0px);
    -ms-filter: blur(0px);
    filter: blur(0px);
    
}
#recommendedForYou {
    width: 70%;
    margin: auto;
    margin-top: 60px;
    background-color: white;
    border-radius: 8px 8px 8px 8px;
    padding: 1.5em;
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
    /* text-overflow: -webkit-ellipsis-lastline; */
    display: -webkit-box;
    -webkit-line-clamp: 1;
    /* line-clamp: 1; */
    -webkit-box-orient: vertical;
}

#updatedThisWeek {
    width: 70%;
    margin: auto;
    margin-top: 40px;
    background-color: white;
    border-radius: 8px 8px 8px 8px;
    padding: 1.5em;
}

#updatedThisWeek span {
    font-size: 24px;
    font-family: "微软雅黑";
    font-weight: bold;
}

/* #recentHotAnime{
    width: 70%;
    margin: auto;
    margin-top: 40px;
    background-color: white; 
    border-radius: 8px 8px 8px 8px;
    padding: 1.5em;
}
#recentHotAnime span {
    font-size: 24px;
    font-family: "微软雅黑";
    font-weight: bold;
} */
.foot {
    height: 100px;
}
</style>