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
            <div class="hero_card_invite_btns-signin">Войти</div>
            <div class="hero_card_invite_btns-signup">Зарегистрироваться</div>
          </div>
          <div class="hero_card_invite_adds">Хотите узнать больше?<router-link to="/" class="hero_card_invite_adds-link">сюда</router-link></div>
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
              <div class="hero_card_main_games_game-name">Counter-Strike:Gl...</div>
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
            <input type="search" class="hero_card_search_block-search">
            <div class="hero_card_search_block-search">Найти людей</div>
          </div>
          <div class="hero_card_search_block">
            <input type="search" class="hero_card_search_block-search">
            <div class="hero_card_search_block-search">Найти продукт</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainPage"
}
</script>

<style lang="sass" scoped>
.main
  padding-top: 290px
  width: 1250px
</style>