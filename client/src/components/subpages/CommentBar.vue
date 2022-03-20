<template>
  <div class="comment">
    <div class="comment_main">
      <div class="comment-image"></div>
      <div class="comment_info">
        <div class="comment_info-title">{{ comment.sender }}</div>
        <div class="comment_info_date">
          <div class="comment_info_date-date">{{ comment.created_date }}</div>
          <div class="comment_info_date-time">{{ comment.created_time }}</div>
        </div>
        <div class="comment_info-signature">{{ comment.signature }}</div>
      </div>
    </div>
    <div class="comment_content">{{ comment.content }}</div>
  </div>
</template>

<script>
export default {
  name: "CommentBar",
  props: {
    comment: {
      sender: String,
      created_date: String,
      created_time: String,
      signature: String,
      content: String
    }
  }
}
</script>

<style lang="sass" scoped>
.comment
  display: flex
  justify-content: space-between
  align-items: center
  width: 1220px
  height: 120px
  border-radius: 5px
  background-color: $gray
  margin-bottom: 15px
  padding: 15px
  &_main
    display: flex
    justify-content: flex-start
  &-image
    background-color: $black
    width: 90px
    height: 90px
    margin-right: 5px
  &_info
    display: flex
    flex-direction: column
    justify-content: flex-start
    align-items: flex-start
    &-title
      color: $black
      font-size: 18px
      +medium
    &_date
      color: $white
      +thin
      font-size: 12px
      display: flex
      justify-content: space-between
      align-items: center
      width: 100px
      &-date
      &-time
    &-signature
      color: $green
      +light
      font-size: 14px
      margin-top: 35px
  &_content
    justify-self: flex-end
    border-radius: 15px
    background-color: $black
    width: 895px
    height: 100px
    padding: 6px
    color: $white
    font-size: 14px
    +light
</style>