import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Challenge from '../views/Challenge.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Solution from '../views/Solution.vue'
import MyAccount from '../views/MyAccount.vue'
import Create from '../views/Create.vue'
import Successcr from '../views/Successcr.vue'
import search from '../views/search.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/category/:category_slug',
    name: 'category',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },

  {
    name:'Challenge',
    path:'/challenge/:category_slug/:product_slug',
    component:Challenge
  },
  {
    name: "Login",
    path:'/log-in/',
    component:Login
  },
  {
    name: 'Signup',
    path: '/signup/',
    component: Signup
  },

  {
    name:'Solution',
    path:'/challenge/:category_slug/:product_slug/solution',
    component:Solution
  },


 { 
  name:'MyAcc',
  path:'/myacc',
  component: MyAccount
},

{ 
  name:'Create',
  path:'/create',
  component: Create
},

{ 
  name:'Successcr',
  path:'/successcr',
  component: Successcr
},
{ 
  name:'Search',
  path:'/search',
  component: search
},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
