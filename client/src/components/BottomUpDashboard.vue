<template>
    <div class="dashboard">
        <div class="panel">
            <v-chip
                class="ma-2"
                color="primary"
                v-for="(sos, index) in sos" :key="index"
                @click="getConstituents(sos.sos_id)">
                    {{ sos.sos_name }}
                </v-chip>
        </div>
        <div class="panel">
            <v-chip
                class="ma-2"
                color="secondary"
                v-for="(constituent, index) in constituents" :key="index"
                @click="addConstituent(constituent)">
                    {{ constituent.constituent_name }}
            </v-chip>
        </div>
        <div class="panel">
            <v-chip
                class="ma-2"
                close
                v-for="(constituent, index) in composedSoS" :key="index"
                @click:close="removeConstituent(index)">
                    {{ constituent.constituent_name }}
            </v-chip>
        </div>
        <div class="panel">
            <v-btn
                color="primary"
                @click="preProcessDatabase()"
            >{{ this.message }}</v-btn>

            <v-btn
                color="primary"
                @click="predict()"
            >Predict!</v-btn>

            <v-chip
                class="ma-2"
                close
                v-for="(predictions, index) in predictions" :key="index"
                @click:close="removePrediction(index)">
                    {{ predictions }}
            </v-chip>
        </div>


    </div>

</template>

<script>
import axios from 'axios';

  export default {
    data: () => ({
        sos: [],
        constituents: [],
        composedSoS: [],
        message: 'Train Model',
        predictions: []
    }),
    methods: {
        closeDialog() {
            this.dialog = false;
        },
        getSoS() {
            const path = `${process.env.VUE_APP_BASE_URL}/list_all_sos`;
            console.log(path)
            axios.get(path)
                .then((res) => {
                    this.sos = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
            },
        getConstituents(sos) {
            this.constituents = []
            const path = `${process.env.VUE_APP_BASE_URL}/list_constituents_from_sos?sos_id=[${sos}]`;
            axios.get(path)
                .then((res) => {
                    this.constituents = res.data;
                    console.log(constituents)
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        preProcessDatabase() {
            const path = `${process.env.VUE_APP_BASE_URL}/pre_process_database`;
            axios.get(path)
                .then((res) => {
                    this.message = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        predict() {
            const path = `${process.env.VUE_APP_BASE_URL}/predict`;
            axios.get(path)
                .then((res) => {
                    this.predictions = res.data;
                    console.log(this.predictions)
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        addConstituent(constituent){
            this.composedSoS.push(constituent)
        },
        removeConstituent(index){
            this.composedSoS.splice(index, 1)
        },
        removePrediction(index){
            this.predictions.splice(index, 1)
        }
    },
    created() {
        this.getSoS();
    }
  }
</script>

<style>
.dashboard {
    padding: 5px;
    display: grid;
    grid-template-columns: repeat(4, minmax(25%, 1fr));
    gap: 5px;
}

.dashboard div {
    background-color: white;
}

.panel {
    align-items: center;
    display: flex;
    gap: 2px;
    flex-direction: column;
}

.btn-multiline > span {
    width: 100%;
}

.v-chip.v-size--default {
    height: auto !important;
    min-height: 32px;
}

.v-chip {
    white-space: normal !important;
}
</style>