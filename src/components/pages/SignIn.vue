<template>
    <div class="login">
        <div class="login_left">
            <div class="login_left-title">Авторизация</div>
            <div id="error"></div>
            <div class="login_left_fields">
                <Input label="email" placeholder="Введите ваш Email адрес" type="email" @updateInput="onUpdateInput"
                       field="email"
                />
                <Input label="Пароль" placeholder="Введите ваш Пароль" type="password" @updateInput="onUpdateInput"
                       field="password"
                />
            </div>
            <div class="login_left_btn" @click="try_login">
                Войти
                <vue-feather type="chevrons-right" class="login_left_btn-icon" size="24"/>
            </div>
        </div>
        <div class="login_right">
            <div class="login_right-title">Ещё не создали аккаунт?</div>
            <div class="login_right_body">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus lacus nibh, ac lacinia diam
                euismod
                quis. Etiam ultrices ipsum ac augue condimentum, vel molestie lorem consectetur
            </div>
            <div class="login_right_btn" @click="$router.push('/sign_up')">
                Создать аккаунт
                <vue-feather type="chevrons-right" class="login_right_btn-icon" size="24"/>
            </div>
        </div>
    </div>
</template>

<script>
import Input from "@/components/subpages/Input";
import axios from "axios";

export default {
    name: "SignIn",
    components: {Input},
    data() {
        return {
            user: {
                email: String,
                password: String
            },
            errors: {
                'wrong_credentials': ['Неправильные почта или пароль']
            },
        }
    },
    methods: {
        onUpdateInput(field, data) {
            this.user[field] = data
        },
        try_login() {
            axios.post('http://127.0.0.1:8080/login', {
                email: this.user.email,
                password: this.user.password
            })
                .then(res => {
                    console.log(res)
                    if (res.status === 200) {
                        localStorage.setItem('user_id', res.data.user_id)
                        localStorage.setItem('token', res.data.token)

                        this.$router.push(`/profile/${res.data.user_id}`)
                    }
                })
                .catch(err => {
                    console.log(err)
                    let res = err.response.data.error
                    document.getElementById('error').textContent = this.errors[res]
                    document.querySelectorAll('input').forEach(elem => elem.classList.add('error'))
                })
        },
    },
}
</script>

<style lang="sass" scoped>
.login
    display: flex
    justify-content: space-between
    align-items: flex-start
    padding-top: 70px
    width: 1250px

    &_left
        background-color: $white
        width: 815px
        height: 615px
        padding: 55px 80px

        & #error
            color: $red
            +medium
            font-size: 12px
            text-transform: uppercase
            height: 12px
            margin-bottom: 28px

        &-title
            margin-bottom: 10px
            color: $black
            text-transform: uppercase
            font-size: 24px
            +bold

        &_fields
            margin-bottom: 92px

        &_btn
            width: 210px
            height: 70px
            background-color: $gray
            display: flex
            justify-content: flex-start
            align-items: center
            padding-left: 40px
            color: $white
            text-transform: uppercase
            -webkit-transition: 0.2s
            -moz-transition: 0.2s
            -ms-transition: 0.2s
            -o-transition: 0.2s
            transition: 0.2s
            font-size: 18px
            +medium

            &:hover
                cursor: pointer
                -webkit-transform: scale(1.1)
                -moz-transform: scale(1.1)
                -ms-transform: scale(1.1)
                -o-transform: scale(1.1)
                transform: scale(1.1)

            &-icon
                padding-left: 55px
                color: $orange

    &_right
        background-color: $gray
        width: 435px
        height: 615px
        display: flex
        flex-direction: column
        justify-content: space-between

        &-title
            +medium
            font-size: 36px
            color: $white
            margin-top: 80px
            width: 100%
            text-align: center
            text-transform: uppercase

        &_body
            color: $white
            margin: 60px auto 115px
            +medium
            width: 345px
            text-align: center
            text-transform: uppercase

        &_btn
            width: 275px
            height: 70px
            border: 2px solid $white
            margin-left: 40px
            padding-left: 10px
            display: flex
            justify-content: flex-start
            align-items: center
            color: $white
            text-transform: uppercase
            font-size: 18px
            margin-bottom: 35px
            -webkit-transition: 0.2s
            -moz-transition: 0.2s
            -ms-transition: 0.2s
            -o-transition: 0.2s
            transition: 0.2s
            +medium

            &:hover
                cursor: pointer
                -webkit-transform: scale(1.1)
                -moz-transform: scale(1.1)
                -ms-transform: scale(1.1)
                -o-transform: scale(1.1)
                transform: scale(1.1)

            &-icon
                padding-left: 50px
                color: $white
</style>