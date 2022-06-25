<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/casal.jpg" width="40%" height="40%">
    <HelloWorld msg="Te amo, ursona!!!" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
