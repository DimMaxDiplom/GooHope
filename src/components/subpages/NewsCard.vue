<template>
    <div class="news">
        <div class="news_image">
            <img :src="media + content_image_path" alt="">
        </div>
        <div class="news_content">
            <div class="news_content_main">
                <div class="news_content_main_header">
                    <div class="news_content_main_header-title">{{ author }}</div>
                    <div class="news_content_main_header-title">{{ title }}</div>
                </div>
                <div class="news_content_main_body">
                    {{ content.substring(0, 500) }}
                </div>
            </div>
            <div class="news_content_info">
                <div class="likes">
                    <div class="news_content_info_likes">
                        <div class="disslike">
                            <vue-feather type="minus" size="24" class="disslike-icon"/>
                        </div>
                        <div class="like">
                            <vue-feather type="plus" size="24" class="like-icon"/>
                        </div>
                    </div>
                    <div class="news_content_info-likes">
                        {{ commends }}
                        <vue-feather type="heart" size="10" class="icon" fill="#FFA801"/>
                    </div>
                </div>
                <div class="news_content_info_comments">
                    Перейти к обсуждению
                    <vue-feather type="message-square" size="12" class="news_content_info_comments-icon"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "NewsCard",
    props: {
        content_image_path: String,
        author: String,
        title: String,
        commends: Number,
        content: String
    },
    data() {
        return {
            media: 'http://127.0.0.1:8000'
        }
    },
}
</script>

<style lang="sass" scoped>
.news
    display: flex
    justify-content: flex-start
    align-items: center
    margin-bottom: 30px

    &_image
        width: 128px
        height: 128px
        background-color: $black
        display: flex
        justify-content: center
        align-items: center

        & img
            width: 124px
            height: 124px

    &_content
        display: flex
        justify-content: flex-start
        align-items: flex-end
        margin-left: 5px
        width: 875px

        &_main
            display: flex
            flex-direction: column
            align-items: flex-start

            &_header
                display: flex
                justify-content: space-between
                align-items: center
                margin-bottom: 5px
                width: 100%

                &-title
                    color: $white
                    +light
                    font-size: 18px
                    border-bottom: 4px solid $orange
                    text-align: center
                    width: 180px

                    &:nth-child(2)
                        width: 485px
                        margin-right: 100px

            &_body
                height: 95px
                width: 880px
                background-color: $black
                border-radius: 5px
                color: $white
                padding: 5px
                +light
                font-size: 14px

        &_info
            display: flex
            flex-direction: column
            justify-content: space-between
            align-items: flex-start
            margin-left: 5px

            & .likes
                display: flex
                justify-content: space-between
                align-items: center
                width: 80%

            &_likes
                display: flex
                justify-content: flex-start
                align-items: flex-start

                & .disslike
                    position: relative
                    margin-right: 5px

                    &-icon
                        color: $black
                        -webkit-transition: 0.2s
                        -moz-transition: 0.2s
                        -ms-transition: 0.2s
                        -o-transition: 0.2s
                        transition: 0.2s

                        &:hover
                            color: $orange

                        &.active
                            color: $orange

                & .like
                    margin-left: 5px

                    &-icon
                        color: $black
                        -webkit-transition: 0.2s
                        -moz-transition: 0.2s
                        -ms-transition: 0.2s
                        -o-transition: 0.2s
                        transition: 0.2s

                        &:hover
                            color: $pink

                        &.active
                            color: $pink

            &-likes
                color: $orange
                +medium
                font-size: 18px
                display: flex
                justify-content: space-between
                align-items: center

                & .icon
                    padding-left: 5px

            &_comments
                color: $white
                text-decoration: underline
                font-size: 14px
                +light
                width: 200px

</style>