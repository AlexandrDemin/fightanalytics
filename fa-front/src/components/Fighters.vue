<template>
  <main>
    <p v-if="!isLoaded">Загрузка...</p>
    <ul v-if="errors && errors.length > 0">
      <li v-for="error in errors">
        {{error}}
      </li>
    </ul>
    <button @click="goToFighter">Добавить бойца</button>
    <table v-if="isLoaded && fighters && fighters.length > 0">
      <tr>
        <th>Имя</th>
        <th>Страна</th>
        <th>Весовая категория</th>
        <th>Год рождения</th>
        <th></th>
      </tr>
      <tr v-for="fighter in fighters" v-bind:key="fighter.id">
        <td>{{fighter.name}}</td>
        <td>{{fighter.country}}</td>
        <td>{{fighter.weight_class}}</td>
        <td>{{fighter.birth_year}}</td>
        <td @click="goToFighter(fighter.id)">Редактировать</td>
      </tr>
    </table>
  </main>
</template>

<script>
import {HTTP} from '@/API/API'

export default {
  name: 'Fighters',
  data () {
    return {
      fighters: [],
      errors: [],
      isLoaded: false
    }
  },
  methods: {
    goToFighter: function (id) {
      if (id) {
        this.$router.push('fighter/' + id)
      } else {
        this.$router.push('fighter')
      }
    }
  },
  created () {
    HTTP.get(`fighters/`)
    .then(response => {
      this.fighters = response.data
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
