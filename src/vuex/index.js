import {createStore} from "vuex";
import profile from "@/vuex/modules/profile";
import dialogs from "@/vuex/modules/dialogs";
import content from "@/vuex/modules/content";

const store = createStore({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        profile,
        dialogs,
        content
    },
})

export default store