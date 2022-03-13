<template>
  <div class="input">
    <div class="input-title">{{ label }}</div>
    <input :type="type" :placeholder="placeholder">
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Input",
  props: {
    label: String,
    placeholder: String,
    type: String
  }
}
</script>

<style lang="sass" scoped>
.input
  display: flex
  flex-direction: column
  justify-content: center
  align-items: flex-start
  margin-bottom: 30px
  &-title
    color: $black
    +medium
    font-size: 18px
    text-transform: uppercase
    margin-bottom: 15px
  & input
    width: 630px
    height: 90px
    background-color: transparent
    border: 2px solid $trs_gray
    padding-left: 40px
    font-size: 18px
    +medium
    outline: none
    color: $black
    &::placeholder
      text-transform: uppercase
      color: $trs_gray
    &:focus
      border: 2px solid $gray
</style>