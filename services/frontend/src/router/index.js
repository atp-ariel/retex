import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/credits',
    name: 'Credits',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "credits" */ '@/views/Credits.vue')
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import(/* webpackChunkName: "search" */ '@/views/Search.vue'),
    props: true
  },
  {
    path: '/docs/:id',
    name: 'Doc',
    component: () => import(/* webpackChunkName: "doc" */ '@/views/Doc.vue'),
    props: true
  },
  {
    path: '/evaluation',
    name: "Eval",
    component: () => import("@/views/Eval.vue")
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
