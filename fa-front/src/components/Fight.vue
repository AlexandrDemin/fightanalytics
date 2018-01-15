<template>
    <div>
      <h1><router-link to="/fights">Бои</router-link> →
        <span v-if="isLoaded">{{fighters[0]}} против {{fighters[1]}}</span>
        <span v-else>...</span>
      </h1>
      <p v-if="!isLoaded">Загрузка...</p>
      <ul v-if="errors && errors.length > 0">
        <li v-for="error in errors">
          {{error}}
        </li>
      </ul>
      <form v-if="isLoaded">
        <div>
          <label for="name">Дата</label>
          <input type="text" name="name" v-on:blur="validateDate" ref="dateInput" autofocus>
          <p class="error" v-if="!dateValid">Необходимо указать дату в формате дд.мм.гг</p>
        </div>
        <div>
          <label for="place">Место проведения</label>
          <input type="text" name="place" v-model="place" v-on:blur="validatePlace">
          <p class="error" v-if="!placeValid">Необходимо указать место</p>
        </div>
        <div>
          <label for="fighters">Участники</label>
          <input type="text" name="fighters" v-model="fightersStr" v-on:blur="validateFighters">
          <p class="error" v-if="!fightersValid">Необходимо указать id участников через запятую</p>
        </div>
        <div>
          <label for="result">Результат боя</label>
          <input type="text" name="result" v-model="result" v-on:blur="validateResult">
          <p class="error" v-if="!resultValid">Необходимо указать результат боя.</p>
        </div>
        <div v-if="result!=4">
          <label for="winner_id">Победитель</label>
          <input type="text" name="winner_id" v-model="winner_id" v-on:blur="validateWinnerId">
          <p class="error" v-if="!winnerIdValid">Необходимо указать id победителя. Победитель должен быть среди участников боя.</p>
        </div>
        <button type="button" @click="save" ref="saveButton">Сохранить</button>
      </form>
    </div>
</template>

<script>
import {HTTP} from '@/API/API'
export default {
  name: 'Fights',
  data () {
    return {
      id: 0,
      place: 'Москва, Олимпийский',
      date: new Date(),
      sport: '1',
      result: 2,
      winner_id: 0,
      fighters: [1, 2],
      fightersStr: '1, 2',
      isLoaded: false,
      placeValid: true,
      dateValid: true,
      resultValid: true,
      winnerIdValid: true,
      fightersValid: true,
      errors: []
    }
  },
  methods: {
    validatePlace: function () {
      this.placeValid = true
    },
    validateDate: function () {
      this.dateValid = true
    },
    validateResult: function () {
      this.resultValid = true
    },
    validateWinnerId: function () {
      this.winnerIdValid = true
    },
    validateFighters: function () {
      this.fighters = this.fightersStr.split(', ')
      this.fightersValid = true
    },
    save: function () {
      this.validatePlace()
      this.validateDate()
      this.validateResult()
      this.validateWinnerId()
      this.validateFighters()
      if (this.placeValid && this.dateValid && this.resultValid && this.winnerIdValid &&
        this.fightersValid) {
        this.$refs.saveButton.disabled = true
        var data = {
          place: this.place,
          date: this.date,
          result: this.result,
          sport: this.sport,
          winner_id: this.winner_id,
          fighters: this.fighters
        }
        var id = parseInt(this.$route.params.id)
        var url = `fight/0`
        if (id > 0) {
          url = `fight/` + id
        }
        HTTP.post(url, data)
        .then(response => {
          var result = response.data.result
          alert(result)
          this.$refs.saveButton.disabled = false
        })
        .catch(e => {
          this.errors.push(e)
          this.$refs.saveButton.disabled = false
        })
      }
    }
  },
  created () {
    var id = this.$route.params.id
    if (id && parseInt(id) > 0) {
      HTTP.get(`fight/` + parseInt(id))
        .then(response => {
          var data = response.data
          this.id = data.id
          this.place = data.place
          this.date = data.date
          this.result = data.result
          this.sport = data.sport
          this.winner_id = data.winner_id
          this.fighters = data.fighters
          this.isLoaded = true
        })
        .catch(e => {
          this.errors.push(e)
          this.isLoaded = true
        })
    } else {
      this.isLoaded = true
    }
  },
  mounted () {
    if (this.$refs.dateInput) {
      this.$refs.dateInput.focus()
    }
  }
}
</script>

<style scoped>
label {
  display: block;
  margin-bottom: 3px;
}
</style>
