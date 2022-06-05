<template>
    <div class="about">
        <div class="about_hero">
            <div class="about_hero_logo">
                <div class="about_hero_logo_logo">
                    <img src="@/assets/logo.png" alt="" class="about_hero_logo_logo-img">
                </div>
                <div class="about_hero_logo-title">
                    GooHope - Игровая платформа для игроков и разработчиков.
                </div>
            </div>
            <div class="about_hero_status">
                <div class="about_hero_status-btn">Загрузить GooHope</div>
                <div class="about_hero_status_stat">
                    <div class="about_hero_status_stat-online">В сети: 2</div>
                    <div class="about_hero_status_stat-playing">В игре: 1</div>
                </div>
            </div>
        </div>
        <div class="about_skipped">
            GooHope предлагает более 0 игр на любой вкус. Автоматическое обновление игр и приложений, скачивание в фоновом режиме и многое другое
        </div>
        <div class="about_info">
            <div class="about_info_top">
                <div class="about_info_top_info">
                    <div class="about_info_top_info-title">Выпускай свои игры</div>
                    <div class="about_info_top_info-subtitle">
                        PlaceWork - инструмент, позволяющий разработчику разместить свою игру на платформе и активно её распространять
                    </div>
                </div>
                <div class="about_info_top_img">
                    <img src="" alt="" class="about_info_top_img-img">
                </div>
            </div>
            <div class="about_info_bottom">
                <div class="about_info_bottom_img">
                    <img src="" alt="" class="about_info_bottom_img-img">
                </div>
                <div class="about_info_bottom_info">
                    <div class="about_info_bottom_info-title">Вступай в сообщества и ищи друзей</div>
                    <div class="about_info_bottom_info-subtitle">
                        Заводите знакомства, вступайте в группы, общайтесь и не только! Один возможный друг не даст вам соскучиться.
                    </div>
                </div>
            </div>
        </div>
        <div class="about_possibilities">
            <div class="about_possibilities_title">Возможности на GooHope</div>
            <div class="about_possibilities_subtitle">
                Наша платформа постоянно развивается и улучшается. На текущий момент у нас уже немало возможностей, а именно:
            </div>
            <div class="about_possibilities_cards">
                <div class="about_possibilities_cards-card"></div>
                <div class="about_possibilities_cards-card"></div>
                <div class="about_possibilities_cards-card"></div>
                <div class="about_possibilities_cards-card"></div>
                <div class="about_possibilities_cards-card"></div>
                <div class="about_possibilities_cards-card"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "AboutPage"
}
</script>

<style scoped lang="sass">
.about
    display: flex
    justify-content: center
    flex-direction: column
    align-items: center
    width: 1250px

    &_hero
        width: 800px
        height: 432px

        &_logo
            display: flex
            justify-content: flex-start
            align-items: flex-end

            &_logo
                &-img
                    width: 275px
                    height: 275px

            &-title
                color: $orange
                +medium
                text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
                text-align: left
                font-size: 24px
                margin-bottom: 10px
                margin-left: 40px

        &_status
            display: flex
            justify-content: center
            align-items: flex-end

            &-btn
                color: $orange
                border: 1px solid $orange
                padding: 10px
                width: 380px
                height: 70px
                border-radius: 10px
                display: flex
                justify-content: center
                align-items: center
                font-size: 24px
                +medium
                margin-top: 85px
                transition: 0.4s

                &:hover
                    background-color: $orange
                    color: $black
                    cursor: pointer
                    border: 1px solid $black


            &_stat
                margin-left: 90px
                margin-bottom: 45px

                &-online
                    text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
                    color: $blue
                    font-size: 24px
                    +medium
                    margin-bottom: 12px

                &-playing
                    text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
                    color: $green
                    font-size: 24px
                    +medium

    &_skipped
        margin-top: 188px
        text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
        color: $white
        text-align: center
        font-size: 48px
        +medium
        width: 878px
        margin-bottom: 80px

    &_info
        display: flex
        flex-direction: column
        justify-content: space-between
        align-items: flex-start
        width: 100%

        &_top
            position: relative
            display: flex
            justify-content: space-between
            align-items: flex-start
            width: 100%

            &_info
                box-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
                border-radius: 25px
                background-color: $trs_gray
                width: 605px
                height: 321px
                padding: 15px
                display: flex
                flex-direction: column
                justify-content: flex-start
                align-items: center

                &-title
                    color: $orange
                    border-bottom: 3px solid $orange
                    width: 274px
                    text-align: center
                    padding-bottom: 5px
                    text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
                    font-size: 24px
                    +medium
                    position: relative

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

                &-subtitle
                    margin-top: 18px
                    text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.5)
                    color: $white
                    text-align: center
                    font-size: 36px
                    +medium

            &_img
                width: 525px
                height: 525px
                background-color: $gray

                &-img

        &_bottom
            position: relative
            display: flex
            justify-content: space-between
            align-items: flex-end
            width: 100%
            transform: translateY(-80px)

            &_info
                box-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
                border-radius: 25px
                background-color: $trs_gray
                width: 605px
                height: 321px
                padding: 15px
                display: flex
                flex-direction: column
                justify-content: flex-start
                align-items: center

                &-title
                    color: $orange
                    border-bottom: 3px solid $orange
                    width: 467px
                    text-align: center
                    padding-bottom: 5px
                    text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
                    font-size: 24px
                    +medium
                    position: relative

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

                &-subtitle
                    margin-top: 18px
                    text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.5)
                    color: $white
                    text-align: center
                    font-size: 36px
                    +medium

            &_img
                width: 525px
                height: 525px
                background-color: $gray

                &-img

    &_possibilities
        width: 100%
        display: flex
        flex-direction: column
        justify-content: center
        align-items: center

        &_title
            width: 1250px
            text-align: center
            color: $orange
            padding-bottom: 15px
            border-bottom: 3px solid $orange
            position: relative
            text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.25)
            font-size: 48px
            +medium
            margin-bottom: 43px

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

        &_subtitle
            width: 1090px
            height: 180px
            border-radius: 20px
            box-shadow: 4px 4px 2px rgba(0, 0, 0, 0.25)
            background-color: $trs_gray
            text-shadow: 4px 2px 2px rgba(0, 0, 0, 0.5)
            color: $white
            +medium
            font-size: 36px
            display: flex
            justify-content: center
            align-items: center
            text-align: center

        &_cards
            width: 1010px
            display: flex
            justify-content: space-between
            align-items: flex-start
            flex-wrap: wrap
            margin-top: 65px

            &-card
                background-color: $gray
                width: 210px
                height: 260px
                margin-bottom: 100px
                margin-left: 90px
                &:nth-child(4n)
                    margin-left: 0
                &:first-child
                    margin-left: 0
</style>