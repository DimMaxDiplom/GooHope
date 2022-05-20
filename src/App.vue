<template>
  <div class="mainWrapper">
    <Header/>
    <router-view></router-view>
    <Footer/>
  </div>
</template>

<script>
import Footer from "@/components/subpages/Footer";
import Header from "@/components/subpages/Header";

export default {
  name: 'App',
  components: {
    Footer, Header
  }
}
</script>

<style lang="sass">
.mainWrapper
  display: flex
  justify-content: flex-start
  flex-direction: column
  align-items: center
  min-height: 100vh
  background-color: $black

*
  padding: 0
  margin: 0
  box-sizing: border-box
</style>
