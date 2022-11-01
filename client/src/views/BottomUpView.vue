<template>
  <div class="bottom-up">
    <BottomUpDashboard></BottomUpDashboard>
  </div>
</template>

<script>
import BottomUpDashboard from '@/components/BottomUpDashboard.vue';

  export default {
    data: () => ({
      
    }),
    components: { BottomUpDashboard }
}
</script>

<style>
.bottom-up{
  background-color:chartreuse;
  padding: 10px;
  margin-block-end: 50px;
}
</style>