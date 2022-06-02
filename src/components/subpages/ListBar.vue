<template>
    <div class="bar">
        <div class="bar-image"></div>
        <div class="bar_info">
            <div class="bar_info-title">{{ title }}</div>
            <div class="bar_info-content" :class="color ? 'green' : 'red'">
                {{ content ? content : 'Последний раз в сети: 5ч 37мин назад' }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ListBar",
    data() {
        return {
            title: '',
            content: '',
            color: ''
        }
    },
    props: {
        tile: {
            type: Object,
            default: null
        },
        group: {
            type: Object,
            default: null
        }
    },
    mounted() {
        if (this.tile !== null) {
            this.title = this.tile.login
            this.content = this.tile.status
            if (this.tile.status === true) {
                this.content = 'Online'
                this.color = 'green'
            }
        } else if (this.group !== null) {
            this.title = this.group.title
            this.content = ' '
        }
    }
}
</script>

<style lang="sass" scoped>
.bar
    display: flex
    justify-content: flex-start
    align-items: flex-start
    margin-bottom: 10px
    transition: 0.3s

    &:hover
        cursor: pointer
        transform: scale(1.1)

    &-image
        width: 62px
        height: 62px
        background-color: $gray
        margin-right: 5px

    &_info
        display: flex
        flex-direction: column

        &-title
            color: $white
            font-size: 18px
            +medium

        &-content
            margin-top: 5px
            font-size: 10px
            margin-left: 1px
            +light
            color: $white

            &.red
                color: $red

            &.green
                color: $green
</style>