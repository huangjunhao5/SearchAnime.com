<template>
    <div class="row justify-content-md-center">
        <div class="col-md-auto" id="MainCSS" style="width: 60%;">
            <el-row>
                <el-col class='RankPage' >
                    <div class="space" />
                    <el-row >
                        <!-- <el-col :span="8">
                            <div class="space"></div>
                        </el-col> -->
                        <el-col :offset="3">
                            <div class="space"/>
                            <h2>{{ state.pageTitle }}</h2>
                        </el-col>
                    </el-row>
                    <el-row>
                        <div class="space" style="height: 5em;"></div>
                    </el-row>
                    <div v-for="(anime, key) of animeList.slice(pageSize * (currentPage - 1), pageSize * currentPage)"
                        :key="key">
                        <div @click="divClick(anime.fields.media_id)" class="AnimeList">
                            <el-row class='animeElem' style="width: 90em;">
                                <el-col :span="2" :offset="3">
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
                                            :style="'min-width:' + (anime.fields.title.length + 4) + 'em'">
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
                                            <el-rate disabled :model-value="anime.fields.user_sumScore / 2"></el-rate>
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
            </el-row>
            <div v-if="NoElem" style="text-align: center;">
                <img src="@/../public/static/image/404.png">
                <h3>啥都没有</h3>
                <div class="space"/>
            </div>            
            <el-row>
                <div class="space" style="height:1.5em;" />
            </el-row>
        </div>
    </div>


    <el-row v-if="animeList.length">
        <el-col>
            <div class="space" style="height: 3em;" />
            <div class='provider'>
                <el-config-provider :locale="locale">
                    <div class="space" style="flex: 1;" />
                    <el-pagination :locale="locale" background @current-change="handleCurrentChange"
                        :current-page="currentPage" :page-size="pageSize" layout="total, prev, pager, next, jumper"
                        :total="animeList.length">
                    </el-pagination>
                </el-config-provider>
                <div class="space" style="flex: 1;" />
            </div>
        </el-col>
    </el-row>
    <el-row>
        <el-col>
            <div class='space' />
        </el-col>
    </el-row>
</template>

<script>
import { defineComponent, getCurrentInstance, reactive, watchEffect } from 'vue'
import zhCn from 'element-plus/dist/locale/zh-cn.mjs'
import { ElConfigProvider } from 'element-plus'

export default defineComponent({
    name: "ListAnime",
    components: {
        ElConfigProvider,
    },
    props: {
        url: {
            type: String,
            default: '111',
        },
        title: {
            type: String,
            default: '111',
        }
    },
    data() {
        return {
            currentPage: 1,
            pageSize: 10,
            NoElem: 0,
            animeList: [],
        }
    },
    created() {
        this.$data.currentPage = this.$route.query.page;
        this.axios.get(this.state.getUrl).then((res) => {
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
        if (
            this.$data.currentPage == null
            || this.$data.currentPage == ''
            || this.$data.currentPage > this.$data.animeList.length
        ) this.$data.currentPage = 1;
    },
    methods: {
        divClick(routeLink) {
            // alert(routeLink);
            // window.location.href = '/#/AnimePage?media_id=' + routeLink;
            this.$router.push({ path: '/AnimePage', query: { media_id: routeLink } });
        },
        scrollTop(selector) {
            let element = selector && document.querySelector(selector) || window;
            element.scrollTo(0, 0);
        },
        handleCurrentChange(val) {
            this.currentPage = val;
            this.scrollTop(".tabledns");
        },
    },
    setup(props) {
        const state = reactive({
            getUrl: props.url,
            pageTitle: props.title,
        })
        return {
            locale: zhCn,
            state,
            //
        }
    },
})
</script>

<style scoped>


.img img {
    height: 100%;
    width: 100%;
    border-radius: 8px 8px 8px 8px;
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

#MainCSS {
    background-color: white;
    border-radius: 8px 8px 8px 8px;
}
</style>