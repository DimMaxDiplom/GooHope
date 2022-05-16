import axios from "axios";

const host = 'http://127.0.0.1:8000/user'

const state = {
    profile_friends: [],
    profile_societies: [],
    user: {},
}
const getters = {
    FRIENDS_LIST: state => {
        return {
            'friends': state.profile_friends.map(elem => {
                return {
                    'title': 'ReF0iL', // TODO: change to profile.login
                    // eslint-disable-next-line no-constant-condition
                    'color': elem.status ? 'green' : 'red',
                    // eslint-disable-next-line no-constant-condition
                    'content': elem.status ? 'Online' : 'Последний раз в сети: 5ч 37мин назад' // TODO: change to profile.updated
                }
            }),
            'friends_count': state.profile_friends.length
        }
    },
    SOCIETIES_LIST: state => {
        return {
            'groups': state.profile_societies,
            'groups_count': state.profile_societies.length
        }
    },
    USER: state => {
        return state.user
    }
}
const mutations = {
    UPDATE_FRIENDS: (state, friends_list) => {
        state.profile_friends = friends_list
    },
    UPDATE_SOCIETIES: (state, societies_list) => {
        state.profile_societies = societies_list
    },
    UPDATE_PROFILE_INFO: (state, {profile, is_hidden}) => {
        state.user = profile
        state.user.hidden = is_hidden
        state.user.status = state.user.status ? 'Online' : 'Последний раз в сети: 5ч 37мин назад' // TODO: change to profile.updated
    }
}
const actions = {
    UPDATE_PROFILE: async (context, profile_id) => {
        axios.get(`${host}`, {
            params: {
                id: profile_id
            }
        })
            .then(res => {
                if (res.status === 200) {
                    context.commit('UPDATE_FRIENDS', res.data.friends);
                    context.commit('UPDATE_SOCIETIES', res.data.societies)
                    context.commit('UPDATE_PROFILE_INFO', {
                            'profile': res.data.user,
                            'is_hidden': res.data.hidden
                        })
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