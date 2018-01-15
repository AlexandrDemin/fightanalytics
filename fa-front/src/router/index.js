import Vue from 'vue'
import Router from 'vue-router'
import Fighters from '@/components/Fighters'
import Fights from '@/components/Fights'
import Fighter from '@/components/Fighter'
import Fight from '@/components/Fight'

Vue.use(Router)

export default new Router({
  scrollBehavior (to, from, savedPosition) {
    return { x: 0, y: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'Fighters',
      component: Fighters
    },
    {
      path: '/fights',
      name: 'Fights',
      component: Fights
    },
    {
      path: '/fighter/:id',
      name: 'Fighter',
      component: Fighter
    },
    {
      path: '/fight/:id',
      name: 'Fight',
      component: Fight
    }
  ]
})
