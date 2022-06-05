<template>
    <div class="list">
        <div class="list_title">
            <div class="list_title-title">Возможные жанры</div>
        </div>
        <div class="list_filter">
            <div class="list_filter-cat active">Все</div>
            <div class="list_filter-cat">Экшн</div>
            <div class="list_filter-cat">Приключения</div>
            <div class="list_filter-cat">Ролевые игры</div>
            <div class="list_filter-cat">Симуляторы</div>
            <div class="list_filter-cat">Стратегии</div>
            <div class="list_filter-cat">Спорт и гонки</div>
        </div>
        <div class="list_cards">
            <div class="list_cards_card" v-for="game in games" :key="game.id">
                <div class="list_cards_card_img">
                    <img src="" alt="" class="list_cards_card_img-img">
                </div>
                <div class="list_cards_card_content">
                    <div class="list_cards_card_content_title">
                        <div class="list_cards_card_content_title-title">{{ game.title }}</div>
                        <div class="list_cards_card_content_title-cost">{{ game.cost }} $</div>
                    </div>
                    <div class="list_cards_card_content_tags">
                        <div class="list_cards_card_content_tags-tag" v-for="tag in game.tags" :key="tag.id">{{ tag.name }}</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "GameListPage",
    data() {
        return {
            games: [
                {
                    title: 'Dota 2',
                    cost: 250,
                    tags: [
                        {
                            name: 'Data',
                        },
                        {
                            name: 'Best',
                        },
                    ]
                },
                {
                    title: 'CS:GO',
                    cost: 1000,
                    tags: [
                        {
                            name: 'Smth',
                        },
                        {
                            name: 'Best',
                        },
                    ]
                },
                {
                    title: 'Counter Strike: Source',
                    cost: 1000,
                    tags: [
                        {
                            name: 'Smth',
                        },
                        {
                            name: 'Best',
                        },
                    ]
                },
                {
                    title: 'Minecraft',
                    cost: 1000,
                    tags: [
                        {
                            name: 'Smth',
                        },
                        {
                            name: 'Best',
                        },
                    ]
                },
                {
                    title: 'Terraria',
                    cost: 1000,
                    tags: [
                        {
                            name: 'Smth',
                        },
                        {
                            name: 'Best',
                        },
                    ]
                },
                {
                    title: 'Fortnite',
                    cost: 1000,
                    tags: [
                        {
                            name: 'Smth',
                        },
                        {
                            name: 'Best',
                        },
                    ]
                },
            ]
        }
    }
}
</script>

<style scoped lang="sass">
.list
    width: 1250px
    display: flex
    flex-direction: column
    justify-content: flex-start
    align-items: flex-start

    &_title
        margin-top: 60px
        width: 100%
        &-title
            color: $white
            padding-bottom: 10px
            +bold
            border-bottom: 4px solid $orange
            font-size: 22px


    &_filter
        display: flex
        justify-content: flex-start
        align-items: flex-start
        margin-bottom: 30px

        &-cat
            color: $white
            +bold
            font-size: 16px
            padding: 5px 15px
            border-radius: 0 0 10px 10px
            transition: 0.2s

            &:hover
                background-color: $trs_gray
                cursor: pointer
            &.active
                background-color: $trs_gray

    &_cards
        display: flex
        justify-content: space-between
        align-items: center
        flex-wrap: wrap
        margin: 25px 0
        width: 100%

        &_card
            display: flex
            justify-content: flex-start
            align-items: flex-start
            background-color: $trs_gray
            width: 49%
            border-radius: 10px
            padding: 10px
            margin-bottom: 15px
            transition: 0.2s

            &:hover
                cursor: pointer
                transform: scale(1.05)

            &_img
                height: 92px
                width: 92px
                background-color: $white
                border-radius: 2px
                margin-right: 15px
                align-self: center

                &-img

            &_content
                display: flex
                flex-direction: column
                justify-content: space-between
                height: 92px

                &_title
                    display: flex
                    justify-content: space-between
                    align-items: flex-start
                    width: 100%

                    &-title
                        margin-bottom: 10px
                        +medium
                        color: $white
                        margin-right: 15px

                    &-cost
                        +light
                        color: $green

                &_tags
                    border-top: 3px solid $orange
                    border-bottom: 3px solid $orange
                    display: flex
                    justify-content: flex-start
                    align-items: flex-start
                    width: 484px
                    height: 45px
                    border-radius: 10px
                    padding: 0 10px

                    &-tag
                        margin: 5px 10px 5px 0
                        border: 1px solid $orange
                        background-color: $trs_gray
                        min-width: 55px
                        height: 30px
                        display: flex
                        justify-content: center
                        align-items: center
                        font-size: 14px
                        +medium
                        color: $white
                        transition: 0.2s
                        border-radius: 5px

                        &:hover
                            transform: scale(1.1)
                            cursor: pointer
</style>