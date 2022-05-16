<template>
    <div class="card">
        <div class="card_img"></div>
        <div class="card_content">
            <div class="card_content_title">
                <div class="card_content_title-title">{{ login }}</div>
                <div class="card_content_title-subtitle">
                    {{ status }}
                </div>
            </div>
            <div class="card_content-text">
                {{ content }}
            </div>
        </div>
        <div class="card_info">
            <div class="card_info_left">
                <span>Получено:</span>
                <span>Прочитано:</span>
            </div>
            <div class="card_info_right">
                <span>{{ get }}</span>
                <span>{{ read }}</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "DialogCard",
    props: {
        login: String,
        status: String,
        content: String,
        get: String,
        read: String
    }
}
</script>

<style lang="sass" scoped>
.card
    width: 819px
    height: 146px
    background: $gray
    border-radius: 10px
    display: flex
    justify-content: flex-start
    align-items: flex-start
    margin-bottom: 15px

    &_img
        margin: 28px 10px
        background-color: $white
        height: 90px
        width: 90px

    &_content
        display: flex
        flex-direction: column
        justify-content: flex-start
        align-items: flex-start

        &_title
            display: flex
            flex-direction: column
            justify-content: flex-start
            align-items: flex-start
            margin-top: 15px

            &-title
                color: $white
                +light
                font-size: 14px

            &-subtitle
                color: $black
                +light
                font-size: 8px
                margin-bottom: 5px
        &-text
            width: 600px
            height: 85px
            border: 3px solid $black
            border-radius: 5px
            font-size: 12px
            +light
            color: $white
            padding: 5px 6px
            margin-bottom: 20px

    &_info
        display: flex
        justify-content: center
        align-items: flex-end
        font-size: 8px
        align-self: flex-end
        margin-bottom: 15px
        margin-left: 5px
        +thin
        &_left
            display: flex
            flex-direction: column
            & span
                color: $white

        &_right
            display: flex
            flex-direction: column
            margin-left: 3px
            & span
                color: $orange
                &:last-child
                    color: $green
</style>