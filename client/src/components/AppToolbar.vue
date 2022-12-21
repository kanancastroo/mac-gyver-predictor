<template>
  <v-card color="#285430" dark flat tile>
    <h1>MacGyver Predictor</h1>
    <v-toolbar flat class="d-flex justify-center align-center" color="#5F8D4E">
      <router-link to="/bottom-up">
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

<style>
.v-toolbar__content {
  gap: 10px;
}
</style>
