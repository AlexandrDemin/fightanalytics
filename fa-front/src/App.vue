<template>
  <div id="app">
    <mainHeader/>
    <router-view/>
  </div>
</template>

<script>
import MainHeader from '@/components/MainHeader'

export default {
  name: 'app',
  components: {
    'mainHeader': MainHeader
  }
}
</script>

<style>

</style>
