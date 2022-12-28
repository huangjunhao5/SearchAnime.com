const {defineConfig} = require('@vue/cli-service')
const webpack = require("webpack")
module.exports = defineConfig({
    transpileDependencies: true,
    assetsDir: 'static',
	configureWebpack: {
		plugins: [
			// 配置 jQuery 插件的参数
			new webpack.ProvidePlugin({
				$: 'jquery',
				jQuery: 'jquery',
				'window.jQuery': 'jquery',
				Popper: ['popper.js', 'default']
			})
		]
	},
    pages: {
        login: {
            // 入口文件，相当于单页面的 main.js
            entry: 'src/module/login/login.js',
            // 模板文件
            template: 'public/index.html',
            // 编译后 dist 目录下输出的文件，可以包含子目录
            filename: 'login.html'
        },
        register: {
            // 入口文件，相当于单页面的 main.js
            entry: 'src/module/register/register.js',
            // 模板文件
            template: 'public/index.html',
            // 编译后 dist 目录下输出的文件，可以包含子目录
            filename: 'register.html'
        },
        MainPage: {
            // 入口文件，相当于单页面的 main.js
            entry: 'src/module/MainPage/MainPage.js',
            // 模板文件
            template: 'public/index.html',//'src/module/User/UserPage.html',
            // 编译后 dist 目录下输出的文件，可以包含子目录
            filename: 'index.html'
        },
        TestPage: {
            entry: 'src/module/Test.js',
            // 模板文件
            template: 'src/module/Test.html',
            // 编译后 dist 目录下输出的文件，可以包含子目录
            filename: 'Test.html'
        },
        UserMainPage: {
            entry: 'src/module/User/UserMainPage.js',
            template: 'src/module/User/UserPage.html',
            filename: 'UserMainPage.html',
        },
        NotFoundPage:{
            entry: 'src/module/NotFoundPage/NotFoundPage.js',
            template: 'src/module/NotFoundPag/NotFoundPage.html',
            filename: 'NotFoundPage.html',
        }
    },
    devServer: {
        host: 'localhost', //target host
        port: 8080,
        //proxy:{'/api':{}},代理器中设置/api,项目中请求路径为/api的替换为target
        proxy: {
            '/api': {
                target: 'http://api.studyserver.icu',//代理地址，这里设置的地址会代替axios中设置的baseURL
                changeOrigin: true,// 如果接口跨域，需要进行这个参数配置
                //ws: true, // proxy websockets
                //pathRewrite方法重写url
                pathRewrite: {
                    '^/api': '/'
                    //pathRewrite: {'^/api': '/'} 重写之后url为 http://192.168.1.16:8085/xxxx
                    //pathRewrite: {'^/api': '/api'} 重写之后url为 http://192.168.1.16:8085/api/xxxx
                },
            }
        }
    },
})