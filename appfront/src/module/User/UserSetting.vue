<template>
    <div>
        <ChangeInfo></ChangeInfo>
        <div class='space'></div>
        <ChangeUserPassword></ChangeUserPassword>
        <!--    <v-form-render :form-json="formJson" :form-data="formData" :option-data="optionData" ref="vFormRef">-->
        <!--    </v-form-render>-->
        <!--    <el-button type="primary" @click="submitForm">确认更改</el-button>-->
    </div>
</template>

<script>

import ChangeInfo from "@/module/User/ChangeInfo";
import ChangeUserPassword from "@/module/User/ChangeUserPassword";

export default {
    name: 'UserSetting',
    components: {
        ChangeInfo,
        ChangeUserPassword,
    },
    data() {
        return {};
    }
}
</script>

<style scoped>
.space {
    height: 4em;
}

/* #MainCSS{
    background-color: white; 
    border-radius: 10px 10px 10px 10px;
} */

</style>
