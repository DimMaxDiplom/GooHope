import {createWebHistory, createRouter} from "vue-router"
import MainPage from "@/components/pages/MainPage";
import Login from "@/components/pages/Login";

const routes = [
    {
        path: "/",
        name: MainPage.name,
        component: MainPage
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

export default router