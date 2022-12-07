<template>
    <div class="dashboard">
        <div class="panel">
            <div class="title">SoS</div>
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
            <div class="title">Constituents</div>
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
            <div class="title">Dashboard</div>
            <div class="composedSoSPanel">
                <v-chip
                    class="ma-2"
                    close
                    v-for="(constituent, index) in composedSoS" :key="index"
                    @click:close="removeConstituent(index)">
                        {{ constituent.constituent_name }}
                </v-chip>
            </div>

            <div class="text-center">
                <!-- <v-btn
                :disabled="saveDialog"
                :loading="saveDialog"
                class="white--text"
                color="purple darken-2"
                @click="saveDialog = true; saveSoS()"
                >
                Save SoS
                </v-btn> -->
                <v-row justify="center">
                <v-dialog
                v-model="addSoSDialog"
                persistent
                max-width="600px"
                >
                <template v-slot:activator="{ on, attrs }">
                    <v-btn
                    color="primary"
                    dark
                    v-bind="attrs"
                    v-on="on"
                    >
                    Save SoS
                    </v-btn>
                </template>
                    <v-card>
                        <v-card-title>
                        <span class="text-h5">New SoS name</span>
                        </v-card-title>
                        <small>Type a name for the new SoS:</small>                        
                        <v-card-text>
                        <v-container>
                            <v-row>
                            <v-col cols="12">
                                <v-text-field
                                v-model="sosName"
                                label=""
                                ></v-text-field>
                            </v-col>
                            </v-row>
                        </v-container>
                        </v-card-text>
                        <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="addSoSDialog = false"
                        >
                            Cancel
                        </v-btn>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="addSoSDialog = false; saveSoS(sosName)"
                        >
                            Save
                        </v-btn>
                        </v-card-actions>
                    </v-card>
                    </v-dialog>
                </v-row>
                <v-dialog
                v-model="saveDialog"
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
        </div>
        <div class="panel">
            <div class="title">Emergent Behaviors</div> 
            <div class="text">Known:</div>
            <div class="behaviors">
                <v-chip
                    class="ma-2"
                    close
                    v-for="(behavior, index) in knownBehaviors" :key="index"
                    @click:close="removeKnownBehavior(index)">
                        {{ behavior.description }}
                </v-chip>
            </div>
            <v-btn
                elevation="2" @click="showKnownEmergentBehaviors()"
            >Show</v-btn>
            <div class="text">Predicted:</div>
            <div class="behaviors">
                <v-chip
                    class="ma-2"
                    close
                    v-for="(prediction, index) in predictions" :key="index"
                    @click:close="removePrediction(index)">
                        {{ prediction.description }}
                </v-chip>
            </div>
            <div class="text-center">
                <v-btn
                :disabled="predictDialog"
                :loading="predictDialog"
                class="white--text"
                color="purple darken-2"
                @click="predictDialog = true; predict()"
                >
                Predict
                </v-btn>
                <v-dialog
                v-model="predictDialog"
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
            <div class="text">Observed:</div>
            <div class="behaviors">
                <v-chip
                    class="ma-2"
                    close
                    v-for="(behavior, index) in observedBehaviors" :key="index"
                    @click:close="removeObservedBehavior(index)">
                        {{ behavior.description }}
                </v-chip>
            </div>
            <v-row justify="center">
                <v-dialog
                v-model="behaviorDialog"
                persistent
                max-width="600px"
                >
                <template v-slot:activator="{ on, attrs }">
                    <v-btn
                    color="primary"
                    dark
                    v-bind="attrs"
                    v-on="on"
                    >
                    Add
                    </v-btn>
                </template>
                <v-card>
                    <v-card-title>
                    <span class="text-h5">Emergent Behavior</span>
                    <small>Pick one from the list or type a new behavior in the textbox</small>
                    </v-card-title>
                    <v-card-text>
                    <v-container>
                        <v-row>
                        <v-col
                            cols="12"
                            sm="12"
                        >
                            <v-select
                            :items="this.emergentBehaviors"
                            item-text="description"
                            label="Pick an emergent behavior"
                            v-model="selectedBehavior"
                            return-object
                            ></v-select>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                            v-model="insertedBehavior"
                            label="...or type a new one here"
                            ></v-text-field>
                        </v-col>
                        </v-row>
                    </v-container>
                    </v-card-text>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        color="blue darken-1"
                        text
                        @click="behaviorDialog = false"
                    >
                        Cancel
                    </v-btn>
                    <v-btn
                        color="blue darken-1"
                        text
                        @click="behaviorDialog = false; addObservedBehavior(selectedBehavior, insertedBehavior)"
                    >
                        Add
                    </v-btn>
                    </v-card-actions>
                </v-card>
                </v-dialog>
            </v-row>
        </div>


    </div>

</template>

<script>
import axios from 'axios';
import {v4 as uuidv4} from 'uuid';
// import LeaderLine from 'leader-line-new';

  export default {
    data: () => ({
        sos: [],
        constituents: [],
        composedSoS: [],
        featuresFromChosenConstituents: [],
        message: 'Train Model',
        predictions: [],
        knownBehaviors: [],
        observedBehaviors: [],
        SoSLines: [],
        emergentBehaviors: [],
        selectedBehavior: null,
        insertedBehavior: null,
        predictDialog: false,
        saveDialog: false,
        behaviorDialog: false,
        addSoSDialog: false,
        sosName: 'Unnamed SoS'
    }),
    watch: {
        predictDialog (val) {
            if (!val) return

            // setTimeout(() => (this.dialog = false), 4000)
        },
        saveDialog (val) {
            if (!val) return

            // setTimeout(() => (this.dialog = false), 4000)
        },
        behaviorDialog (val) {
            if (!val) return

            // setTimeout(() => (this.dialog = false), 4000)
        },
        addSoSDialog (val) {
            if (!val) return

            // setTimeout(() => (this.dialog = false), 4000)
        },
    },
    methods: {
        addObservedBehavior(selectedBehavior, insertedBehavior) {
            // console.log('selectedBehavior: ', selectedBehavior)
            // console.log('insertedBehavior: ', insertedBehavior)
            if (insertedBehavior) {
                const addBehavior = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/add`;
                axios.get(addBehavior, {params: {description: insertedBehavior}})
                    .then(res => {
                        let newBehavior = {}
                        newBehavior.emergent_external_id = res.data
                        newBehavior.description = insertedBehavior
                        this.observedBehaviors.push(newBehavior)
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            } else {
                this.observedBehaviors.push(selectedBehavior)
            }
        },
        showKnownEmergentBehaviors() {
            const path = `${process.env.VUE_APP_BASE_URL}/constituents/basic_features/emergent_behaviors/post`;
            let payload = {
                        constituent_list: this.composedSoS,
                    }    
            axios({
                    url: path,
                    method: 'post',
                    data: payload
                    })
                    .then((res) => {
                        this.knownBehaviors = res.data
                    })
                    .catch((error) => {
                        console.error('ERROR ON SHOW KNOWN EMERGENT BEHAVIORS =>>> ', error);
                    })
        },
        getAllEmergentBehaviors() {
            const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/get`;
            axios.get(path)
                .then((res) => {
                    this.emergentBehaviors = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        saveSoS(sosName) {
            this.saveDialog = true
            const path_addSoS = `${process.env.VUE_APP_BASE_URL}/sos/add`;
            console.log(path_addSoS)
            let sos_name = sosName
            let sos_external_id = uuidv4()
            axios.get(path_addSoS, {params: {sos_name: sos_name, sos_id: sos_external_id}})
                .then(async res => {
                    console.log(res.data)

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
                                this.saveDialog = false
                            })
                        )
                    }

                    await Promise.all(promises)
                    console.log('Relations SoS/Constituent added Successfully. Now adding relations Basic Features/Emergent Behaviors...')

                    console.log('Executing addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.predictions)')
                    this.addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.predictions).then(result => {
                        console.log('Executing addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.knownBehaviors)')
                        this.addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.knownBehaviors).then(result => {
                            console.log('Executing addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.observedBehaviors)')
                            this.addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.observedBehaviors).then(result => {
                                console.log('Executing updateModel()')
                                this.updateModel().then(result => console.log('DONE!'))
                            })
                        })
                    })
                    
                })
                .catch((error) => {
                    this.saveDialog = false
                    console.error('ERROR ON ADD SOS =>>> ', error);
                });
        },
        updateModel() {
            const path_processing = `${process.env.VUE_APP_BASE_URL}/database/process`;
            return new Promise((resolve, reject) => {
                axios.get(path_processing)
                    .then((res) => {                          
                        console.log('Model updated successfully!')
                        this.saveDialog = false
                        resolve()
                    })
                    .catch((error) => {
                        console.error(error);
                        this.saveDialog = false
                    });
            })
        },
        addRelationBasicFeaturesEmergentBehaviors(sos_external_id, behaviorsList) {
            console.log('sos_external_id =>>> ', sos_external_id)
            let payload = {
                        basic_features_list: this.featuresFromChosenConstituents,
                        emergent_behaviors_list: behaviorsList
                    }
            const path_addRelationsFeaturesBehaviors = `${process.env.VUE_APP_BASE_URL}/relation/basic_feature_emergent_behavior/add`;
            return new Promise((resolve, reject) => {
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
                            emergent_behaviors_list: behaviorsList
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
                                console.log('SUBPROCESS FINISHED!!!')
                                resolve()
                            })
                            .catch((error) => {
                            // your action on error success
                                console.log('ERROR ON ADD RELATION SoS/BEHAVIORS =>>> ', error);
                                this.saveDialog = false
                            });
                    })
                    .catch((error) => {
                    // your action on error success
                        console.log('ERROR ON ADD RELATION FEATURES/BEHAVIORS =>>> ', error);
                        this.saveDialog = false
                    });
            })
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
                            this.predictDialog = false
                        })
                        .catch((error) => {
                        // your action on error success
                            this.predictDialog = false
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
        },
        removeKnownBehavior(index){
            this.knownBehaviors.splice(index, 1)
        },
        removeObservedBehavior(index){
            this.observedBehaviors.splice(index, 1)
        }
    },
    created() {
        this.getSoS();
        this.getAllEmergentBehaviors();
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

.composedSoSPanel {
    min-height: 90%;
}

.behaviors {
    min-height: 100px;
    width: 90%;
    border-color: black;
    border-style: solid;
    border-width: 1px;
}

.row {
    margin: 0 !important;
}

#observed {
    width: 90%;
    border-color: black;
    border-style: solid;
    border-width: 1px;
}
</style>