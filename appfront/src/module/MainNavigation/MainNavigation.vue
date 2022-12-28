<template>
    <div id="MainNavigation">
        <ul>
            <li v-for="(nav, index) in mainNaviText"
                :key="index" @click="Li_Click_Event(nav.link,nav.text,index)"
                :class="nav.link"
                :style="{color: nav.color}"
            >
                {{ nav.text }}
            </li>
        </ul>
        <div id="logo">SMW</div>
        <div id="searchBox">
            <el-autocomplete
                v-model="inputValue"
                :fetch-suggestions="querySearch"
                :trigger-on-focus="false"
                placeholder="搜索番剧"
                clearable
                @select="handleSelect"
                @keyup.enter="searchAnimeClickEvent"
                v-on:focus="InputOnFocusEvent"
                v-on:blur="InputOnBlurEvent"
            ></el-autocomplete>
            <button @click="searchAnimeClickEvent">搜索</button>
        </div>
        <!--自适应搜索栏-->
        <button class="btn btn-primary" id="smallSearchBox" @click="clickMiniSearchBox"><i class="bi bi-search"></i></button>
        <!-- 用户状态显示菜单 -->
        <div id="user-tools" style="float:right;">
            <div v-if="uid" style="margin: 0em 2em;">
                <!-- 占位，如果已经登录显示人头 -->
                <el-dropdown>
                    <span class="el-dropdown-link">
                        <i class="bi bi-person-circle" style="font-size:2em;"></i>
                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item disabled>{{username}}</el-dropdown-item>
                            <el-dropdown-item @click="userInfoClickEvent">用户主页</el-dropdown-item>
                            <el-dropdown-item @click="userSettingClickEvent">用户设置</el-dropdown-item>
                            <el-dropdown-item @click="userUpdateClickEvent">最近评论</el-dropdown-item>
                            <el-dropdown-item @click="dialogTableVisible = true" divided>退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </div>
            <div v-else style="float:right; margin: -0.5em 2em;">
                <!-- 如果没登陆显示登录和注册按钮 -->
                <button class="btn btn-primary" id="loginButton"
                        style="background-color: #e78fdc; border: 0;"
                        @click="loginButtonClick">登录
                </button>
                <div class="el-space"  style="width: 1em;"></div>
                <button class="btn btn-secondary" id="registerButton" @click="registerButtonClick" style="border: 0;">注册</button>
            </div>
        </div>
        <el-dialog v-model="dialogTableVisible" title="退出登录" width="25%">
            <p>你确定要退出登录吗？</p>
            <template #footer>
                <span class="dialog-footer">
                    <el-button class = "btn btn-secondary" @click="dialogTableVisible = false">取消</el-button>
                    <el-button class = "btn btn-primary" type="primary" @click="userLogoutClickEvent">
                        确定
                    </el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<style>
* {
    margin: 0;
    padding: 0;
}

#MainNavigation {
    width: 100%;
    height: 60px;
    background-color: rgb(235, 235, 235);
    position: fixed;
    top: 0px;
    left: 0px;
    box-shadow: 0 0 2px rgb(133, 133, 133);
    z-index: 9;
}

#MainNavigation ul {
    list-style: none;
    margin-left: 100px;
    cursor: pointer;
}

#MainNavigation ul li {
    float: left;
    line-height: 60px;
    padding: 0 20px;
    font-size: 14px;
}

#MainNavigation ul li:hover {
    background-color: rgb(219, 219, 219);
    box-shadow: 0px 1px 2px #a7a6a6;
}

#logo {
    position: fixed;
    top: 0;
    left: 10px;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 32px;
    font-weight: bold;
    color: hotpink;
    line-height: 60px;
}

#searchBox {
    position: fixed;
    top: 10px;
    left: 38%;
    /* vertical-align: middle */
}

#searchBox input:nth-child(1) {
    height: 40px;
    width: 450px;
    border-radius: 25px 0 0 25px;
    border: 2px solid #e78fdc;
    background: #fffbf2;
    color: black;
    vertical-align: top;
    font-size: 15px;
    text-indent: 15px;
}


/*#searchBox el-autocomplete {*/
/*    height: 40px;*/
/*    width: 450px;*/
/*    border-radius: 25px 0 0 25px;*/
/*    border: 2px solid #e78fdc;*/
/*    background: #fffbf2;*/
/*    !*color: #9E9C9C;*!*/
/*    color: black;*/
/*    !* vertical-align: top; *!*/
/*    !*font-size: 15px;*!*/
/*    !*text-indent: 15px;*!*/
/*}*/

#searchBox button {
    height: 40px;
    width: 70px;
    cursor: pointer;
    background: #e78fdc;
    border-radius: 0 25px 25px 0;
    border: none;
    font-weight: bold;
    font-size: 14px;
    vertical-align: bottom;
}
#smallSearchBox{
    border-radius: 100%;
    background-color: #e78fdc;
    border:none;
    position:fixed;
    top:80px;
    right:10px;
    display: none;
}

@media screen and (max-width:992px) {
    #MainNavigation ul{
        margin-left:65px ;
    }
    #loginButton{
        font-size: 12px;
        position: fixed;
        top:15px;
        right: 80px;
    }
    #registerButton{
        font-size: 12px;
        position: fixed;
        top: 15px;
        right: 20px;
    }
    #searchBox{
        display: none;
        top: 76px;
        left: auto;
        right: 50px;
    }
    #searchBox input:nth-child(1){
        width: 100px;
        height: 35px;
        font-size: 12px;
        vertical-align: bottom;
    }
    #searchBox button{
        height: 35px;
        width: 52px;
        font-size: 12px;
    }
    #smallSearchBox{
        display: block;
    }
}
</style>

<script>
import {watchEffect} from "vue";
import router from "@/router";


export default {
    name: 'MainNavigation',
    data() {
        return {
            uid: '',
            username: '',
            is_admin: '',
            activeColor: '#e78fdc', // 激活时的颜色
            unActiveColor: 'black', // 未激活时的颜色
            inputValue: "", //输入框中的内容
            showCustomer: false,
            dialogTableVisible: false,
            mainNaviText: [
                {
                    text: '首页',
                    link: '/home',
                    color: 'black',
                },
                {
                    text: '',
                    link: '/FindAnimePage',
                    color: 'black',
                },
                {
                    text: '排行榜',
                    link: '/RankPage',
                    color: 'black',
                },
                {
                    text: '精选评论',
                    link: '/NewCommentPage',
                    color: 'black',
                },
            ],
            searchRes: [],
        }
    },
    created() {
        // 加载页面时获取
        // 获取当前用户
        this.axios.get('AppUser/api/GetNowUser/').then((res) => {
            if (res.data.code === 'ok') {
                this.$data.uid = res.data.result[0].fields.uid;
                this.$data.username = res.data.result[0].fields.open_name;
                this.$data.is_admin = res.data.result[0].fields.is_admin;
            }
        });
        // 加载路由，获取路由地址
        watchEffect(() => {
            router.getRoutes().map((item, index) => {
                if (item.path === router.currentRoute.value.path) {
                    for (let i = 0; i < 4; i++) {
                        this.$data.mainNaviText[i].color = this.$data.unActiveColor;
                    }
                    if (router.currentRoute.value.path === '/AnimePage' || router.currentRoute.value.path === '/SearchResultPage') {
                        return;
                    }
                    if (index < 2) index = 2;
                    this.$data.mainNaviText[index - 2].color = this.$data.activeColor;
                    // console.log(router.currentRoute.value.path)
                    // console.log(index);
                }
            })
        });
        // 获取番剧名称列表，用于搜索提示
        this.axios.get('Anime/api/GetAllAnimeTitle/').then((res) => {
            if (res.data.code === 'ok') {
                //
                this.$data.searchRes = res.data.data;
                // console.log(this.$data.searchRes);
            }
        })
    },
    methods: {
        // 当导航栏当元素被点击时，实现路由跳转并改变导航栏的样式
        Li_Click_Event: function (LinkTo, Text, pos) {
            for (let i = 0; i < 4; i++) {
                this.$data.mainNaviText[i].color = this.$data.unActiveColor;
            }
            document.title = Text;
            this.$data.mainNaviText[pos].color = this.$data.activeColor;
            if (LinkTo === '/RankPage') {
                this.$router.push({path: LinkTo, query: {page: 1}});
                return;
            }
            this.$router.push({path: LinkTo});
        },
        InputOnFocusEvent() {
            // 聚焦时显示下拉框
            this.$data.showCustomer = true;
        },
        InputOnBlurEvent() {
            // 失去焦点时隐藏下拉框
            this.$data.showCustomer = false;
        },
        handleSelect(item) {
            // 选中时触发的事件
            // 在新标签页打开路由
            let routeUrl = this.$router.resolve({
                path: '/AnimePage',
                query: {media_id: item.media_id}
            })
            window.open(routeUrl.href, '_blank');
        },
        querySearch(queryString, cb) {
            // 下拉框的内容
            let res = this.$data.searchRes;
            let results = queryString ? res.filter(this.createFilter(queryString)) : res;
            cb(results);
        },
        createFilter(queryString) {
            return (restaurant) => {
                return (restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
            };
        },
        searchAnimeClickEvent() {
            let routeUrl = this.$router.resolve({
                path: '/SearchResultPage',
                query: {
                    keyword: this.$data.inputValue,
                    page: 1,
                }
            })
            window.open(routeUrl.href, '_blank');
        },
        loginButtonClick() {
            window.location.href = '/login';
        },
        registerButtonClick() {
            window.location.href = '/register';
        },
        userInfoClickEvent(){
            window.open('/UserMainPage#/UserInfo?uid=' + this.$data.uid, '_blank');
        },
        userSettingClickEvent(){
            window.open('/UserMainPage#/UserSetting?uid=' + this.$data.uid, '_blank');
        },
        userUpdateClickEvent(){
            window.open('/UserMainPage#/UserUpdate?uid=' + this.$data.uid, '_blank');
        },
        userLogoutClickEvent(){
            // 用户登出函数
            this.$data.dialogTableVisible = false;
            this.axios.get('/AppUser/api/logout/').then((res) => {
                if(res.data.code === 'ok'){
                    this.$message({
                        message: '退出登录成功',
                        type: 'success',
                        center: true,
                    })
                    window.location.reload();
                }else{
                    this.$message({
                        message: res.data.message,
                        type: 'error',
                        center: true,
                    })
                }
            })
        },
        clickMiniSearchBox(){
            let miniSearchbox = document.getElementById("searchBox");
            if (miniSearchbox.style.display == "none") {
                miniSearchbox.style.display = "block";
            } else {
                miniSearchbox.style.display = "none";
            }
        }
    }
}
</script>