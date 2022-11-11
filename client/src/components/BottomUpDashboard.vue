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
            <div class="text-center">
                <v-btn
                :disabled="dialog"
                :loading="dialog"
                class="white--text"
                color="purple darken-2"
                @click="dialog = true; saveSoS()"
                >
                Save SoS
                </v-btn>
                <v-dialog
                v-model="dialog"
                hide-overlay
                persistent
                width="300"
                >
                <v-card
                    color="red"
                    dark
                >
                    <v-card-text>
                    Saving new SoS...
                    <v-progress-linear
                        indeterminate
                        color="white"
                        class="mb-0"
                    ></v-progress-linear>
                    </v-card-text>
                </v-card>
                </v-dialog>
            </div>

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
                    {{ prediction.description }}
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
        featuresFromChosenConstituents: [],
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
        saveSoS() {
            const path_addSoS = `${process.env.VUE_APP_BASE_URL}/sos/add`;
            console.log(path_addSoS)
            let sos_name = 'Seinfeld'
            axios.get(path_addSoS, {params: {sos_name: sos_name}})
                .then(async res => {
                    let sos_external_id = res.data
                    console.log(sos_external_id)

                    const path_addRelationSoSConstituent = `${process.env.VUE_APP_BASE_URL}/relation/sos_constituent/add`;
                    console.log(path_addRelationSoSConstituent)
                    let promises = []
                    for (let i=0; i < this.composedSoS.length; i++) {
                        promises.push(
                            axios.get(path_addRelationSoSConstituent, {params: {sos_external_id: sos_external_id, constituent_external_id:this.composedSoS[i].constituent_external_id}})
                            .then((res) => {
                                console.log(`Added relation between ${sos_name} and ${this.composedSoS[i].constituent_name}`)
                            })
                            .catch((error) => {
                                console.error('ERROR ON ADD RELATION SOS/CONSTITUENT =>>> ', error);
                                this.dialog = false
                            })
                        )
                    }

                    await Promise.all(promises)
                    console.log('Relations SoS/Constituent added Successfully. Now adding relations Basic Features/Emergent Behaviors...')

                    let payload = {
                        basic_features_list: this.featuresFromChosenConstituents,
                        emergent_behaviors_list: this.predictions
                    }
                    const path_addRelationsFeaturesBehaviors = `${process.env.VUE_APP_BASE_URL}/relation/basic_feature_emergent_behavior/add`;
                    axios({
                        url: path_addRelationsFeaturesBehaviors,
                        method: 'post',
                        data: payload
                        })
                        .then((res) => {
                            // your action after success
                            // this.dialog = false
                            console.log('Relations Basic Features/Emergent Behaviors added Successfully. Now adding relations SoS/Emergent Behaviors...')
                            let payload_final = {
                                sos_external_id: sos_external_id,
                                emergent_behaviors_list: this.predictions
                            }
                            const path_addRelationsSoSBehaviors = `${process.env.VUE_APP_BASE_URL}/relation/sos_emergent_behavior/add`;
                            axios({
                                url: path_addRelationsSoSBehaviors,
                                method: 'post',
                                data: payload_final
                                })
                                .then((res) => {
                                    // your action after success
                                    // this.dialog = false
                                    console.log('PROCESS FINISHED!!!')
                                    this.dialog = false
                                })
                                .catch((error) => {
                                // your action on error success
                                    console.log('ERROR ON ADD RELATION FEATURES/BEHAVIORS =>>> ', error);
                                    this.dialog = false
                                });
                        })
                        .catch((error) => {
                        // your action on error success
                            console.log('ERROR ON ADD RELATION FEATURES/BEHAVIORS =>>> ', error);
                            this.dialog = false
                        });
                })
                .catch((error) => {
                    this.dialog = false
                    console.error('ERROR ON ADD SOS =>>> ', error);
                });
        },
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
                    // this.dialog = false
                    console.log(this.predictions)

                    const featuresPath = `${process.env.VUE_APP_BASE_URL}/constituents/basic_features/post`
                    axios({
                        url: featuresPath,
                        method: 'post',
                        data: payload
                        })
                        .then((res) => {
                            // your action after success
                            this.featuresFromChosenConstituents = res.data
                            console.log('BASIC FEATURES:')
                            console.log(this.featuresFromChosenConstituents)
                            this.dialog = false
                        })
                        .catch((error) => {
                        // your action on error success
                            this.dialog = false
                            console.log(error);
                        });
                })
                .catch((error) => {
                // your action on error success
                    console.log(error);
                });
        },
        addConstituent(constituent){
            this.composedSoS.push(constituent)
            console.log(this.composedSoS)
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