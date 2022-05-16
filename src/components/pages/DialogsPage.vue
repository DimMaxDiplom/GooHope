<template>
    <main class="main">
        <div class="dialogs">
            <DialogCard v-for="card in cards" :key="card.id"
                        :login="card.login"
                        :status="card.status"
                        :content="card.content"
                        :get="card.get"
                        :read="card.read"
            />
        </div>
        <div class="list">
            <div class="list_title">
                <div class="list_title-title">Недавние диалоги</div>
                <div class="list_title-num">({{ 22 }})</div>
            </div>
            <div class="list_list">
                <ListBar v-for="bar in bars" :key="bar.id" :tile="bar"/>
            </div>
        </div>
    </main>
</template>

<script>
import DialogCard from "@/components/subpages/DialogCard";
import ListBar from "@/components/subpages/ListBar";

export default {
    name: "DialogsPage",
    components: {ListBar, DialogCard},
    data: () => {
        return {
            cards: [
                {
                    login: 'ReF0iL',
                    status: 'Был в сети 6 минут назад',
                    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' +
                        'Curabitur et felis in mi porttitor pretium. Duis eleifend ex nec eros porta, vel tristique eros ' +
                        'posuere. Quisque a ante non eros feugiat aliquam ac a elit. Fusce non libero nec tellus luctus ' +
                        'finibus ut a eros. Aliquam non risus lorem. Nunc ultrices a erat sed dignissim.',
                    get: 'Сегодня',
                    read: 'Сегодня'
                },
                {
                    login: 'ReF0iL 123',
                    status: 'Был в сети 6 минут назад',
                    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' +
                        'Curabitur et felis in mi porttitor pretium. Duis eleifend ex nec eros porta, vel tristique eros ' +
                        'posuere. Quisque a ante non eros feugiat aliquam ac a elit. Fusce non libero nec tellus luctus ' +
                        'finibus ut a eros. Aliquam non risus lorem. Nunc ultrices a erat sed dignissim.',
                    get: 'Сегодня',
                    read: 'Сегодня'
                },
                {
                    login: 'ReF0iL 321',
                    status: 'Был в сети 6 минут назад',
                    content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' +
                        'Curabitur et felis in mi porttitor pretium. Duis eleifend ex nec eros porta, vel tristique eros ' +
                        'posuere. Quisque a ante non eros feugiat aliquam ac a elit. Fusce non libero nec tellus luctus ' +
                        'finibus ut a eros. Aliquam non risus lorem. Nunc ultrices a erat sed dignissim.',
                    get: 'Сегодня',
                    read: 'Сегодня'
                },
            ],
            bars: [
                {
                    title: 'ReF0iL',
                },
                {
                    title: 'ReF0iL',
                },
                {
                    title: 'ReF0iL',
                },
                {
                    title: 'ReF0iL',
                },
                {
                    title: 'ReF0iL',
                },
            ]
        }
    }
}
</script>

<style lang="sass" scoped>
.main
    padding-top: 25px
    width: 1250px
    display: flex
    justify-content: space-between
    align-items: flex-start

    .dialogs
        width: 840px
        background: rgba(72, 84, 96, 0.4)
        box-shadow: 4px 2px 4px rgba(30, 39, 46, 0.3)
        border-radius: 5px
        padding: 10px

    .list
        display: flex
        flex-direction: column
        justify-content: flex-end
        align-items: center

        &_title
            display: flex
            color: $white
            font-size: 18px
            width: 310px
            +medium
            position: relative
            padding-bottom: 10px
            border-bottom: 3px solid $orange
            margin: 0 15px 15px

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

            &-title
                margin-left: 70px
                margin-right: 25px

            &-num

        &_list
            display: flex
            flex-direction: column
            justify-content: flex-start
            align-items: flex-start
            width: 330px
            background-color: $trs_gray
            border-radius: 10px
            padding: 15px 0 5px 20px
</style>