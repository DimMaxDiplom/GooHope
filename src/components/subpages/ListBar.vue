<template>
    <div class="bar">
        <div class="bar-image"></div>
        <div class="bar_info">
            <div class="bar_info-title">{{ tile.login }}</div>
            <div class="bar_info-content" :class="tile.status ? 'green' : 'red'">{{
                    tile.status ? 'Online' : 'Последний раз в сети: 5ч 37мин назад'
                }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "ListBar",
    props: {
        tile: {
            title: String,
            content: String,
            color: String
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