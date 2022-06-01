<template>
    <div class="edit">
        <div class="edit-title">Редактирование профиля</div>
        <div id="error"></div>
        <div class="edit_fields">
            <Input label="email" placeholder="Введите ваш Email адрес" type="email" @updateInput="onUpdateInput"
                   field="email"
            />
            <Input label="Старый пароль" placeholder="Введите ваш Пароль" type="password" @updateInput="onUpdateInput"
                   field="old_password"
            />
            <Input label="Новый пароль" placeholder="Введите ваш Пароль" type="password" @updateInput="onUpdateInput"
                   field="new_password"
            />
        </div>
        <div class="edit_btns">
            <div class="edit_btns-btn-1" @click="$router.back()">
                <vue-feather type="chevrons-left" class="edit_btns-btn-1-icon" size="24"/>
                Назад
            </div>
            <div class="edit_btns-btn-2" @click="update_password">
                Изменить пароль
                <vue-feather type="chevrons-right" class="edit_btns-btn-2-icon" size="24"/>
            </div>
        </div>
    </div>
</template>

<script>
import Input from "@/components/subpages/Input";
import axios from "axios";

export default {
    name: "ProfileEditPage",
    components: {Input},
    data() {
        return {
            user: {
                email: '',
                old_password: '',
                new_password: '',
            },
            errors: {
                'wrong_credentials': ['Неправильные почта или пароль'],
                'required': ['Вы забыли заполнить это поле']
            },
        }
    },
    methods: {
        onUpdateInput(field, data) {
            this.user[field] = data
        },
        update_password() {
            if (this.user.email && this.user.old_password && this.user.new_password) {
                axios.post('http://127.0.0.1:8080/change_password', {
                    email: this.user.email,
                    old_password: this.user.old_password,
                    new_password: this.user.new_password
                })
                    .then(res => {
                        localStorage.token = res.data.token
                        this.$router.push(`/profile/${localStorage.user_id}`)
                    })
                    .catch(err => {
                        console.log(err)
                        let res = err.response.data.error
                        document.getElementById('error').textContent = this.errors[res]
                        document.querySelectorAll('input').forEach(elem => elem.classList.add('error'))
                    })
            } else {
                if (!this.user.email) {
                    this.error(document.getElementById('email'), this.errors['required'])
                } if (!this.user.old_password) {
                    this.error(document.getElementById('old_password'), this.errors['required'])
                } if (!this.user.new_password) {
                    this.error(document.getElementById('new_password'), this.errors['required'])
                }
            }
        },
        error(root, message) {
            let error_label = root.querySelector('.input-error')
            let error_input = root.querySelector('input')

            error_label.textContent = message
            error_input.classList.add('error')
        },
    },
}
</script>

<style lang="sass" scoped>
.edit
    background-color: $white
    width: 815px
    height: 615px
    padding: 35px 80px

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
    &_btns
        display: flex
        justify-content: space-between
        align-items: center
        width: 630px
        &-btn
            &-1, &-2
                width: 350px
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

            &-1
                width: 210px
                &-icon
                    padding-right: 25px
                    padding-left: 0

</style>