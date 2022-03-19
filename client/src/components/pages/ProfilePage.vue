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
      </div>
      <div class="profile_main_right"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfilePage"
}
</script>

<style lang="sass" scoped>
.profile
  &_main
    display: flex
    justify-content: center
    align-items: center
    &_left
      display: flex
      flex-direction: column
      justify-content: flex-start
      align-items: flex-start
      padding-bottom: 52px
      border-bottom: 3px solid $green
      &_profile
        display: flex
        justify-content: flex-start
        align-items: flex-start
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
    &_right
      width: 330px
      margin-left: 70px
</style>