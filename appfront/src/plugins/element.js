import ElementPlus from 'element-plus'
import '../element-variables.scss'
import zhCn from 'element-plus/lib/locale/lang/zh-cn'
// import { use as localeUse } from 'element-plus/lib/locale'

export default (app) => {
  app.use(ElementPlus, { locale: zhCn})
}
