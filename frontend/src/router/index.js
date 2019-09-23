import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Home from '@/components/home/Home'
import SpiderInstanceList from '@/components/SpiderInstanceList'
import Books from '@/components/book/Books'
import Contacts from '@/components/Contacts'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
      children: [
        {
          path: '',
          component: Home
        },
        {
          path: 'spider',
          component: SpiderInstanceList
        },
        {
          path: 'books',
          component: Books
        },
        {
          path: 'contacts',
          component: Contacts
        }

      ]
    }
  ]
})
