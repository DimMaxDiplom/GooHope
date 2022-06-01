<template>
    <div class="header">
        <div class="header_logo">
            <img src="@/assets/logo.png" alt="" class="header_logo-logo" @click="main">
        </div>
        <nav class="header_nav">
            <router-link to="/" class="header_nav-elem">Магазин</router-link>
            <router-link to="/" class="header_nav-elem">Сообщество</router-link>
            <router-link to="/" class="header_nav-elem">О GooHope</router-link>
            <router-link to="/" class="header_nav-elem">Поддержка</router-link>
        </nav>
        <div class="header_side">
            <router-link to="/sign_in" class="header_side-login" v-if="!token">Войти</router-link>
            <router-link :to="`/profile/${user_id}`" class="header_side-login" v-else>Профиль</router-link>
            <div class="header_side-download" v-if="!token">Установить <span>GooHope</span></div>
            <div class="header_side-logout" v-else @click="logout">Выйти</div>
        </div>
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Header",
    methods: {
        main() {
            this.$router.push('/')
        },
        logout() {
            localStorage.removeItem('token')
            localStorage.removeItem('user_id')

            this.main()
        }
    },
    data() {
        return {
            token: false,
            user_id: 0
        }
    },
    mounted() {
        this.token = localStorage.token
        this.user_id = localStorage.user_id
    },

    watch: {
        $route() {
            if (localStorage.user_id && localStorage.token) {
                this.token = localStorage.token
                this.user_id = localStorage.user_id
            }
        }
    }
}
</script>

<style lang="sass" scoped>
.header
    width: 1250px
    height: 185px
    display: flex

    &_logo
        &-logo
            width: 185px
            height: 185px

            &:hover
                cursor: pointer

    &_nav
        display: flex
        justify-content: space-between
        align-items: center
        width: 700px
        margin: 100px auto 170px

        &-elem
            color: $white
            +medium
            font-size: 24px
            text-decoration: none
            border-bottom: 2px solid transparent
            text-transform: uppercase
            -webkit-transition: 0.2s
            -moz-transition: 0.2s
            -ms-transition: 0.2s
            -o-transition: 0.2s
            transition: 0.2s

            &:hover
                border-bottom: 2px solid $gray

    &_side
        display: flex
        justify-content: flex-start
        align-items: center
        flex-direction: column

        &-login
            width: 80px
            height: 20px
            text-align: center
            +medium
            color: $white
            font-size: 16px
            margin: 20px auto 7px auto
            text-decoration: none

            &:hover
                cursor: pointer

        &-logout
            width: 80px
            height: 12px
            text-align: right
            +medium
            color: $gray
            font-size: 14px
            text-decoration: none

            &:hover
                cursor: pointer

        &-download
            width: 80px
            height: 30px
            padding: 0 3px
            background-color: $white
            border-radius: 10px
            color: $black
            font-size: 10px
            display: flex
            justify-content: center
            align-items: center
            flex-direction: column
            +medium
            -webkit-transition: 0.2s
            -moz-transition: 0.2s
            -ms-transition: 0.2s
            -o-transition: 0.2s
            transition: 0.2s

            & span
                color: $orange

            &:hover
                cursor: pointer
                color: $white
                background-color: $gray


</style>