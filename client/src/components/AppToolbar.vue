<template>
  <v-card color="#285430" dark flat tile>
    <h1 class="page-title">MacGyver Predictor</h1>
    <v-toolbar flat class="d-flex justify-center align-center" color="#5F8D4E">
      <router-link to="/dashboard/bottom-up">
        <v-btn>Bottom-Up</v-btn>
      </router-link>

      <router-link to="/dashboard/manager">
        <v-btn>Manager</v-btn>
      </router-link>

      <router-link to="/dashboard/top-down">
        <v-btn>Top-Down</v-btn>
      </router-link>

      <router-link to="/dashboard/admin">
        <v-btn>Admin</v-btn>
      </router-link>

      <router-link to="/dashboard/logout">
        <v-btn color="red">Logout</v-btn>
      </router-link>
    </v-toolbar>
  </v-card>
</template>

<style>
.v-toolbar__content {
  gap: 10px;
}

.page-title {
  text-align: center;
}
</style>
