<template>
    <div class="input" :id="field">
        <div class="input-title">{{ label }}</div>
        <div class="input-error"></div>
        <input v-model="data" :type="type" :placeholder="placeholder" @input="deactivate">
    </div>
</template>

<script>
export default {
    // eslint-disable-next-line vue/multi-word-component-names
    name: "Input",
    data() {
        return {
            data: ''
        }
    },
    props: {
        label: String,
        placeholder: String,
        type: String,
        field: String,
        content: String
    },
    mounted() {
        this.data = this.content
    },
    watch: {
        data() {
            this.$emit('updateInput', this.field, this.data)
        }
    },
    methods: {
        deactivate() {
            let root = document.getElementById(this.field)
            let error_label = root.querySelector('.input-error')
            let error_input = root.querySelector('input')

            error_label.textContent = ''
            error_input.classList.remove('error')
        }
    }
}
</script>

<style lang="sass" scoped>
.input
    display: flex
    flex-direction: column
    justify-content: center
    align-items: flex-start
    margin-bottom: 30px

    &-title
        color: $black
        +medium
        font-size: 18px
        text-transform: uppercase

    &-error
        color: $red
        +medium
        font-size: 12px
        text-transform: uppercase
        margin-bottom: 5px
        height: 12px

    & input
        width: 630px
        height: 70px
        background-color: transparent
        border: 2px solid $trs_gray
        padding-left: 40px
        font-size: 18px
        +medium
        outline: none
        color: $black

        &::placeholder
            text-transform: uppercase
            color: $trs_gray

        &:focus
            border: 2px solid $gray

        &.error
            border: 2px solid $red
</style>