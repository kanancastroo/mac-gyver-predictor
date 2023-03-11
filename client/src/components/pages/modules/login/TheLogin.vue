<template>
  <div class="body">
    <div class="container has-text-centered">
      <h1 class="subtitle">MacGyver Predictor 2.0</h1>
    </div>
    <div class="container has-text-centered">
      <h4 class="title">Login or Register</h4>
      <p class="subtitle error-msg">{{ errorMsg }}</p>
    </div>
    <section class="section">
      <div class="container">
        <div class="field">
          <label class="label is-large" for="email">Email:</label>
          <div class="control">
            <v-text-field
              type="email"
              class="input is-large"
              id="email"
              v-model="email"
              solo
            ></v-text-field>
          </div>
        </div>
        <div class="field">
          <label class="label is-large" for="password">Password:</label>
          <div class="control">
            <v-text-field
              solo
              type="password"
              class="input is-large"
              id="password"
              v-model="password"
            ></v-text-field>
          </div>
        </div>

        <div class="control">
          <v-spacer></v-spacer>
          <v-btn elevation="2" @click="authenticate" color="#A4BE7B" dark
            >Login</v-btn
          >
          <v-spacer></v-spacer>
          <v-btn elevation="2" @click="register" color="#A4BE7B" dark
            >Register</v-btn
          >
          <v-spacer></v-spacer>
          <!-- <a class="button is-large is-primary" @click="authenticate">Login</a>
          <a class="button is-large is-success" @click="register">Register</a> -->
        </div>
      </div>
    </section>

    <v-dialog
      transition="dialog-top-transition"
      max-width="600"
      v-model="errorDialog"
    >
      <v-card>
        <v-toolbar color="red" dark>Error</v-toolbar>
        <v-card-text>
          <div class="text-h5 pa-12">Invalid login or password!</div>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn text @click="errorDialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import { EventBus } from "@/utils";

export default {
  data() {
    return {
      email: "",
      password: "",
      errorMsg: "",
      errorDialog: false,
    };
  },
  methods: {
    authenticate() {
      this.$store
        .dispatch("login", { email: this.email, password: this.password })
        .then(() => this.$router.push("/dashboard/bottom-up"))
        .catch((err) => (this.errorDialog = true));
    },
    register() {
      this.$store
        .dispatch("register", { email: this.email, password: this.password })
        .then(() => this.authenticate())
        .catch((err) => (this.errorDialog = true));
    },
  },
  mounted() {
    // EventBus.$on("failedRegistering", (msg) => {
    //   this.errorDialog = true;
    //   this.errorMsg = msg;
    // });
    // EventBus.$on("failedAuthentication", (msg) => {
    //   this.errorDialog = true;
    //   this.errorMsg = msg;
    // });
  },
  beforeDestroy() {
    // EventBus.$off("failedRegistering");
    // EventBus.$off("failedAuthentication");
  },
};
</script>

<style>
.body {
  width: 100%;
  display: grid;
  justify-content: center;
}

.control {
  display: flex;
  justify-content: center;
}

.title {
  display: flex;
  justify-content: center;
}
</style>
