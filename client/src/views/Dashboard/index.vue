<template>
  <div class="dashboard">
    <app-toolbar></app-toolbar>
    <router-view />
    <app-footer></app-footer>
  </div>
</template>

<script>
import AppToolbar from "@/components/AppToolbar.vue";
import AppFooter from "@/components/AppFooter.vue";

export default {
  name: "Dashboard",
  components: { AppFooter, AppToolbar },
  mounted() {
    console.log("here");
  },
};
</script>

<style></style>
