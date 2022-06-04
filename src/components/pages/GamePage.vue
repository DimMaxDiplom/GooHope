<template>
    <div class="main">
        <div class="header">
            <div class="header_main">
                <div class="header_main_img">
                    <img src="" alt="" class="header_main_img-img">
                </div>
                <div class="header_main_content">
                    <div class="header_main_content_title">
                        <div class="header_main_content_title-game">{{ "Dota 2" }}</div>
                        <div class="header_main_content_title-cost">{{ 100.49 }} $</div>
                    </div>
                    <div class="header_main_content-data">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ante nisl, lobortis ut
                        dignissim quis, gravida non velit. Sed sollicitudin sem in urna convallis, sed interdum lacus fringilla. Curabitur quis ante
                        enim. Praesent porttitor, tellus iaculis lacinia vulputate, ante lacus tincidunt orci, at efficitur purus arcu id lacus.
                    </div>
                    <div class="header_main_content_tags">
                        <div class="header_main_content_tags-tag" v-for="tag in tags" :key="tag.id">
                            {{ tag.name }}
                        </div>
                    </div>
                </div>
                <div class="header_main_info">
                    <div class="header_main_info-line">Издатель: {{ publisher }}</div>
                    <div class="header_main_info-line">Разработчик: {{ developer }}</div>
                    <div class="header_main_info-line">Дата выхода: {{ publish_date }}</div>
                    <div class="header_main_info-line">Обзоров: {{ review_count }}</div>
                </div>
            </div>
            <div class="header_btns">
                <div class="header_btns-buy">Приобрести</div>
                <div class="header_btns-favorite">Добавить в избранное</div>
            </div>
        </div>
        <div class="requirements">
            <div class="requirements-title">Системные требования</div>
            <div class="requirements_cols">
                <div class="requirements_cols_col">
                    <div class="requirements_cols_col-title">Минимальные</div>
                    <div class="requirements_cols_col_data">
                        <div class="requirements_cols_col_data-component">ОС: {{ min.os }}</div>
                        <div class="requirements_cols_col_data-component">Процессор: {{ min.proc }}</div>
                        <div class="requirements_cols_col_data-component">Оперативная память: {{ min.RAM }}</div>
                        <div class="requirements_cols_col_data-component">Видеокарта: {{ min.video_card }}</div>
                        <div class="requirements_cols_col_data-component">Место на диске: {{ min.memory }}</div>
                    </div>
                </div>
                <div class="requirements_cols_col">
                    <div class="requirements_cols_col-title">Рекомендуемые</div>
                    <div class="requirements_cols_col_data">
                        <div class="requirements_cols_col_data-component">ОС: {{ rec.os }}</div>
                        <div class="requirements_cols_col_data-component">Процессор: {{ rec.proc }}</div>
                        <div class="requirements_cols_col_data-component">Оперативная память: {{ rec.RAM }}</div>
                        <div class="requirements_cols_col_data-component">Видеокарта: {{ rec.video_card }}</div>
                        <div class="requirements_cols_col_data-component">Место на диске: {{ rec.memory }}</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="reviews">
            <div class="reviews-title">Обзоры</div>
            <div class="reviews_card">
                <div class="reviews_card_img">
                    <img src="" alt="" class="reviews_card_img-img">
                </div>
                <div class="reviews_card_content">
                    <div class="reviews_card_content-login">ReF0iL</div>
                    <div class="reviews_card_content-content">
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tristique mi et finibus placerat. Suspendisse venenatis id
                        libero eget sagittis. Fusce luctus, turpis ut mollis placerat, arcu eros volutpat odio, at porta dolor dolor in ligula. Aliquam
                        vulputate faucibus vestibulum. Nam pellentesque lorem no
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "GamePage",
    data() {
        return {
            tags: [
                {
                    name: 'Data',
                },
                {
                    name: 'Best',
                },
            ],
            publisher: 'Carbon Studio',
            developer: 'Carbon Studio',
            publish_date: '26.01.2022',
            review_count: '422',
            min: {
                os: '',
                proc: '',
                RAM: '',
                video_card: '',
                memory: ''
            },
            rec: {
                os: '',
                proc: '',
                RAM: '',
                video_card: '',
                memory: ''
            }
        }
    }
}
</script>

<style scoped lang="sass">
.main
    display: flex
    justify-content: center
    align-items: center
    margin-top: 35px
    flex-direction: column

    & .header
        border-bottom: 3px solid $green
        display: flex
        justify-content: center
        align-items: center
        flex-direction: column
        padding-bottom: 55px

        &_main
            display: flex
            justify-content: center
            align-items: flex-end

            &_img
                width: 380px
                height: 380px
                background-color: $gray

                &-img
                    max-width: 374px
                    height: 374px

            &_content
                display: flex
                flex-direction: column
                justify-content: center
                margin-left: 52px

                &_title
                    display: flex
                    justify-content: space-between
                    align-items: flex-end
                    margin-bottom: 36px
                    width: 484px

                    &-game
                        color: $white
                        font-size: 24px
                        +medium
                        border-bottom: 3px solid $orange
                        width: 270px
                        text-align: center
                        position: relative
                        padding-bottom: 10px

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

                    &-cost
                        color: $green
                        font-size: 18px
                        +medium
                        border-bottom: 3px solid $green
                        width: 160px
                        text-align: center
                        position: relative
                        padding-bottom: 10px
                        margin-right: 5px

                        &::after, &::before
                            content: ''
                            display: block
                            position: absolute
                            right: -19px
                            bottom: -10px
                            width: 12px
                            height: 12px
                            background-color: $green
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

                &-data
                    color: $white
                    font-size: 14px
                    text-align: left
                    +medium
                    width: 484px
                    margin-bottom: 20px
                    margin-right: 40px

                &_tags
                    border-top: 3px solid $orange
                    border-bottom: 3px solid $orange
                    display: flex
                    justify-content: flex-start
                    align-items: flex-start
                    width: 484px
                    height: 160px
                    border-radius: 10px
                    padding: 0 10px

                    &-tag
                        margin: 10px 10px 10px 0
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

            &_info
                display: flex
                flex-direction: column
                justify-content: center
                align-items: center

                &-line
                    color: $white
                    width: 275px
                    font-size: 16px
                    +medium
                    border-bottom: 3px solid $orange
                    text-align: center
                    padding-bottom: 20px
                    margin-bottom: 60px
                    position: relative

                    &:last-child
                        margin-bottom: 0

                    &::after, &::before
                        content: ''
                        display: block
                        position: absolute
                        right: -19px
                        bottom: -10px
                        width: 12px
                        height: 12px
                        background-color: $orange
                        transform: rotate(-45deg)
                        transform-origin: 0 100%

                    &::before
                        left: -6px


        &_btns
            display: flex
            justify-content: space-between
            align-items: center
            width: 100%
            margin-top: 50px

            &-buy
                border: 1px solid $green
                background-color: $trs_gray
                width: 290px
                height: 56px
                display: flex
                justify-content: center
                align-items: center
                color: $white
                +medium
                font-size: 24px

            &-favorite
                border: 1px solid $orange
                background-color: $trs_gray
                width: 330px
                height: 56px
                display: flex
                justify-content: center
                align-items: center
                color: $white
                +medium
                font-size: 24px

            & div
                transition: 0.2s

                &:hover
                    transform: scale(1.1)
                    cursor: pointer

    & .requirements
        display: flex
        justify-content: flex-start
        align-items: flex-start
        flex-direction: column
        width: 1250px
        margin-bottom: 70px
        margin-left: 15px

        &-title
            color: $white
            font-size: 18px
            +light
            text-transform: uppercase
            margin: 15px 0

        &_cols
            display: flex
            justify-content: space-between
            align-items: flex-start
            width: 70%

            &_col
                display: flex
                flex-direction: column
                justify-content: flex-start
                align-items: flex-start

                &-title
                    +bold
                    font-size: 20px
                    color: $white
                    border-bottom: 2px solid $white
                    margin-bottom: 15px

                &_data
                    display: flex
                    flex-direction: column
                    justify-content: center
                    align-items: flex-start

                    &-component
                        color: $white
                        font-size: 18px
                        +light
                        margin: 5px 0
    .reviews
        display: flex
        justify-content: flex-start
        align-items: flex-start
        flex-direction: column
        margin-left: 15px
        width: 1250px
        margin-bottom: 25px
        &-title
            text-align: left
            border-bottom: 3px solid $orange
            font-size: 22px
            width: 120px
            +medium
            color: $white
            margin-bottom: 25px
            padding-bottom: 5px
        &_card
            background-color: $trs_gray
            width: 100%
            border-radius: 10px
            height: 140px
            margin-bottom: 10px
            display: flex
            justify-content: flex-start
            align-items: center
            &_img
                width: 130px
                height: 130px
                background-color: $white
                margin-left: 5px
                &-img
            &_content
                display: flex
                flex-direction: column
                align-items: flex-start
                margin-left: 15px
                &-login
                    margin-bottom: 10px
                    margin-top: 10px
                    color: $white
                    +medium
                    font-size: 20px
                    border-bottom: 3px solid $orange
                    width: 125px
                &-content
                    height: 110px
                    width: 1000px
                    color: $white
                    +light
                    font-size: 16px


</style>