<template>
  <div class="profile">
    <div class="profile_main">
      <div class="profile_main_left">
        <div class="profile_main_left_profile">
          <div class="profile_main_left_profile-image">
            <img src="" alt="">
          </div>
          <div class="profile_main_left_profile_info">
            <div class="profile_main_left_profile_info_header">
              <div class="profile_main_left_profile_info_header-title">ReF0iL</div>
              <div class="profile_main_left_profile_info_header-status">Online</div>
            </div>
            <div class="profile_main_left_profile_info_desc">
              <span>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam placerat ornare nulla quis venenatis. Pellentesque habitant morbi tristique senectus et netus et ma... </span>
              <div class="profile_main_left_profile_info_desc-btn">Развернуть</div>
            </div>
            <div class="profile_main_left_profile_info_game">
              <div class="profile_main_left_profile_info_game-title">Название любимой игры</div>
              <div class="profile_main_left_profile_info_game_info">
                <div class="profile_main_left_profile_info_game_info-image"></div>
                <div class="profile_main_left_profile_info_game_info_desc">
                  <span>1000 часов</span>
                  <span>1000 часов за эту неделю</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="profile_main_left_games">
          <GameCard v-for="game in games" :key="game.id"
                    :title="game.title" :total_hours="game.total_hours"
                    :week_hours="game.week_hours" :achievements="game.achievements"
          />
          <div class="profile_main_left_games-all">Показать всё</div>
        </div>
      </div>
      <div class="profile_main_right">
        <div class="profile_main_right-edit">Редактировать профиль</div>
        <div class="profile_main_right_ach">
          <div class="profile_main_right_ach-elem" v-for="elem in achs.slice(0, 4)" :key="elem.id"></div>
        </div>
        <div class="profile_main_right_friends">
          <div class="profile_main_right_friends_title">
            <div class="profile_main_right_friends_title-title">Список друзей</div>
            <div class="profile_main_right_friends_title-num">({{ friends_count }})</div>
          </div>
          <div class="profile_main_right_friends_list">
            <ListBar v-for="friend in friends" :key="friend.id" :tile="friend" />
          </div>
        </div>
        <div class="profile_main_right_groups">
          <div class="profile_main_right_groups_title">
            <div class="profile_main_right_groups_title-title">Список групп</div>
            <div class="profile_main_right_groups_title-num">({{ groups_count }})</div>
          </div>
          <div class="profile_main_right_groups_list">
            <ListBar v-for="group in groups" :key="group.id" :tile="group" />
          </div>
        </div>
      </div>
    </div>
    <div class="profile_comments">
      <div class="profile_comments_title">
        <div class="profile_comments_title-title">Комментарии</div>
      </div>
      <div class="profile_comments_list">
        <CommentBar v-for="comment in comments" :key="comment.id" :comment="comment"/>
      </div>
    </div>
  </div>
</template>

<script>

import GameCard from "@/components/subpages/GameCard";
import ListBar from "@/components/subpages/ListBar";
import CommentBar from "@/components/subpages/CommentBar";

export default {
  name: "ProfilePage",
  components: {GameCard, ListBar, CommentBar},
  data() {
    return {
      games: [
        {
          title: 'Dota 2',
          total_hours: '100',
          week_hours: '120',
          achievements: [1, 2, 3]
        },
        {
          title: 'Dota 2',
          total_hours: '100',
          week_hours: '120',
          achievements: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
        {
          title: 'Dota 2',
          total_hours: '100',
          week_hours: '120',
          achievements: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
        {
          title: 'Dota 2',
          total_hours: '100',
          week_hours: '120',
          achievements: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
        {
          title: 'Dota 2',
          total_hours: '100',
          week_hours: '120',
          achievements: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        },
      ],
      achs: [1, 2, 3, 4, 5, 6, 7, 8, 9],
      friends_count: 69,
      friends: [
        {title: 'ReF0iL-1', content: 'Последний раз в сети: 5ч 37мин назад', color: 'red'},
        {title: 'ReF0iL-2', content: 'Online', color: 'green'},
        {title: 'ReF0iL-3', content: 'Последний раз в сети: 5ч 37мин назад', color: 'red'},
        {title: 'ReF0iL-4', content: 'Последний раз в сети: 5ч 37мин назад', color: 'red'},
        {title: 'ReF0iL-5', content: 'Последний раз в сети: 5ч 37мин назад', color: 'red'},
      ],
      groups_count: 19,
      groups: [
        {title: 'Group-1', content: 'Участников: 1261'},
        {title: 'Group-2', content: 'Участников: 126'},
        {title: 'Group-3', content: 'Участников: 11'},
        {title: 'Group-4', content: 'Участников: 1'},
        {title: 'Group-5', content: 'Участников: 21261'},
      ],
      comments: [
        {sender: 'ReF0iL-1', created_date: '24.02.2022', created_time: '18:36', signature: 'С Уважением, Дмитрий', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar placerat placerat. Aliquam faucibus arcu dolor, at condimentum tortor posuere in. Curabitur tristique augue eu nisl aliquam tincidunt. Nam vehicula vulputate eleifend. Suspendisse dictum a leo a vestibulum. Suspendisse consequat purus in sapien accumsan sagittis. Sed quis est sed libero fermentum maximus. Donec sed tincidunt tellus.'},
        {sender: 'ReF0iL-2', created_date: '25.02.2022', created_time: '18:37', signature: 'С Уважением, Дмитрий', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar placerat placerat. Aliquam faucibus arcu dolor, at condimentum tortor posuere in. Curabitur tristique augue eu nisl aliquam tincidunt. Nam vehicula vulputate eleifend. Suspendisse dictum a leo a vestibulum. Suspendisse consequat purus in sapien accumsan sagittis. Sed quis est sed libero fermentum maximus. Donec sed tincidunt tellus.'},
        {sender: 'ReF0iL-3', created_date: '26.02.2022', created_time: '18:38', signature: 'С Уважением, Дмитрий', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar placerat placerat. Aliquam faucibus arcu dolor, at condimentum tortor posuere in. Curabitur tristique augue eu nisl aliquam tincidunt. Nam vehicula vulputate eleifend. Suspendisse dictum a leo a vestibulum. Suspendisse consequat purus in sapien accumsan sagittis. Sed quis est sed libero fermentum maximus. Donec sed tincidunt tellus.'},
        {sender: 'ReF0iL-4', created_date: '27.02.2022', created_time: '18:39', signature: 'С Уважением, Дмитрий', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar placerat placerat. Aliquam faucibus arcu dolor, at condimentum tortor posuere in. Curabitur tristique augue eu nisl aliquam tincidunt. Nam vehicula vulputate eleifend. Suspendisse dictum a leo a vestibulum. Suspendisse consequat purus in sapien accumsan sagittis. Sed quis est sed libero fermentum maximus. Donec sed tincidunt tellus.'},
        {sender: 'ReF0iL-5', created_date: '28.02.2022', created_time: '18:40', signature: 'С Уважением, Дмитрий', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar placerat placerat. Aliquam faucibus arcu dolor, at condimentum tortor posuere in. Curabitur tristique augue eu nisl aliquam tincidunt. Nam vehicula vulputate eleifend. Suspendisse dictum a leo a vestibulum. Suspendisse consequat purus in sapien accumsan sagittis. Sed quis est sed libero fermentum maximus. Donec sed tincidunt tellus.'},
      ]
    }
  },

}
</script>

<style lang="sass" scoped>
.profile
  &_main
    display: flex
    justify-content: center
    align-items: flex-start

    &_left
      display: flex
      flex-direction: column
      justify-content: flex-start
      align-items: flex-start

      &_profile
        display: flex
        justify-content: flex-start
        align-items: flex-start
        padding-bottom: 52px
        border-bottom: 3px solid $green

        &-image
          width: 380px
          height: 380px
          background-color: $gray
          margin-right: 40px

        &_info
          &_header
            display: flex
            justify-content: flex-start
            align-items: flex-end
            margin-bottom: 16px

            &-title
              color: $white
              font-size: 24px
              +medium
              border-bottom: 3px solid $orange
              width: 280px
              text-align: center
              position: relative
              padding-bottom: 10px

              &::after, &::before
                content: ''
                display: block
                position: absolute
                right: -19px
                bottom: -10px
                width: 12px
                height: 12px
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

              &::before
                left: -6px

            &-status
              color: $green
              font-size: 16px
              +medium
              margin-left: 90px

          &_desc
            width: 425px
            height: 85px
            background-color: $gray
            padding: 10px 10px 5px
            border-radius: 10px

            & span
              color: $white
              font-size: 14px
              +medium

            &-btn
              color: $green
              font-size: 10px
              +medium
              text-align: right
              margin-top: 5px

          &_game
            display: flex
            flex-direction: column
            align-items: flex-start
            justify-content: flex-start
            margin-top: 32px

            &-title
              color: $white
              font-size: 14px
              +medium
              width: 280px
              position: relative
              border-bottom: 3px solid $orange
              text-align: center
              padding-bottom: 5px
              margin-bottom: 25px

              &::after, &::before
                content: ''
                display: block
                position: absolute
                right: -19px
                bottom: -10px
                width: 12px
                height: 12px
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

              &::before
                left: -6px

            &_info
              display: flex
              justify-content: flex-start
              align-items: flex-start

              &-image
                background-color: $gray
                width: 105px
                height: 105px
                margin-right: 8px

              &_desc
                display: flex
                flex-direction: column
                justify-content: flex-start
                align-items: flex-start

                & span
                  color: $white
                  font-size: 14px
                  +medium
                  margin-bottom: 5px
      &_games
        display: flex
        flex-direction: column
        margin-top: 30px
        padding-bottom: 40px
        border-bottom: 3px solid $green
        &-all
          color: $white
          +medium
          text-decoration: underline
          font-size: 18px
          align-self: flex-end
          &:hover
            cursor: pointer
    &_right
      width: 330px
      margin-left: 75px
      display: flex
      flex-direction: column
      align-items: flex-end
      justify-content: flex-start
      &-edit
        width: 280px
        height: 40px
        font-size: 16px
        +medium
        color: $white
        text-transform: uppercase
        display: flex
        justify-content: center
        align-items: center
        border: 2px solid $gray
        border-radius: 10px
        align-self: center
        -webkit-transition: 0.2s
        -moz-transition: 0.2s
        -ms-transition: 0.2s
        -o-transition: 0.2s
        transition: 0.2s
        margin-left: 15px
        &:hover
          cursor: pointer
          background-color: $gray
      &_ach
        display: flex
        justify-content: flex-start
        align-items: center
        border-radius: 10px
        border: 2px solid $orange
        padding: 7px 18px
        margin: 27px 0 37px
        &-elem
          width: 61px
          height: 61px
          border-radius: 15px
          border: 1px solid $green
          margin-right: 8px
          &:last-child
            margin-right: 0
      &_friends
        display: flex
        flex-direction: column
        justify-content: flex-end
        align-items: center
        &_title
          display: flex
          color: $white
          font-size: 18px
          width: 280px
          +medium
          position: relative
          padding-bottom: 10px
          border-bottom: 3px solid $orange
          margin: 0 15px 15px
          &::after, &::before
            content: ''
            display: block
            position: absolute
            right: -19px
            bottom: -10px
            width: 12px
            height: 12px
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
          &::before
            left: -6px
          &-title
            margin-left: 70px
            margin-right: 25px
          &-num
        &_list
          display: flex
          flex-direction: column
          justify-content: flex-start
          align-items: flex-start
          width: 330px
          background-color: $trs_gray
          border-radius: 10px
          padding: 15px 0 5px 20px
      &_groups
        display: flex
        flex-direction: column
        justify-content: flex-end
        align-items: center
        margin-top: 100px
        &_title
          display: flex
          color: $white
          font-size: 18px
          width: 280px
          +medium
          position: relative
          padding-bottom: 10px
          border-bottom: 3px solid $orange
          margin: 0 15px 15px
          &::after, &::before
            content: ''
            display: block
            position: absolute
            right: -19px
            bottom: -10px
            width: 12px
            height: 12px
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
          &::before
            left: -6px
          &-title
            margin-left: 70px
            margin-right: 25px
          &-num
        &_list
          display: flex
          flex-direction: column
          justify-content: flex-start
          align-items: flex-start
          width: 330px
          background-color: $trs_gray
          border-radius: 10px
          padding: 15px 0 5px 20px
.profile
  &_comments
    width: 1250px
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
    &_list
      background-color: $trs_gray
      margin-top: 70px
      display: flex
      flex-direction: column
      justify-content: flex-start
      align-items: flex-start
      border-radius: 10px
      padding: 15px 15px 0
      margin-bottom: 15px
</style>