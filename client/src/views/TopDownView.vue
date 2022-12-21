<template>
  <div class="top-down">
    <TopDownDashboard></TopDownDashboard>
  </div>
</template>

<script>
import TopDownDashboard from '@/components/TopDownDashboard.vue';

  export default {
    data: () => ({
      
    }),
    components: { TopDownDashboard }
}
</script>

<style>
.bottom-up{
  background-color:chartreuse;
  padding: 10px;
  margin-block-end: 50px;
}
</style>