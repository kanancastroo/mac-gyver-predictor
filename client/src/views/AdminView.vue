<template>
  <div class="admin">
    <AdminDashboard></AdminDashboard>
  </div>
</template>

<script>
import AdminDashboard from '@/components/AdminDashboard.vue';

  export default {
    data: () => ({
      
    }),
    components: { AdminDashboard }
}
</script>

<style>
.admin{
  background-color:chartreuse;
  padding: 10px;
  margin-block-end: 50px;
}
</style>