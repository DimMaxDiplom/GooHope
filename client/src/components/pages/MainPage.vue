<template>
  <div class="main">
    <div class="hero">
      <div class="hero_title">
        <h2 class="hero_title-title">Новости сообщества</h2>
      </div>
      <div class="hero_card">
        <div class="hero_card_invite">
          <div class="hero_card_invite_title">
            <div class="hero_card_invite_title-title">Добро пожаловать в GooHope</div>
            <div class="hero_card_invite_title-title">Войдите в свой профиль для удобства</div>
          </div>
          <div class="hero_card_invite_btns">
            <router-link to="/login" class="hero_card_invite_btns-signin">Войти</router-link>
            <router-link to="/sign_up" class="hero_card_invite_btns-signup">Зарегистрироваться</router-link>
          </div>
          <div class="hero_card_invite_adds">Хотите узнать больше? Вам
            <router-link to="/" class="hero_card_invite_adds-link">сюда</router-link>
          </div>
        </div>
        <div class="hero_card_main">
          <div class="hero_card_main-title">Популярные центры сообщества</div>
          <div class="hero_card_main_games">
            <div class="hero_card_main_games_game">
              <img src="" alt="" class="hero_card_main_games_game_image">
              <div class="hero_card_main_games_game-name">Dota 2</div>
              <div class="hero_card_main_games_game_info">
                <div class="hero_card_main_games_game_info-elem">5234 записей</div>
                <div class="hero_card_main_games_game_info-elem">524 иллюстрации</div>
                <div class="hero_card_main_games_game_info-elem">52 видеозаписи</div>
              </div>
            </div>
            <div class="hero_card_main_games_game">
              <img src="" alt="" class="hero_card_main_games_game_image">
              <div class="hero_card_main_games_game-name">Counter-Strike: Gl...</div>
              <div class="hero_card_main_games_game_info">
                <div class="hero_card_main_games_game_info-elem">5234 записей</div>
                <div class="hero_card_main_games_game_info-elem">524 иллюстрации</div>
                <div class="hero_card_main_games_game_info-elem">52 видеозаписи</div>
              </div>
            </div>
          </div>
        </div>
        <div class="hero_card_search">
          <div class="hero_card_search_block">
            <input type="text">
            <vue-feather type="search" class="hero_card_search_block-search-icon" size="15"></vue-feather>
            <div class="hero_card_search_block-search">Найти людей</div>
          </div>
          <div class="hero_card_search_block">
            <input type="text">
            <vue-feather type="search" class="hero_card_search_block-search-icon" size="15"></vue-feather>
            <div class="hero_card_search_block-search">Найти продукт</div>
          </div>
        </div>
      </div>
    </div>
    <div class="recs">
      <h2 class="recs-title">Рекомендации</h2>
      <div class="recs_catgs">
        <div class="recs_catgs-catg active">Все</div>
        <div class="recs_catgs-catg">Иллюстрации</div>
        <div class="recs_catgs-catg">Видео</div>
        <div class="recs_catgs-catg">Новости</div>
        <div class="recs_catgs-catg">Обзоры</div>
        <div class="recs_catgs-catg">Стримы</div>
      </div>
      <div class="ills">
        <div class="ills_line" v-for="item in ills" :key="item.id">
          <ContentCard :content_image_path="item[0].content_image_path"
                       :author="item[0].author"
                       :title="item[0].title"
                       :game_title="item[0].game_title"
                       :commends="item[0].commends"/>
          <ContentCard :content_image_path="item[1].content_image_path"
                       :author="item[1].author"
                       :title="item[1].title"
                       :game_title="item[1].game_title"
                       :commends="item[1].commends"/>
        </div>
      </div>
      <div class="video">
        <div class="video_line" v-for="item in video" :key="item.id">
          <ContentCard :content_image_path="item[0].content_video_path"
                       :author="item[0].author"
                       :title="item[0].title"
                       :game_title="item[0].game_title"
                       :commends="item[0].commends"/>
          <ContentCard :content_image_path="item[1].content_video_path"
                       :author="item[1].author"
                       :title="item[1].title"
                       :game_title="item[1].game_title"
                       :commends="item[1].commends"/>
        </div>
      </div>
      <div class="mainNews">
        <NewsCard v-for="item in news" :key="item.id"
                  :content="item.content" :content_image_path="item.content_image_path"
                  :author="item.author" :title="item.title" :commends="item.commends"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ContentCard from "@/components/subpages/ContentCard";
import NewsCard from "@/components/subpages/NewsCard";

export default {
  name: "MainPage",
  components: {NewsCard, ContentCard},
  data() {
    return {
      ills: [
        [
          {
            content_image_path: '',
            author: 'ReF0iL 1',
            title: 'ReF0iL title 1',
            game_title: 'Game Title 1',
            commends: 1015
          },
          {
            content_image_path: '',
            author: 'ReF0iL 2',
            title: 'ReF0iL title 2',
            game_title: 'Game Title 2',
            commends: 125
          }
        ],
        [
          {
            content_image_path: '',
            author: 'ReF0iL 3',
            title: 'ReF0iL title 3',
            game_title: 'Game Title 3',
            commends: 1
          },
          {
            content_image_path: '',
            author: 'ReF0iL 4',
            title: 'ReF0iL title 4',
            game_title: 'Game Title 4',
            commends: 25
          }]
      ],
      video: [
        [
          {
            content_video_path: '',
            author: 'ReF0iL 1',
            title: 'ReF0iL title 1',
            game_title: 'Game Title 1',
            commends: 1015
          },
          {
            content_video_path: '',
            author: 'ReF0iL 2',
            title: 'ReF0iL title 2',
            game_title: 'Game Title 2',
            commends: 125
          }
        ],
        [
          {
            content_video_path: '',
            author: 'ReF0iL 3',
            title: 'ReF0iL title 3',
            game_title: 'Game Title 3',
            commends: 1
          },
          {
            content_video_path: '',
            author: 'ReF0iL 4',
            title: 'ReF0iL title 4',
            game_title: 'Game Title 4',
            commends: 25
          }]
      ],
      news: [
        {
          content_image_path: '',
          author: 'ReF0iL 1',
          title: 'ReF0iL title 1',
          commends: 1015,
          content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus lacus nibh, ac lacinia diam euismod quis. Etiam ultrices ipsum ac augue condimentum, vel molestie lorem consectetur. Praesent sodales diam tellus, non tincidunt ipsum vestibulum eget. Nam ut mauris dui. Sed gravida ultrices lacus faucibus tincidunt. Quisque vel risus lorem. Ut at sodales est."
        }, {
          content_image_path: '',
          author: 'ReF0iL 1',
          title: 'ReF0iL title 1',
          commends: 1015,
          content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus lacus nibh, ac lacinia diam euismod quis. Etiam ultrices ipsum ac augue condimentum, vel molestie lorem consectetur. Praesent sodales diam tellus, non tincidunt ipsum vestibulum eget. Nam ut mauris dui. Sed gravida ultrices lacus faucibus tincidunt. Quisque vel risus lorem. Ut at sodales est."
        }, {
          content_image_path: '',
          author: 'ReF0iL 1',
          title: 'ReF0iL title 1',
          commends: 1015,
          content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus lacus nibh, ac lacinia diam euismod quis. Etiam ultrices ipsum ac augue condimentum, vel molestie lorem consectetur. Praesent sodales diam tellus, non tincidunt ipsum vestibulum eget. Nam ut mauris dui. Sed gravida ultrices lacus faucibus tincidunt. Quisque vel risus lorem. Ut at sodales est."
        }, {
          content_image_path: '',
          author: 'ReF0iL 1',
          title: 'ReF0iL title 1',
          commends: 1015,
          content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus lacus nibh, ac lacinia diam euismod quis. Etiam ultrices ipsum ac augue condimentum, vel molestie lorem consectetur. Praesent sodales diam tellus, non tincidunt ipsum vestibulum eget. Nam ut mauris dui. Sed gravida ultrices lacus faucibus tincidunt. Quisque vel risus lorem. Ut at sodales est."
        },
      ]
    }
  }
}
</script>

<style lang="sass" scoped>
.main
  padding-top: 100px
  width: 1250px

  & .hero
    &_title
      width: 225px
      height: 55px
      position: relative

      &-title
        color: $orange
        font-size: 18px
        +semi-bold
        width: 224px
        padding: 22px 0
        border-bottom: 4px solid $orange

        &::after
          content: ''
          display: block
          position: absolute
          right: -19px
          bottom: -27px
          width: 20px
          height: 20px
          background-color: $orange
          -webkit-transform: rotate(-45deg)
          -moz-transform: rotate(-45deg)
          -ms-transform: rotate(-45deg)
          -o-transform: rotate(-45deg)
          transform: rotate(-45deg)
          -webkit-transform-origin: 0 100%
          -moz-transform-origin: 0 100%
          -ms-transform-origin: 0 100%
          -o-transform-origin: 0 100%
          transform-origin: 0 100%

    &_card
      width: 100%
      display: flex
      justify-content: flex-start
      align-items: flex-start
      border-radius: 5px
      background-color: $gray
      height: 234px
      margin-top: 45px

      &_main
        display: flex
        flex-direction: column
        justify-content: center
        align-items: center
        margin-right: 80px

        &-title
          color: $white
          font-size: 24px
          +medium
          padding: 12px 2px 8px 0
          border-bottom: 2px solid $orange

        &_games
          align-self: flex-start
          display: flex
          flex-direction: column
          justify-content: center
          align-items: flex-start
          position: relative

          &::before
            content: ''
            display: block
            height: 131px
            width: 2px
            background-color: $white
            position: absolute
            // image size + name size + margin
            left: calc(50px + 231px + 15px)
            top: 25px

          &_game
            display: flex
            justify-content: flex-start
            align-items: center

            &:nth-child(1)
              padding: 25px 0

            &_image
              background-color: $white
              width: 50px
              height: 50px

            &-name
              margin: auto 7px
              +medium
              font-size: 24px
              color: $white
              width: 231px

            &_info
              display: flex
              flex-direction: column
              align-items: flex-start
              justify-content: center
              margin-left: 10px

              &-elem
                color: $white
                +medium
                font-size: 14px

      &_invite
        margin: 15px 70px auto 15px
        display: flex
        justify-content: center
        align-items: flex-start
        flex-direction: column

        &_title
          &-title
            +light
            color: $white
            font-size: 18px

            &:nth-child(2)
              margin: 25px auto 30px auto

        &_btns
          display: flex
          justify-content: space-between
          align-items: center
          width: 100%

          &-signin
            background-color: $black
            border-radius: 10px
            color: $white
            font-size: 16px
            padding: 8px 23px
            text-align: center
            text-decoration: none
            +medium
            position: relative
            -webkit-transition: 0.4s
            -moz-transition: 0.4s
            -ms-transition: 0.4s
            -o-transition: 0.4s
            transition: 0.4s

            &:hover
              -webkit-transform: scale(1.1)
              -moz-transform: scale(1.1)
              -ms-transform: scale(1.1)
              -o-transform: scale(1.1)
              transform: scale(1.1)

            &::after
              content: ''
              display: block
              position: absolute
              right: -65px
              top: 50%
              width: 65px
              height: 4px
              background-color: $orange

          &-signup
            background-color: $black
            border-radius: 10px
            color: $white
            font-size: 16px
            padding: 8px 10px
            text-align: center
            text-decoration: none
            +medium
            z-index: 10
            -webkit-transition: 0.4s
            -moz-transition: 0.4s
            -ms-transition: 0.4s
            -o-transition: 0.4s
            transition: 0.4s

            &:hover
              -webkit-transform: scale(1.1)
              -moz-transform: scale(1.1)
              -ms-transform: scale(1.1)
              -o-transform: scale(1.1)
              transform: scale(1.1)

        &_adds
          padding-top: 20px
          color: $white
          font-size: 16px
          +thin

          &-link
            +medium
            color: $orange
            text-decoration: underline

      &_search
        margin-top: 40px

        &_block
          position: relative

          & input
            background-color: $white
            border-radius: 10px
            border: none
            outline: none
            width: 210px
            height: 35px
            padding-left: 15px
            +medium
            font-size: 16px
            color: $black
            margin-bottom: 3px

          &-search
            color: $white
            margin-bottom: 30px
            +light
            font-size: 12px

            &-icon
              color: $gray
              position: absolute
              right: 5px
              bottom: 28px

              &:hover
                cursor: pointer

  & .recs
    display: flex
    flex-direction: column
    align-items: flex-start
    justify-content: flex-start

    &-title
      color: $white
      margin-top: 100px
      padding-bottom: 10px
      +bold
      border-bottom: 4px solid $orange
      width: 100%

    &_catgs
      display: flex
      justify-content: flex-start
      align-items: flex-start
      margin-bottom: 30px

      &-catg
        color: $white
        +bold
        font-size: 24px
        padding: 5px 35px
        border-radius: 0 0 10px 10px
        -webkit-transition: 0.2s
        -moz-transition: 0.2s
        -ms-transition: 0.2s
        -o-transition: 0.2s
        transition: 0.2s

        &:hover
          background-color: $trs_gray
          cursor: pointer

        &.active
          background-color: $gray

  & .ills
    display: flex
    flex-direction: column
    width: 100%
    background-color: $gray
    padding: 15px
    &_line
      display: flex
      justify-content: space-between
      align-items: flex-start
      width: 100%
      &:nth-child(1)
        padding-bottom: 25px
        margin-bottom: 25px
        border-bottom: 4px solid $orange
  & .video
    display: flex
    flex-direction: column
    width: 100%
    background-color: $gray
    padding: 15px
    margin-top: 50px
    &_line
      display: flex
      justify-content: space-between
      align-items: flex-start
      width: 100%
      &:nth-child(1)
        padding-bottom: 25px
        margin-bottom: 25px
        border-bottom: 4px solid $orange
  & .mainNews
    display: flex
    flex-direction: column
    width: 100%
    background-color: $gray
    padding: 15px
    margin-top: 50px


</style>