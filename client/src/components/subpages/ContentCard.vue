<template>
  <div class="card">
    <div class="card_image">
      <img src="" alt="">
    </div>
    <div class="card_info">
      <ContentLine class="card_info-content" :content="author"/>
      <ContentLine class="card_info-content" :content="title"/>
      <ContentLine class="card_info-content" :content="game_title"/>
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

  props: {
    content_image_path: String,
    author: String,
    title: String,
    game_title: String,
    commends: Number
  }
}
</script>

<style lang="sass" scoped>
.card
  display: flex
  justify-content: flex-start
  align-items: flex-start

  &_image
    width: 315px
    height: 315px
    background-color: $black
    border: none
    outline: none
    margin-right: 5px

    & img
      width: 50px
      height: 50px

  &_info
    &-content
      margin-bottom: 20px
    &_comments
      margin-top: 130px
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
</style>