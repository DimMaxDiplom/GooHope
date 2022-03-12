import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router";
import store from "@/vuex";
import VueFeather from 'vue-feather'

createApp(App).use(router).use(store).component(VueFeather.name, VueFeather).mount('#app')