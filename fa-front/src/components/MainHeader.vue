<template>
  <header>
    <nav>
      <router-link to="/">Бойцы</router-link>
      <router-link to="/fights">Бои</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'MainHeader',
  data () {
    return {
      msg: 'MainHeader'
    }
  }
}
</script>

<style scoped>

</style>
