<template>
  <v-app>
    <div id="app">
      <app-toolbar></app-toolbar>
      <router-view />
      <app-footer></app-footer>
    </div>
  </v-app>
</template>

<script>
import AppToolbar from "@/components/AppToolbar.vue";
import AppFooter from "@/components/AppFooter.vue";

export default {
  name: "App",
  components: { AppFooter, AppToolbar },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900");
@import url("https://cdn.jsdelivr.net/npm/@mdi/font@6.x/css/materialdesignicons.min.css");

#app {
  font-family: Roboto, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

:where(a) {
  text-decoration: none;
}

:where(nav) {
  padding: 30px;
}
</style>
