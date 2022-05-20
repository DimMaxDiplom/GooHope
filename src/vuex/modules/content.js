import axios from "axios";

const host = 'http://127.0.0.1:8000/api/content'

const state = {
    illustrations: [],
    videos: [],
    reviews: [],
    news: []
}
const getters = {
    ILLUSTRATIONS: state => {
        return state.illustrations
    },
    PAIRS_ILLS: state => {
        return [state.illustrations.slice(0, 2), state.illustrations.slice(2, 4)]
    },
    VIDEOS: state => {
        return state.videos
    },
    PAIRS_VIDEOS: state => {
        return [state.videos.slice(0, 2), state.videos.slice(2, 4)]
    },
    REVIEWS: state => {
        return state.reviews
    },
    PAIRS_REVIEWS: state => {
        return [state.reviews.slice(0, 2), state.reviews.slice(2, 4)]
    },
    NEWS: state => {
        return state.news
    }
}
const mutations = {
    UPDATE_ILLUSTRATIONS: (state, illustrations) => {
        state.illustrations = illustrations
    },
    UPDATE_VIDEOS: (state, videos) => {
        state.videos = videos
    },
    UPDATE_REVIEWS: (state, reviews) => {
        state.reviews = reviews
    },
    UPDATE_NEWS: (state, news) => {
        state.news = news
    },
}
const actions = {
    DOWN_ILLUSTRATIONS: async context => {
        console.log('here')
        axios.get(`${host}/illustrations`)
            .then(res => {
                if (res.status === 200) {
                    context.commit('UPDATE_ILLUSTRATIONS', res.data);
                }
            })
            .catch(err => {
                alert(err)
            })
    },
    DOWN_VIDEOS: async context => {
        axios.get(`${host}/videos`)
            .then(res => {
                if (res.status === 200) {
                    context.commit('UPDATE_VIDEOS', res.data);
                }
            })
            .catch(err => {
                alert(err)
            })
    },
    DOWN_REVIEWS: async context => {
        axios.get(`${host}/reviews`)
            .then(res => {
                if (res.status === 200) {
                    context.commit('UPDATE_REVIEWS', res.data);
                }
            })
            .catch(err => {
                alert(err)
            })
    },
    DOWN_NEWS: async context => {
        axios.get(`${host}/news`)
            .then(res => {
                if (res.status === 200) {
                    context.commit('UPDATE_NEWS', res.data);
                }
            })
            .catch(err => {
                alert(err)
            })
    },
}
export default {
    state,
    getters,
    actions,
    mutations
}