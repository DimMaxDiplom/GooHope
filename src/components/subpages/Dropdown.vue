<template>
    <div class="btn-group">
        <li @click="toggleMenu" class="dropdown-toggle" v-if="selectedOption.name !== undefined">
            {{ selectedOption.name }}
            <span class="caret"></span>
        </li>

        <li @click="toggleMenu" class="dropdown-toggle dropdown-toggle-placeholder"
            v-if="selectedOption.name === undefined">
            {{ placeholderText }}
            <span class="caret"></span>
        </li>

        <ul class="dropdown-menu" v-if="showMenu">
            <li v-for="(option, idx) in options" :key="idx">
                <a href="javascript:void(0)" @click="updateOption(option)">
                    {{ option.name }}
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'DropDown',
    data() {
        return {
            selectedOption: {
                name: '',
            },
            showMenu: false,
            placeholderText: 'Please select an item',
        }
    },
    props: {
        options: {
            type: [Array, Object]
        },
        selected: {},
        placeholder: [String],
        closeOnOutsideClick: {
            type: [Boolean],
            default: true,
        },
    },

    mounted() {
        this.selectedOption = this.selected;
        if (this.placeholder) {
            this.placeholderText = this.placeholder;
        }

        if (this.closeOnOutsideClick) {
            document.addEventListener('click', this.clickHandler);
        }
    },

    beforeUnmount() {
        document.removeEventListener('click', this.clickHandler);
    },

    methods: {
        updateOption(option) {
            this.selectedOption = option;
            this.showMenu = false;
            this.$emit('updateOption', this.selectedOption);
        },

        toggleMenu(event) {
            this.showMenu = !this.showMenu;
            event.target.classList.toggle('active')
            document.getElementsByClassName('caret')[0].classList.toggle('active')
        },

        clickHandler(event) {
            const {target} = event;
            const {$el} = this;

            if (!$el.contains(target)) {
                this.showMenu = false;
                document.getElementsByClassName('dropdown-toggle')[0].classList.remove('active')
                document.getElementsByClassName('caret')[0].classList.remove('active')
            }
        },
    }
}
</script>

<style lang="sass" scoped>
.btn-group
    position: relative
    display: inline-block
    vertical-align: middle
    margin-bottom: 30px

    & a:hover
        text-decoration: none

    & .dropdown
        &-toggle
            color: $black
            text-transform: uppercase
            font-size: 18px
            +medium
            display: flex
            flex-direction: column
            justify-content: center
            align-items: flex-start
            width: 630px
            height: 70px
            background-color: transparent
            border: 2px solid $trs_gray
            padding-left: 40px
            outline: none
            position: relative
            vertical-align: middle
            &.active
                border: 2px solid $gray

            &:hover
                cursor: pointer

        &-menu
            position: absolute
            top: 100%
            left: 0
            z-index: 1000
            float: left
            width: 100%
            padding: 5px 0
            margin: 2px 0 0
            list-style: none
            font-size: 14px
            text-align: left
            background-color: $white
            border: 1px solid $trs_gray
            border-radius: 4px
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175)
            background-clip: padding-box

            & > li
                overflow: hidden
                width: 100%
                position: relative
                margin: 0

                & > a
                    padding: 10px 30px
                    display: block
                    clear: both
                    font-weight: normal
                    line-height: 1.6
                    color: $black
                    white-space: nowrap
                    text-decoration: none
                    +medium
                    font-size: 18px

                    &:hover
                        background: $gray
                        color: $white

.caret
    width: 0
    position: absolute
    top: 50%
    height: 0
    margin-left: -24px
    vertical-align: middle
    border-top: 6px dashed
    border-top: 6px solid
    border-right: 6px solid transparent
    border-left: 6px solid transparent
    right: 10px
    color: $trs_gray
    &.active
        color: $gray


li
    list-style: none
</style>
