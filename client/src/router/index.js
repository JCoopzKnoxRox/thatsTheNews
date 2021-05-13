import { createRouter, createWebHistory } from 'vue-router';

import Home from '@/views/Home'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Covid',
    name: 'Covid',
    component:  () => import(/* webpackChunkName: "Left" */ '@/views/Covid')
  },
  {
    path: '/Entertainment',
    name: 'Entertainment',
    component:  () => import(/* webpackChunkName: "Left" */ '@/views/Entertainment')
  },
  {
    path: '/Climate',
    name: 'Climate',
    component:  () => import(/* webpackChunkName: "Left" */ '@/views/Climate')
  },
  {
    path: '/Crypto',
    name: 'Crypto',
    component:  () => import(/* webpackChunkName: "Left" */ '@/views/Crypto')
  },
  {
    path: '/Sports',
    name: 'Sports',
    component:  () => import(/* webpackChunkName: "Left" */ '@/views/Sports')
  },
  {
    path: '/Tech',
    name: 'Tech',
    component:  () => import(/* webpackChunkName: "Left" */ '@/views/Tech')
  },
  {
    path: '/Politics',
    name: 'Politics',
    component:  () => import(/* webpackChunkName: "Politics" */ '@/views/Politics')
  },
  {
    path: '/Stocks',
    name: 'Stocks',
    component:  () => import(/* webpackChunkName: "Stocks" */ '@/views/Stocks')
  },
  {
    path: '/newsPost',
    name: 'newsPost',
    component:  () => import(/* webpackChunkName: "newsPost" */ '@/views/newsPost')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import(/* webpackChunkName: "login" */ '@/views/Login')
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: () => import(/* webpackChunkName: "signup" */ '@/views/SignUp')
  },
  {
    path: '/s/:name',
    name: 'Subvue',
    component: () => import(/* webpackChunkName: "subvue" */ '@/views/Subvue')
  },
  {
    path: '/s/:subvuePermalink/:id',
    name: 'Post',
    component: () => import(/* webpackChunkName: "post" */ '@/views/Post')
  },
  {
    path: '/u/:username',
    name: 'User',
    component: () => import(/* webpackChunkName: "user" */ '@/views/User')
  },
  {
    path: '/create',
    name: 'CreatePost',
    component: () => import(/* webpackChunkName: "create" */ '@/views/CreatePost')
  },
  {
    path: '/create/subvue',
    name: 'CreateSubvue',
    component: () => import(/* webpackChunkName: "createsubvue" */ '@/views/CreateSubvue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
