<template>
  <div class="bottom-up">
    <ManagerDashboard></ManagerDashboard>
  </div>
</template>

<script>
import ManagerDashboard from '@/components/ManagerDashboard.vue';

  export default {
    data: () => ({
      
    }),
    components: { ManagerDashboard }
}
</script>

<style>
.bottom-up{
  background-color:chartreuse;
  padding: 10px;
  margin-block-end: 50px;
}
</style>