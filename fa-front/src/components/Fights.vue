<template>
  <main>
    <p v-if="!isLoaded">Загрузка...</p>
    <ul v-if="errors && errors.length > 0">
      <li v-for="error in errors">
        {{error}}
      </li>
    </ul>
    <button @click="goToFight">Добавить бой</button>
    <table v-if="isLoaded && fights && fights.length > 0">
      <tr>
        <th>Дата</th>
        <th>Место</th>
        <th>Результат</th>
        <th>Победитель</th>
        <th></th>
      </tr>
      <tr v-for="fight in fights" v-bind:key="fight.id">
        <td>{{fight.date}}</td>
        <td>{{fight.place}}</td>
        <td>{{fight.result}}</td>
        <td>{{fight.winner_id}}</td>
        <td @click="goToFight(fight.id)">Редактировать</td>
      </tr>
    </table>
  </main>
</template>

<script>
import {HTTP} from '@/API/API'

export default {
  name: 'Fights',
  data () {
    return {
      fights: [],
      errors: [],
      isLoaded: false
    }
  },
  methods: {
    goToFight: function (id) {
      if (id) {
        this.$router.push('fight/' + id)
      } else {
        this.$router.push('fight')
      }
    }
  },
  created () {
    HTTP.get(`fights/`)
    .then(response => {
      this.fights = response.data
      this.isLoaded = true
    })
    .catch(e => {
      this.errors.push(e)
      this.isLoaded = true
    })
  }
}
</script>

<style scoped>

</style>
