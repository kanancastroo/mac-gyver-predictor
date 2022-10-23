<template>
    <div>
        <v-btn color="primary" v-for="(constituent, index) in constituents" :key="index">
            {{ constituent.constituent_name }}
        </v-btn>
    </div>
</template>

<script>
import axios from 'axios';

  export default {
    data: () => ({
        constituents: []
    }),
    methods: {
        getSoS() {
            const path = 'http://localhost:5000/list_constituents';
            axios.get(path)
                .then((res) => {
                    this.constituents = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
            }
    },
    created() {
        this.getSoS();
    }
  }
</script>