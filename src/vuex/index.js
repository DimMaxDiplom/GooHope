import {createStore} from "vuex";
import profile from "@/vuex/modules/profile";
import dialogs from "@/vuex/modules/dialogs";

const store = createStore({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        profile,
        dialogs
    },
})

export default store