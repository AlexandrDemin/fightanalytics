<template>
    <div>
      <h1><router-link to="/">Бойцы</router-link> →
        <span v-if="isLoaded">{{name}}</span>
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
          <label for="name">Имя</label>
          <input type="text" name="name" v-model="name" v-on:blur="validateName" ref="nameInput" autofocus>
          <p class="error" v-if="!nameValid">Необходимо указать имя</p>
        </div>
        <div>
          <label for="country">Страна</label>
          <input type="text" name="country" v-model="country" v-on:blur="validateCountry">
          <p class="error" v-if="!countryValid">Необходимо указать страну</p>
        </div>
        <div>
          <label for="birth_year">Год рождения</label>
          <input type="text" name="birth_year" v-model="birth_year" v-on:blur="validateBirthYear">
          <p class="error" v-if="!birthYearValid">Необходимо указать год рождения</p>
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
      name: 'Новый боец',
      country: 'Россия',
      picture_url: '',
      sport: '1',
      weight_class: 1,
      birth_year: 1991,
      isLoaded: false,
      nameValid: true,
      countryValid: true,
      birthYearValid: true,
      errors: []
    }
  },
  methods: {
    validateName: function () {
      if (this.name.length === 0) {
        this.nameValid = false
      }
    },
    validateCountry: function () {
      if (this.country.length === 0) {
        this.countryValid = false
      } else {
        this.countryValid = true
      }
    },
    validateBirthYear: function () {
      if (this.birth_year.length === 0) {
        this.birthYearValid = false
      } else {
        this.birthYearValid = true
      }
    },
    save: function () {
      this.validateName()
      this.validateCountry()
      this.validateBirthYear()
      if (this.birthYearValid && this.nameValid && this.countryValid) {
        this.$refs.saveButton.disabled = true
        var data = {
          name: this.name,
          country: this.country,
          picture_url: this.picture_url,
          sport: this.sport,
          weight_class: this.weight_class,
          birth_year: this.birth_year
        }
        var id = parseInt(this.$route.params.id)
        var url = `fighter/0`
        if (id > 0) {
          url = `fighter/` + id
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
      HTTP.get(`fighter/` + parseInt(id))
        .then(response => {
          var data = response.data
          this.id = data.id
          this.name = data.name
          this.country = data.country
          this.picture_url = data.picture_url
          this.sport = data.sport
          this.weight_class = data.weight_class
          this.birth_year = data.birth_year
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
    if (this.$refs.nameInput) {
      this.$refs.nameInput.focus()
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
