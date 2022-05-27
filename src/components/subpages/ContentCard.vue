<template>
    <div class="card">
        <div class="card_image">
            <img v-if="type !== 'video'" :src="media + content_image_path" alt="">
            <canvas id="canvas" v-else/>
        </div>
        <div class="card_info">
            <ContentLine v-if="author" class="card_info-content" :content="author"/>
            <ContentLine v-if="title" class="card_info-content" :content="title"/>
            <ContentLine v-if="game_title" class="card_info-content" :content="game_title"/>
            <ContentLine v-if="date" class="card_info-content" :content="date"/>
            <div class="card_info_comments">
                Перейти к обсуждению
                <vue-feather type="message-square" size="12" class="card_info_comments-icon"/>
            </div>
            <div class="card_info_stat">
                <div class="card_info_stat_likes">
                    <div class="disslike">
                        <vue-feather type="minus" size="24" class="disslike-icon"/>
                    </div>
                    <div class="like">
                        <vue-feather type="plus" size="24" class="like-icon"/>
                    </div>
                </div>
                <div class="card_info_stat-likes">
                    {{ commends }}
                    <vue-feather type="heart" size="10" class="icon" fill="#FFA801"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ContentLine from "@/components/subpages/ContentLine"

export default {
    name: "ContentCard",
    components: {ContentLine},
    data() {
        return {
            media: 'http://127.0.0.1:8000'
        }
    },
    props: {
        content_image_path: String,
        author: String,
        title: String,
        game_title: String,
        commends: Number,
        date: String,
        type: String,
    },
    mounted() {
        const elems = [this.author, this.title, this.game_title, this.date].filter(elem => elem)
        document.querySelectorAll(`.${this.type} .card_info_comments`).forEach(elem => elem.style.marginTop = `${280 - elems.length * 50}px`)

        // Unused code. Was designed to take a frame from a video
        // if (this.type === 'video') {
        //     let secs = 5
        //     let video = document.createElement('video')
        //     video.onloadedmetadata = () => {
        //         if ('function' === typeof secs) {
        //             secs = secs(this.duration)
        //         }
        //         this.currentTime = Math.min(Math.max(0, (secs < 0 ? this.duration : 0) + secs), this.duration)
        //     }
        //     video.onseeked = e => {
        //         let canvas = document.createElement('canvas')
        //         canvas.height = video.videoHeight
        //         canvas.width = video.videoWidth
        //         let ctx = canvas.getContext('2d')
        //         ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
        //         let img = new Image()
        //         img.src = canvas.toDataURL()
        //         console.log(e)
        //     }
        //     video.onerror = e => {
        //         console.error(e)
        //     }
        //     video.src = this.media + this.content_image_path
        // }
    }
}
</script>

<style lang="sass" scoped>
.card
    display: flex
    justify-content: flex-start
    align-items: flex-start

    &_image
        width: 316px
        height: 316px
        background-color: $black
        border: none
        outline: none
        margin-right: 5px
        display: flex
        justify-content: center
        align-items: center

        & img
            width: 310px
            height: 310px

    &_info
        &-content
            margin-bottom: 20px

        &_comments
            margin-bottom: 10px
            color: $white
            text-decoration: underline
            font-size: 14px
            +light

            &-icon

        &_stat
            display: flex
            justify-content: space-between
            align-items: flex-start

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
                            cursor: pointer

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
                            cursor: pointer

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
</style>