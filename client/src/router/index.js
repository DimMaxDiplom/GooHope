import {createWebHistory, createRouter} from "vue-router"
import MainPage from "@/components/pages/MainPage";
import Login from "@/components/pages/Login";

const DEFAULT_TITLE = 'GooHope'

const routes = [
    {
        path: "/",
        name: MainPage.name,
        component: MainPage,
    },
    {
        path: "/login",
        name: Login.name,
        component: Login
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})
router.beforeEach((to, from, next) => {
    let text = `${DEFAULT_TITLE} - ${to.name}`
    if (to.name === MainPage.name)
        text = `Добро пожаловать в ${DEFAULT_TITLE}`
    document.title = text;
    next();
})

export default router