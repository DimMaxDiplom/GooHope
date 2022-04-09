import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router";
import VueFeather from 'vue-feather';
import axios from "axios";
import VueAxios from "vue-axios";
import store from "@/vuex";
import Vuex from "vuex";

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

createApp(App).use(router).use(Vuex).use(store).use(VueAxios, axios).component(VueFeather.name, VueFeather).mount('#app')