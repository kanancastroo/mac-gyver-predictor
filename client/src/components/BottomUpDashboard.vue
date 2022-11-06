<template>
    <div class="dashboard">
        <div class="panel">
            <v-chip
                class="ma-2"
                color="primary"
                v-bind:id="sos.sos_external_id"
                v-for="(sos, index) in sos" :key="index"
                @click="getConstituents(sos.sos_external_id)">
                    {{ sos.sos_name }}
                </v-chip>
        </div>
        <div class="panel">
            <v-chip
                class="ma-2"
                color="secondary"
                v-bind:id="constituents.constituent_external_id"
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
                id="Test"
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
import LeaderLine from 'leader-line-new';

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
            const path = `${process.env.VUE_APP_BASE_URL}/sos/get`;
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
            const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos}/constituents/get`;
            axios.get(path)
                .then((res) => {
                    this.constituents = res.data;
                    
                    this.constituents.forEach(constituent => {
                        // console.log(constituent.constituent_external_id, constituent.constituent_name)
                        // var startElement = document.getElementById(sos)
                        // var endElement = document.getElementById("Test");
                        // console.log(startElement, endElement)
                        // new LeaderLine(startElement, endElement, {
                        //     color: 'red', 
                        //     size: 3,
                        //     middleLabel: 'DROP',
                        //     startPlug: 'disc',
                        //     endPlug: 'disc',
                        // });
                    })
                    let sos_list = []
                    sos_list.push(sos)

                    let constituent_list = []
                    this.constituents.forEach(constituent => constituent_list.push(constituent.constituent_external_id))

                    console.log(sos_list)
                    console.log(constituent_list) 
                    
                    const relations_path = `${process.env.VUE_APP_BASE_URL}/relation/sos_constituent/get`;
                    axios.get(relations_path, {params: {
                        sos_list: sos_list.reduce((f, s) => `${f},${s}`), 
                        constituent_list: constituent_list.reduce((f, s) => `${f},${s}`)
                        }})
                        .then((res) => {
                            console.log(res.data)
                        })
                        .catch((error) => {
                            console.error(error);
                        });
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