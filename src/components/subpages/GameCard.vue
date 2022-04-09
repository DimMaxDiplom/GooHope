<template>
  <div class="card">
    <div class="card_block">
      <div class="card_block-image">
        <img src="" alt="">
      </div>
    </div>
    <div class="card_block">
      <div class="card_block-title">{{ title }}</div>
      <div class="card_block_info">
        <span>{{ total_hours }} часов</span>
        <span>{{ week_hours }} часов за эту неделю</span>
      </div>
    </div>
    <div class="card_block">
      <div class="achievements">
        <div class="achievements-achievement" v-for="elem in achievements.slice(0, 6)" :key="elem.id"></div>
      </div>
      <div class="btn">Запустить</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GameCard",
  props: {
    title: String,
    total_hours: Number,
    week_hours: Number,
    achievements: Array
  }
}
</script>

<style lang="sass" scoped>
.card
  display: flex
  justify-content: flex-start
  align-items: flex-start
  width: 840px
  background-color: $trs_gray
  margin-bottom: 25px
  padding: 8px 40px 8px 15px
  &_block
    display: flex
    flex-direction: column
    &-image
      background-color: $white
      width: 100px
      height: 110px
      margin: 10px 10px 10px 0
    &-title
      margin-top: 10px
      color: $white
      font-size: 18px
      +medium
    &_info
      display: flex
      flex-direction: column
      justify-content: flex-start
      align-items: flex-start
      margin-top: 39px
      & span
        color: $white
        +medium
        font-size: 18px
        &:first-child
          margin-bottom: 5px
    & .achievements
      display: flex
      justify-content: flex-end
      align-items: center
      width: 353px
      background-color: $gray
      padding: 4px 10px
      margin-left: 86px
      margin-bottom: 41px
      &-achievement
        width: 43px
        height: 43px
        border: 1px solid $orange
        border-radius: 2px
        margin-left: 15px
        &:first-child
          margin-left: 0
    & .btn
      align-self: flex-end
      width: 170px
      height: 40px
      border: 1px solid $green
      color: $white
      display: flex
      justify-content: center
      align-items: center
      font-size: 18px
      +medium
      &:hover
        cursor: pointer
</style>