<template>
    <div class="sign_up">
        <div class="sign_up_left">
            <div class="sign_up_left_title">
                <div class="sign_up_left-title">Регистрация</div>
                <div class="sign_up_left-step">Шаг {{ step }}</div>
            </div>
            <div class="sign_up_left_fields" v-if="step === 1"> <!-- Первый шаг -->
                <Input label="Ваш Email" placeholder="Введите ваш email" type="email" @updateInput="on_update_input"
                       field="email"
                />
                <Input label="Пароль" placeholder="Введите ваш Пароль" type="password" @updateInput="on_update_input"
                       field="password"
                />
                <Input label="Пароль повторно" placeholder="Введите ваш Пароль повтороно" type="password"
                       @updateInput="on_update_input"
                       field="repeat_password"
                />
            </div> <!-- Первый шаг -->
            <div class="sign_up_left_fields" v-if="step === 2"> <!-- Второй шаг -->
                <Input label="Ваше имя" placeholder="Введите ваше имя" type="text" @updateInput="on_update_input"
                       field="name"
                />
                <Input label="Логин" placeholder="Введите ваш логин" type="text" @updateInput="on_update_input"
                       field="login"
                />
                <Input label="Ваша страна" placeholder="Введите название вашей страны" type="text"
                       @updateInput="on_update_input"
                       field="country"
                />
            </div> <!-- Второй шаг -->
            <div class="sign_up_left_fields" v-if="step === 3"> <!-- Третий шаг -->
                <Input label="код" placeholder="Введите код, который пришёл к вам на почту" type="text"
                       @updateInput="on_update_input"
                       field="code"
                />
                <span>Выслать повторно можно будет через: {{ time }}</span>
                <div class="check_code locked">Проверить код</div>
            </div> <!-- Третий шаг -->
            <div class="sign_up_left_btns">
                <div class="sign_up_left_btn" @click="next_step">
                    Перейти к шагу №{{ step + 1 }}
                    <vue-feather type="chevrons-right" class="sign_up_left_btn-icon" size="24"/>
                </div>
                <div class="sign_up_left_btn_back" v-if="step > 1" @click="prev_step">
                    Вернуться на шаг №{{ step - 1 }}
                    <vue-feather type="chevrons-right" class="sign_up_left_btn_back-icon" size="24"/>
                </div>
            </div>
        </div>
        <div class="sign_up_right">
            <div class="sign_up_right-title">Уже создали аккаунт?</div>
            <div class="sign_up_right_body">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus lacus nibh, ac lacinia diam
                euismod
                quis. Etiam ultrices ipsum ac augue condimentum, vel molestie lorem consectetur
            </div>
            <div class="sign_up_right_btn" @click="$router.push('/sign_in')">
                Войти в аккаунт
                <vue-feather type="chevrons-right" class="sign_up_right_btn-icon" size="24"/>
            </div>
        </div>
    </div>
</template>

<script>
import Input from "@/components/subpages/Input";
import axios from "axios";

export default {
    name: "SignUp",
    components: {Input},
    data() {
        return {
            step: 1,
            user: {
                login: String,
                password: String,
                repeat_password: String,
                name: String,
                email: String,
                country: String,
                code: ''
            },
            time: '1.00'
        }
    },
    methods: {
        on_update_input(field, data) {
            this.user[field] = data
            if (field === 'code') {
                let elem = document.querySelector('.check_code')
                if (this.user.code !== '')
                    elem.classList.remove('locked')
                else
                    elem.classList.add('locked')
            }
        },
        next_step() {
            // TODO: Check passwords and other errors
            console.log(this.step)
            if (this.step === 1) {
                axios.post('http://127.0.0.1:8080/register', {
                    email: this.user.email,
                    password: this.user.password
                })
                    .then(res => {
                        console.log(res)
                    })
                    .catch(err => {
                        console.log(err)
                    })
            }
            if (this.step <= 2) {
                this.step += 1
                if (this.step === 3)
                    document.querySelector('.sign_up_left_btn').innerText = 'Зарегистрироваться'
            }
        },
        prev_step() {
            this.step--
        }
    },
}
</script>

<style lang="sass" scoped>
.sign_up
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
        display: flex
        flex-direction: column
        justify-content: space-between

        &_title
            display: flex
            justify-content: space-between
            align-items: flex-end
            margin-bottom: 30px

        &-title
            color: $black
            text-transform: uppercase
            font-size: 24px
            +bold

        &-step
            color: $black
            text-transform: uppercase
            font-size: 24px
            +bold
            border-bottom: 2px solid $black
            margin-right: 295px
            width: 125px
            text-align: center

        &_fields
            & span
                color: $black
                text-transform: uppercase
                font-size: 18px
                +medium
                transform: translateY(-60px)
                display: block

            & #code
                margin-bottom: 5px
                transform: translateY(-60px)

            & .check_code
                width: 200px
                height: 50px
                padding: 14px
                text-align: center
                font-size: 18px
                text-transform: uppercase
                margin-top: 35px
                transform: translateY(-60px)
                +medium
                color: $gray
                border: 2px solid $gray
                -webkit-transition: 0.2s
                -moz-transition: 0.2s
                -ms-transition: 0.2s
                -o-transition: 0.2s
                transition: 0.2s

                &:hover
                    cursor: pointer
                    background-color: $gray
                    color: $white

                &.locked
                    background-color: $gray
                    color: $black

                    &:hover
                        cursor: auto

        &_btns
            display: flex
            justify-content: space-between
            align-items: flex-end
            padding-right: 25px

        &_btn
            width: 315px
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
                padding: 21px
                color: $orange

            &_back
                width: 230px
                height: 50px
                border: 2px solid $black
                padding-left: 10px
                display: flex
                justify-content: flex-start
                align-items: center
                color: $black
                text-transform: uppercase
                font-size: 14px
                -webkit-transition: 0.2s
                -moz-transition: 0.2s
                -ms-transition: 0.2s
                -o-transition: 0.2s
                transition: 0.2s
                +medium

                &:hover
                    cursor: pointer
                    background-color: $black
                    color: $white

                    & .sign_up_left_btn_back-icon
                        color: $white

                &-icon
                    padding: 5px
                    color: $black
                    -webkit-transition: 0.3s
                    -moz-transition: 0.3s
                    -ms-transition: 0.3s
                    -o-transition: 0.3s
                    transition: 0.3s

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