<template>
    <div class="sign_up">
        <div class="sign_up_left">
            <div class="sign_up_left_title">
                <div class="sign_up_left-title">Регистрация</div>
                <div class="sign_up_left-step">Шаг {{ step }}</div>
            </div>
            <div class="sign_up_left_fields" v-if="step === 1"> <!-- Первый шаг -->
                <Input label="Ваш Email" placeholder="Введите ваш email" type="email" @updateInput="on_update_input"
                       field="email" :content="user.email"
                />
                <Input label="Пароль" placeholder="Введите ваш Пароль" type="password" @updateInput="on_update_input"
                       field="password" :content="user.password"
                />
                <Input label="Пароль повторно" placeholder="Введите ваш Пароль повтороно" type="password" @updateInput="on_update_input"
                       field="repeat_password" :content="user.repeat_password"
                />
            </div> <!-- Первый шаг -->
            <div class="sign_up_left_fields" v-if="step === 2"> <!-- Второй шаг -->
                <Input label="Ваше имя" placeholder="Введите ваше имя" type="text" @updateInput="on_update_input"
                       field="name" :content="user.name"
                />
                <Input label="Логин" placeholder="Введите ваш логин" type="text" @updateInput="on_update_input"
                       field="login" :content="user.login"
                />
                <Dropdown :options="types" :selected="user.type" v-on:updateOption="update_user_type" :placeholder="user.type.name"/>
            </div> <!-- Второй шаг -->
            <div class="sign_up_left_fields" v-if="step === 3"> <!-- Третий шаг -->
                <Input label="код" placeholder="Введите код, который пришёл к вам на почту" type="text"
                       @updateInput="on_update_input"
                       field="code" :content="user.code"
                />
                <div class="check_code locked" @click="check_code">Проверить код</div>
            </div> <!-- Третий шаг -->
            <div class="sign_up_left_btns">
                <div class="sign_up_left_btn" @click="next_step" v-if="step < 3">
                    Перейти к шагу №{{ step + 1 }}
                    <vue-feather type="chevrons-right" class="sign_up_left_btn-icon" size="24"/>
                </div>
                <div class="sign_up_left_btn locked" @click="next_step" v-else>
                    Зарегистрироваться
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
import Dropdown from "@/components/subpages/Dropdown";
import axios from "axios";

export default {
    name: "SignUp",
    components: {Input, Dropdown},
    data() {
        return {
            step: 1,
            token: '',
            user: {
                user_id: Number,
                login: '',
                password: '',
                repeat_password: '',
                name: '',
                email: '',
                type: {name: 'Пожалуйста, выбери тип профиля', value: 'ALL'},
                code: ''
            },
            types: [
                {name: 'Открытый', value: 'ALL'},
                {name: 'Только для друзей', value: 'FaF'},
                {name: 'Друзья и друзья друзей', value: 'JF'},
                {name: 'Приватный', value: 'OO'}
            ],
            errors: {
                'too_short': ['Слишком короткий пароль'],
                'email_in_use': ['Пользователь с такой почтой уже существует'],
                'not_repeated': ['Пароли не совпадают'], // Local error
                'incorrect_email': ['Проверьте правильность почты'],
                'required': ['Вы забыли заполнить это поле'], // Local error
                'wrong_verification_code': ['Неправильный код'],
            }
        }
    },
    methods: {
        update_user_type(payload) {
            this.user.type = payload
        },
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
            if (this.step === 1) {
                if (this.user.password === this.user.repeat_password) {
                    axios.post('http://127.0.0.1:8080/register', {
                        email: this.user.email,
                        password: this.user.password
                    })
                        .then(res => {
                            if (res.status === 200) {
                                this.step += 1
                            }
                        })
                        .catch(err => {
                            let res = err.response.data
                            if (err.response.status === 400) {
                                if (res.error === 'email_in_use') {
                                    this.error(document.getElementById('email'), this.errors['email_in_use'])
                                } else {
                                    if (res.details) {
                                        if (res.details.email) {
                                            this.error(document.getElementById('email'), this.errors[res.details.email])
                                        }
                                        if (res.details.password) {
                                            this.error(document.getElementById('password'), this.errors[res.details.password])
                                        }
                                    }
                                }
                            }
                        })
                } else {
                    ['password', 'repeat_password'].forEach(elem => this.error(document.getElementById(elem), this.errors['not_repeated']))
                }
            } else if (this.step === 2) {
                if (!this.user.login || !this.user.name) {
                    if (!this.user.login) {
                        this.error(document.getElementById('login'), this.errors['required'])
                    }
                    if (!this.user.name) {
                        this.error(document.getElementById('name'), this.errors['required'])
                    }
                } else {
                    this.step += 1
                }
            } else if (this.step === 3) {
                let elem = document.querySelector('.sign_up_left_btn')
                if (!elem.classList.contains('locked')) {
                    axios.post('http://127.0.0.1:8000/api/profile', {
                        user_id: Number(this.user.user_id),
                        login: this.user.login,
                        publicity: this.user.type.value,
                        name: this.user.name
                    })
                        .then(res => {
                            if (res.status === 201) {
                                localStorage.setItem('token', this.token)
                                localStorage.setItem('user_id', this.user.user_id)

                                this.$router.push(`/profile/${this.user.user_id}`)
                            }
                        })
                        .catch(err => {
                            console.log(err.response)
                        })
                }
            }
        },
        error(root, message) {
            let error_label = root.querySelector('.input-error')
            let error_input = root.querySelector('input')

            error_label.textContent = message
            error_input.classList.add('error')
        },
        prev_step() {
            if (this.step === 3) {
                document.querySelector('.sign_up_left_btn').classList.remove('locked')
            }
            this.step--
        },
        check_code(event) {
            let {target} = event
            let elem = document.querySelector('.sign_up_left_btn')
            // Кнопка проверки кода не залокана и кнопка следующего шага - залокана
            if (!target.classList.contains('locked') && elem.classList.contains('locked')) {
                axios.post('http://127.0.0.1:8080/verify_email', {
                    email: this.user.email,
                    code: this.user.code
                })
                    .then(res => {
                        if (res.status === 200) {
                            elem.classList.remove('locked')

                            this.user.user_id = res.data.user_id
                            this.token = res.data.token
                        }
                    })
                    .catch(err => {
                        let res = err.response.data
                        if (err.response.status === 400) {
                            this.error(document.getElementById('email'), this.errors[res.error])
                        }
                    })
            }
        },
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

            &.locked
                background-color: $gray
                color: $black

                &:hover
                    cursor: auto
                    -webkit-transform: scale(1.0)
                    -moz-transform: scale(1.0)
                    -ms-transform: scale(1.0)
                    -o-transform: scale(1.0)
                    transform: scale(1.0)

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