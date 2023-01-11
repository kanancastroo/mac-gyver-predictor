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
        <v-btn v-if="this.showAdmin">Admin</v-btn>
      </router-link>

      <router-link to="/dashboard/logout">
        <v-btn color="red" @click="logout()">Logout</v-btn>
      </router-link>
    </v-toolbar>
  </v-card>
</template>

<script>
import axios from "axios";
import store from "@/store";

export default {
  data: () => ({
    showAdmin: false,
  }),
  created() {
    this.checkUser();
  },
  methods: {
    logout() {
      this.$store.dispatch("logout").then(() => {
        console.log("going to push login");
        this.$router.push("/login");
      });
    },
    checkUser() {
      // console.log("JWT => ", store.getters.getJwt.token);
      const token = store.getters.getJwt.token;
      const path = `${process.env.VUE_APP_BASE_URL}/login/checkuser`;
      let axiosConfig = {
        headers: {
          "Content-Type": "application/json;charset=UTF-8",
          "Access-Control-Allow-Origin": "*",
          Authorization: token,
        },
      };

      console.log("waiting for check...");
      axios
        .post(path, null, axiosConfig)
        .then((res) => {
          this.showAdmin = res.data;
        })
        .catch((err) => {
          this.showAdmin = false;
        });

      // console.log("RESPONSE => ", response);
      // console.log("type => ", typeof response);
      // return response;
    },
  },
};
</script>

<style>
.v-toolbar__content {
  gap: 10px;
}

.page-title {
  text-align: center;
}
</style>
