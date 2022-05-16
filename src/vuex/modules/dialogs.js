import axios from "axios";

const host = 'http://127.0.0.1:8000/dialogs'

const state = {
    dialogs: [],
    dialog_messages: []
}
const getters = {
    DIALOGS: state => {
        return state.dialogs
    },
    MESSAGES: state => {
        return state.dialog_messages
    }
}
const mutations = {
    UPDATE_DIALOGS: (state, dialogs) => {
        state.dialogs = dialogs
    },
    UPDATE_MESSAGES: (state, {messages, idx=null}) => {
        if (idx) {
            state.dialog_messages[idx] = messages
            return
        }
        state.dialog_messages = messages
    },
}
const actions = {
    UPDATE_DIALOGS: async context => {
        axios.get(`${host}`)
            .then(res => {
                if (res.status === 200) {
                    context.commit('UPDATE_DIALOGS', res.data);
                }
            })
            .catch(err => {
                alert(err)
            })
    }
}
export default {
    state,
    getters,
    actions,
    mutations
}