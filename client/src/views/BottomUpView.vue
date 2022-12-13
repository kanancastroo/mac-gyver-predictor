<template>
  <div class="bottom-up">
    <BottomUpDashboard />
  </div>
</template>

<script>
import BottomUpDashboard from "@/components/BottomUpDashboard.vue";

export default {
  components: { BottomUpDashboard },
};
</script>

<style>
.bottom-up {
  height: calc(100vh - 160px);
  background-color: #dfe8cc;
  padding: 10px;
}
</style>
