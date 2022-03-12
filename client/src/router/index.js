import {createWebHistory, createRouter} from "vue-router"
import MainPage from "@/components/pages/MainPage";
import SignIn from "@/components/pages/SignIn";

const DEFAULT_TITLE = 'GooHope'

const routes = [
    {
        path: "/",
        name: MainPage.name,
        component: MainPage,
    },
    {
        path: "/sign_in",
        name: SignIn.name,
        component: SignIn
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