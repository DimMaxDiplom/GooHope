<template>
  <div class="content">
    {{ content }}
  </div>
</template>

<script>
export default {
  name: "ContentLine",
  props: {
    content: String
  }
}
</script>

<style lang="sass" scoped>
.content
  color: $white
  font-size: 18px
  +light
  width: 165px
  padding-bottom: 5px
  border-bottom: 4px solid $orange
  text-align: center
</style>