<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">Login or Register</h2>
          <p class="subtitle error-msg">{{ errorMsg }}</p>
        </div>
      </div>
    </section>
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
          <v-btn
            elevation="2"
            @click="authenticate"
          >Login</v-btn>
          <v-btn
            elevation="2"
            @click="register"
          >Register</v-btn>
          <!-- <a class="button is-large is-primary" @click="authenticate">Login</a>
          <a class="button is-large is-success" @click="register">Register</a> -->
        </div>
      </div>
    </section>
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
    };
  },
  methods: {
    authenticate() {
      this.$store
        .dispatch("login", { email: this.email, password: this.password })
        .then(() => this.$router.push("/dashboard/bottom-up"))
    },
    register() {
      this.$store
        .dispatch("register", { email: this.email, password: this.password })
        .then(() => this.$router.push("/dashboard/bottom-up"))
    },
  },
  mounted() {
    EventBus.$on("failedRegistering", (msg) => {
      this.errorMsg = msg;
    });
    EventBus.$on("failedAuthentication", (msg) => {
      this.errorMsg = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off("failedRegistering");
    EventBus.$off("failedAuthentication");
  },
};
</script>


<style>


</style>