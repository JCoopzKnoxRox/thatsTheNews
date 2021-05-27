import axios from 'axios'
import store from '@/store/index'

export default () => {
  return axios.create({
    // TODO: Generalize this -> https://cli.vuejs.org/guide/mode-and-env.html#using-env-variables-in-client-side-code
    //                       -> https://stackoverflow.com/questions/51406770/how-to-set-api-path-in-vue-config-js-for-production
    baseURL: process.env.VUE_APP_API_ENDPOINT,
    headers: {
      Authorization: `JWT ${store.state.token}`
    }
  })
}
