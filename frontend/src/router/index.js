import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Home from '@/components/home/Home'
import SpiderInstanceList from '@/components/SpiderInstanceList'
import Books from '@/components/book/Books'
import BookChapters from '@/components/book/BookChapters'
import BookChapterDetail from '@/components/book/BookChapterDetail'
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
          path: 'spiders',
          component: SpiderInstanceList
        },
        {
          path: 'books',
          component: Books
        }, {
          path: 'books/book/:bookId/chapters',
          component: BookChapters
        },
        {
          path: 'books/book/:bookId/chapter/:chapter/detail',
          component: BookChapterDetail,
          props: {bookId: this.$router.params.bookId, chapter: this.$router.params.chapter}
        },
        {
          path: 'contacts',
          component: Contacts
        }

      ]
    }
  ]
})
