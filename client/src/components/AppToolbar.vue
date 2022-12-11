<template>
  <v-card
    color="green lighten-5"
    flat
    tile
  >
    <div><h1>MacGyver Predictor</h1></div>
    <v-toolbar flat class="d-flex justify-center align-center" color="green lighten-2">
      <!-- <v-toolbar-title>MacGyver Predictor</v-toolbar-title> -->

      <router-link to="/">
        <v-btn>Bottom-Up</v-btn>
      </router-link>

      <router-link to="/manager">
        <v-btn>Manager</v-btn>
      </router-link>

      <router-link to="/top-down">
        <v-btn>Top-Down</v-btn>
      </router-link>

      <router-link to="/admin">
        <v-btn>Admin</v-btn>
      </router-link>

    </v-toolbar>
  </v-card>
</template>