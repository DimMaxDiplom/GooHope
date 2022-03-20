<template>
  <div class="bar">
    <div class="bar-image"></div>
    <div class="bar_info">
      <div class="bar_info-title">{{ friend.title }}</div>
      <div class="bar_info-content" :class="friend.color">{{ friend.content }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ListBar",
  props: {
    friend: {
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