<template>
    <div class="dashboard">
        <div class="panel">
            <v-chip
                class="ma-2"
                color="primary"
                ref="sos"
                v-for="(sos, index) in sos" :key="index"
                @click="getConstituents(sos.sos_external_id, $refs.sos[index])">
                    {{ sos.sos_name }}
                </v-chip>
        </div>
        <div class="panel">
            <v-chip
                class="ma-2"
                color="secondary"
                ref="constituents"
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

            <div class="text-center">
                <v-btn
                :disabled="dialog"
                :loading="dialog"
                class="white--text"
                color="purple darken-2"
                @click="dialog = true; predict()"
                >
                Predict
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
                    Processing predictions...
                    <v-progress-linear
                        indeterminate
                        color="white"
                        class="mb-0"
                    ></v-progress-linear>
                    </v-card-text>
                </v-card>
                </v-dialog>
            </div>

            <!-- <v-btn
                color="primary"
                id="Test"
                @click="predict()"
            >Predict!</v-btn> -->

            <v-chip
                class="ma-2"
                close
                v-for="(prediction, index) in predictions" :key="index"
                @click:close="removePrediction(index)">
                    {{ prediction }}
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
        predictions: [],
        SoSLines: [],
        dialog: false,
    }),
    watch: {
      dialog (val) {
        if (!val) return

        // setTimeout(() => (this.dialog = false), 4000)
      },
    },
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
        getConstituents(id, el) {
            this.constituents = []
            // this.SoSLines.forEach(line => line.remove())
            // this.SoSLines = []
            const path = `${process.env.VUE_APP_BASE_URL}/sos/${id}/constituents/get`;
            axios.get(path)
                .then((res) => {
                    this.constituents = res.data;
                    // console.log(this.$refs.constituents)
                    // this.$nextTick(() => {
                    //     this.$refs.constituents.forEach(constituent => {
                    //     // var startElement = document.getElementById(sos);
                    //     // var endElement = document.getElementById(constituent);
                    //     console.log(el, constituent)
                    //     const line = new LeaderLine(el.$el, constituent.$el, {
                    //         color: 'red', 
                    //         size: 3,
                    //         startPlug: 'disc',
                    //         endPlug: 'disc',
                    //     });

                    //     this.SoSLines.push(line)
                    // })
                // })

                    // let sos_list = []
                    // sos_list.push(sos)

                    // let constituent_list = []
                    // this.constituents.forEach(constituent => constituent_list.push(constituent.constituent_external_id))

                    // console.log(sos_list)
                    // console.log(constituent_list) 
                    
                    // const relations_path = `${process.env.VUE_APP_BASE_URL}/relation/sos_constituent/get`;
                    // axios.get(relations_path, {params: {
                    //     sos_list: sos_list.reduce((f, s) => `${f},${s}`), 
                    //     constituent_list: constituent_list.reduce((f, s) => `${f},${s}`)
                    //     }})
                    //     .then((res) => {
                    //         console.log(res.data)
                    //     })
                    //     .catch((error) => {
                    //         console.error(error);
                    //     });
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        preProcessDatabase() {
            const path = `${process.env.VUE_APP_BASE_URL}/database/process`;
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
            // console.log(this.composedSoS)
            // let constituents_elements = this.composedSoS.map(constituent => {return constituent.constituent_name})
            // console.log(constituents_elements)
            // let constituents_elements = this.composedSoS[0].toString()
            // for (let i=1; i < this.composedSoS.length - 1; i++){
            //     constituents_elements.concat(',',this.composedSoS[i])
            // }
            // constituents_elements.concat(',',this.composedSoS[this.composedSoS.length])
            // console.log(constituents_elements)
            let payload = {
                constituent_list: this.composedSoS
            }
            axios({
                url: path,
                method: 'post',
                data: payload
                })
                .then((res) => {
                    // your action after success
                    this.predictions = res.data
                    this.dialog = false
                    console.log(this.predictions)
                })
                .catch((error) => {
                // your action on error success
                    console.log(error);
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