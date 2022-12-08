<template>
    <div>
        <v-btn
        elevation="2"
        @click="savePlot()"
        >Save Plot</v-btn>

        <v-btn
            :disabled="dialog"
            :loading="dialog"
            class="white--text"
            color="purple darken-2"
            @click="dialog = true; resetPlatform()"
            >
            Reset Platform
            </v-btn>
            <v-dialog
            v-model="dialog"
            hide-overlay
            persistent
            width="300"
            >
            <v-card
                color="primary"
                dark
            >
                <v-card-text>
                Reseting platform...
                <v-progress-linear
                    indeterminate
                    color="white"
                    class="mb-0"
                ></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import axios from 'axios';

  export default {
    data: () => ({
        dialog: false,
    }),
    methods: {
        resetPlatform() {
            const path_reset = `${process.env.VUE_APP_BASE_URL}/database/reset`;
            const path_processing = `${process.env.VUE_APP_BASE_URL}/database/process`;
            axios.get(path_reset)
                .then((res) => {
                    axios.get(path_processing)
                        .then((res) => {                            
                            console.log('Plataform reseted successfully!')
                            this.dialog = false
                        })
                        .catch((error) => {
                            console.error(error);
                            this.dialog = false
                        });

                })
                .catch((error) => {
                    console.error(error);
                    this.dialog = false
                });
        },
        savePlot() {
            const path_reset = `${process.env.VUE_APP_BASE_URL}/database/saveplot`;
            axios.get(path_reset)
                .then((res) => {
                    console.log('Saved Plot!')
                })
                .catch((error) => {
                    console.error(error);
                    this.dialog = false
                });
        }
    }
}
</script>
