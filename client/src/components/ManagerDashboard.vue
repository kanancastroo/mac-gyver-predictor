<template>
    <div class="dashboard">
        <div class="panel">
            <div class="title">SoS</div>
            <v-col
                class="d-flex"
                cols="12"
                sm="10"
            >
                <v-select
                :items="this.sos"
                item-text="sos_name"
                label="Pick a SoS"
                v-model="selectedSoS"
                ref="sos"
                @change="loadSoS(selectedSoS.sos_external_id)"
                dense
                return-object
                ></v-select>
            </v-col>
        </div>
        <div class="panel">
            <div class="title">Constituents</div>
            <v-chip
                    class="ma-2"
                    :color="selectedConstituents.includes(constituent.constituent_external_id) ? 'error' : 'primary'"
                    close
                    ref="constituents"
                    v-for="(constituent, index) in constituents" :key="index" :id="constituent.constituent_external_id"
                    @click:close="removeConstituent(index)" @click="handleColorConstituents(constituent)">
                        {{ constituent.constituent_name }}
            </v-chip>
        </div>
        <div class="panel">
            <div class="title">Basic Features</div>
            <v-chip
                    class="ma-2"
                    :color="selectedFeatures.includes(feature.feature_external_id) ? 'error' : 'primary'"
                    close
                    ref="basicFeatures"
                    v-for="(feature, index) in basicFeatures" :key="index" :id="feature.feature_external_id"
                    @click:close="removeBasicFeature(index)" @click="handleColorBasicFeatures(feature)">
                        {{ feature.description }}
            </v-chip>
        </div>
        <div class="panel">
            <div class="title">Emergent Behaviors</div> 
            <v-chip
                    class="ma-2"
                    :color="selectedBehaviors.includes(behavior.emergent_external_id) ? 'error' : 'primary'"
                    close
                    ref="emergentBehaviors"
                    v-for="(behavior, index) in emergentBehaviors" :key="index" :id="behavior.emergent_external_id"
                    @click:close="removeEmergentBehavior(index)" @click="handleColorEmergentBehaviors(behavior)">
                        {{ behavior.description }}
            </v-chip>
        </div>

        <div class="text-center">
            <v-dialog
            v-model="dialog"
            width="500"
            >
            <v-card>
                <v-card-title class="text-h5 grey lighten-2">
                Forbidden action
                </v-card-title>

                <v-card-text>
                An invalid action was detected!
                </v-card-text>

                <v-divider></v-divider>

                <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="primary"
                    text
                    @click="dialog = false"
                >
                    OK
                </v-btn>
                </v-card-actions>
            </v-card>
            </v-dialog>
        </div>
    </div>

</template>

<script>
import axios from 'axios';
import LeaderLine from 'leader-line-new';
import {v4 as uuidv4} from 'uuid';

  export default {
    data: () => ({
        sos: [],
        constituents: [],
        basicFeatures: [],
        emergentBehaviors: [],
        ConstituentsBasicFeaturesLines: [],
        BasicFeaturesEmergentBehaviorsLines: [],
        selectedSoS: null,
        selectedConstituents: [],
        selectedFeatures: [],
        selectedBehaviors: [],
        selectedForCheck: [],
        dialog: false
    }),
    created() {
        this.clearAll();
        this.getSoS();
    },
    methods: {
        checkConnection() {
            if (this.selectedForCheck.length > 2) {
                this.dialog = true
                this.selectedForCheck = []
                this.selectedConstituents = []
                this.selectedFeatures = []
                this.selectedBehaviors = []
            } else if (this.selectedForCheck.length == 2) {
                if (this.selectedForCheck[0].type == 'constituent') {
                    if (this.selectedForCheck[1].type == 'emergentBehavior') {
                        this.dialog = true
                        this.selectedForCheck = []
                        this.selectedConstituents = []
                        this.selectedFeatures = []
                        this.selectedBehaviors = []
                    } else {
                        let connection = this.ConstituentsBasicFeaturesLines.filter(lineObj => {
                            return (lineObj.constituent_external_id == this.selectedForCheck[0].constituent_external_id
                             && lineObj.feature_external_id == this.selectedForCheck[1].feature_external_id)
                        })

                        // console.log('connection =>>> ', connection)
                        
                        if (connection.length == 0) {
                            // console.log('connection is ZERO')
                            let constituent = this.$refs.constituents.find(constituent => {   
                                // console.log(constituent)                         
                                return constituent.$attrs.id == this.selectedForCheck[0].constituent_external_id
                            })

                            let basicFeature = this.$refs.basicFeatures.find(basicFeature => {     
                                // console.log(basicFeature)                       
                                return basicFeature.$attrs.id == this.selectedForCheck[1].feature_external_id
                            })
                        
                            const line = new LeaderLine(LeaderLine.mouseHoverAnchor(constituent.$el), basicFeature.$el, {
                                size: 3,
                                color: 'red',
                                startPlug: 'disc',
                                endPlug: 'disc',
                                path: 'straight'                            
                            });

                            let lineObj = {}
                            lineObj.constituent_external_id = this.selectedForCheck[0].constituent_external_id
                            lineObj.feature_external_id = this.selectedForCheck[1].feature_external_id
                            lineObj.line = line

                            //AVALIAR PARA ADICIONAR EM OUTRO ARRAY
                            this.ConstituentsBasicFeaturesLines.push(lineObj)
                        } else if (connection.length == 1) {
                            // console.log('connection is ONE')
                            // let element = this.ConstituentsBasicFeaturesLines.filter(el => {
                            //     return (el.constituent_external_id == connection[0].constituent_external_id
                            //     && el.feature_external_id == connection[0].feature_external_id)
                            // })

                            // console.log('element =>>> ', element)
                            // element.line = connection[0].line

                            connection[0].line.remove()
                            // console.log(this.ConstituentsBasicFeaturesLines)
                            // console.log(this.ConstituentsBasicFeaturesLines.length)
                            this.ConstituentsBasicFeaturesLines.splice(this.ConstituentsBasicFeaturesLines.indexOf(connection[0]), 1)
                            // console.log(this.ConstituentsBasicFeaturesLines)
                            // console.log(this.ConstituentsBasicFeaturesLines.length)
                        } else {
                            this.dialog = true
                        }

                        this.selectedForCheck = []
                        this.selectedConstituents = []
                        this.selectedFeatures = []
                        this.selectedBehaviors = []
                    }
                } else if (this.selectedForCheck[0].type == 'emergentBehavior') {
                    if (this.selectedForCheck[1].type == 'constituent') {
                        this.dialog = true
                        this.selectedForCheck = []
                        this.selectedConstituents = []
                        this.selectedFeatures = []
                        this.selectedBehaviors = []
                    } else {
                        let connection = this.BasicFeaturesEmergentBehaviorsLines.filter(lineObj => {
                            return (lineObj.emergent_external_id == this.selectedForCheck[0].emergent_external_id
                             && lineObj.feature_external_id == this.selectedForCheck[1].feature_external_id)
                        })

                        if (connection.length == 0) {
                            // console.log('connection is ZERO')

                            let emergentBehavior = this.$refs.emergentBehaviors.find(emergentBehavior => {     
                                // console.log(basicFeature)                       
                                return emergentBehavior.$attrs.id == this.selectedForCheck[0].emergent_external_id
                            })

                            let basicFeature = this.$refs.basicFeatures.find(basicFeature => {     
                                // console.log(basicFeature)                       
                                return basicFeature.$attrs.id == this.selectedForCheck[1].feature_external_id
                            })
                        
                            const line = new LeaderLine(LeaderLine.mouseHoverAnchor(basicFeature.$el), emergentBehavior.$el, {
                                size: 3,
                                color: 'red',
                                startPlug: 'disc',
                                endPlug: 'disc',
                                path: 'straight'                            
                            });

                            let lineObj = {}
                            lineObj.emergent_external_id = this.selectedForCheck[0].emergent_external_id
                            lineObj.feature_external_id = this.selectedForCheck[1].feature_external_id
                            lineObj.line = line

                            //AVALIAR PARA ADICIONAR EM OUTRO ARRAY
                            this.BasicFeaturesEmergentBehaviorsLines.push(lineObj)
                        } else if (connection.length == 1) {
                            connection[0].line.remove()
                            this.BasicFeaturesEmergentBehaviorsLines.splice(this.BasicFeaturesEmergentBehaviorsLines.indexOf(connection[0]), 1)
                        } else {
                            this.dialog = true
                        }

                        this.selectedForCheck = []
                        this.selectedConstituents = []
                        this.selectedFeatures = []
                        this.selectedBehaviors = []
                    }
                } else {
                    if (this.selectedForCheck[1].type == 'constituent') {
                        let connection = this.ConstituentsBasicFeaturesLines.filter(lineObj => {
                            return (lineObj.constituent_external_id == this.selectedForCheck[1].constituent_external_id
                             && lineObj.feature_external_id == this.selectedForCheck[0].feature_external_id)
                        })

                        // console.log('connection =>>> ', connection)
                        
                        if (connection.length == 0) {
                            // console.log('connection is ZERO')
                            let constituent = this.$refs.constituents.find(constituent => {   
                                // console.log(constituent)                         
                                return constituent.$attrs.id == this.selectedForCheck[1].constituent_external_id
                            })

                            let basicFeature = this.$refs.basicFeatures.find(basicFeature => {     
                                // console.log(basicFeature)                       
                                return basicFeature.$attrs.id == this.selectedForCheck[0].feature_external_id
                            })
                        
                            const line = new LeaderLine(LeaderLine.mouseHoverAnchor(constituent.$el), basicFeature.$el, {
                                size: 3,
                                color: 'red',
                                startPlug: 'disc',
                                endPlug: 'disc',
                                path: 'straight'                            
                            });

                            let lineObj = {}
                            lineObj.constituent_external_id = this.selectedForCheck[1].constituent_external_id
                            lineObj.feature_external_id = this.selectedForCheck[0].feature_external_id
                            lineObj.line = line

                            //AVALIAR PARA ADICIONAR EM OUTRO ARRAY
                            this.ConstituentsBasicFeaturesLines.push(lineObj)
                        } else if (connection.length == 1) {
                            // console.log('connection is ONE')
                            // let element = this.ConstituentsBasicFeaturesLines.filter(el => {
                            //     return (el.constituent_external_id == connection[0].constituent_external_id
                            //     && el.feature_external_id == connection[0].feature_external_id)
                            // })

                            // console.log('element =>>> ', element)
                            // element.line = connection[0].line

                            connection[0].line.remove()
                            // console.log(this.ConstituentsBasicFeaturesLines)
                            // console.log(this.ConstituentsBasicFeaturesLines.length)
                            this.ConstituentsBasicFeaturesLines.splice(this.ConstituentsBasicFeaturesLines.indexOf(connection[0]), 1)
                            // console.log(this.ConstituentsBasicFeaturesLines)
                            // console.log(this.ConstituentsBasicFeaturesLines.length)
                        } else {
                            this.dialog = true
                        }

                        this.selectedForCheck = []
                        this.selectedConstituents = []
                        this.selectedFeatures = []
                        this.selectedBehaviors = []
                    } else {
                        let connection = this.BasicFeaturesEmergentBehaviorsLines.filter(lineObj => {
                            return (lineObj.emergent_external_id == this.selectedForCheck[1].emergent_external_id
                             && lineObj.feature_external_id == this.selectedForCheck[0].feature_external_id)
                        })

                        if (connection.length == 0) {
                            // console.log('connection is ZERO')

                            let emergentBehavior = this.$refs.emergentBehaviors.find(emergentBehavior => {     
                                // console.log(basicFeature)                       
                                return emergentBehavior.$attrs.id == this.selectedForCheck[1].emergent_external_id
                            })

                            let basicFeature = this.$refs.basicFeatures.find(basicFeature => {     
                                // console.log(basicFeature)                       
                                return basicFeature.$attrs.id == this.selectedForCheck[0].feature_external_id
                            })
                        
                            const line = new LeaderLine(LeaderLine.mouseHoverAnchor(basicFeature.$el), emergentBehavior.$el, {
                                size: 3,
                                color: 'red',
                                startPlug: 'disc',
                                endPlug: 'disc',
                                path: 'straight'                            
                            });

                            let lineObj = {}
                            lineObj.emergent_external_id = this.selectedForCheck[1].emergent_external_id
                            lineObj.feature_external_id = this.selectedForCheck[0].feature_external_id
                            lineObj.line = line

                            //AVALIAR PARA ADICIONAR EM OUTRO ARRAY
                            this.BasicFeaturesEmergentBehaviorsLines.push(lineObj)
                        } else if (connection.length == 1) {
                            connection[0].line.remove()
                            this.BasicFeaturesEmergentBehaviorsLines.splice(this.BasicFeaturesEmergentBehaviorsLines.indexOf(connection[0]), 1)
                        } else {
                            this.dialog = true
                        }

                        this.selectedForCheck = []
                        this.selectedConstituents = []
                        this.selectedFeatures = []
                        this.selectedBehaviors = []
                    }                    
                }
            } else {
                // console.log(this.selectedForCheck)
                // console.log('waiting for more chips...')
            } 
        },
        handleColorConstituents(item) {
            const id = item.constituent_external_id
            if ((this.selectedConstituents.length == 1) && (this.selectedConstituents[0] !== id)){
                this.dialog = true
                this.selectedForCheck = []
                this.selectedConstituents = []
                this.selectedFeatures = []
                this.selectedBehaviors = []
            } else {
                const el = this.selectedConstituents.findIndex(el => el === id);
                if (el < 0) {
                    // console.log(this.selectedConstituents)
                    this.selectedConstituents.push(id)
                    this.selectedForCheck.push(item)
                    this.checkConnection()
                } else {
                    // console.log(this.selectedConstituents)
                    this.selectedConstituents.splice(el, 1);
                    this.selectedForCheck.splice(item, 1);
                } 
            }
        },
        handleColorBasicFeatures(item) {
            const id = item.feature_external_id
            if ((this.selectedFeatures.length == 1) && (this.selectedFeatures[0] !== id)){
                this.dialog = true
                this.selectedForCheck = []
                this.selectedConstituents = []
                this.selectedFeatures = []
                this.selectedBehaviors = []
            } else {
                const el = this.selectedFeatures.findIndex(el => el === id);
                if (el < 0) {
                    // console.log(this.selectedFeatures)
                    this.selectedFeatures.push(id)
                    this.selectedForCheck.push(item)
                    this.checkConnection()
                } else {
                    // console.log(this.selectedFeatures)
                    this.selectedFeatures.splice(el, 1);
                    this.selectedForCheck.splice(item, 1);
                } 
            }
        },
        handleColorEmergentBehaviors(item) {
            const id = item.emergent_external_id
            if ((this.selectedBehaviors.length == 1) && (this.selectedBehaviors[0] !== id)){
                this.dialog = true
                this.selectedForCheck = []
                this.selectedConstituents = []
                this.selectedFeatures = []
                this.selectedBehaviors = []
            } else {
                const el = this.selectedBehaviors.findIndex(el => el === id);
                if (el < 0) {
                    // console.log(this.selectedBehaviors)
                    this.selectedBehaviors.push(id)
                    this.selectedForCheck.push(item)
                    this.checkConnection()
                } else {
                    // console.log(this.selectedBehaviors)
                    this.selectedBehaviors.splice(el, 1);
                    this.selectedForCheck.splice(item, 1);
                } 
            }
        },
        getSoS() {
            const path = `${process.env.VUE_APP_BASE_URL}/sos/get`;
            // console.log(path)
            axios.get(path)
                .then((res) => {
                    this.sos = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        getConstituentsFromSoS(sos_external_id, el) {
            this.ConstituentsBasicFeaturesLines.forEach(line => line.remove())
            this.ConstituentsBasicFeaturesLines = []
            this.BasicFeaturesEmergentBehaviorsLines = []
            const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/get`;
            // console.log(path, {params: {sos_external_id: sos_external_id}})
            
            return new Promise((resolve, reject) => {
                axios.get(path)
                    .then((res) => {
                        // console.log('Loaded constituents...')
                        this.constituents = res.data;

                        this.constituents.forEach(constituent => {
                            constituent.type = 'constituent'
                        })

                        resolve()
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                })
        },
        getBasicFeaturesFromSoS(sos_external_id) {
            this.ConstituentsBasicFeaturesLines.forEach(line => line.remove())
            this.ConstituentsBasicFeaturesLines = []
            this.BasicFeaturesEmergentBehaviorsLines = []
            const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/basic_features/get`;
            // console.log(path, {params: {sos_external_id: sos_external_id}})
            
            return new Promise((resolve, reject) => {
                axios.get(path)
                    .then((res) => {
                        this.basicFeatures = res.data;
                        // console.log('Loaded basic features...')

                        this.basicFeatures.forEach(basicFeature => {
                            basicFeature.type = 'basicFeature'
                        })
                        
                        this.$nextTick(() => {
                            // console.log(this.$refs.constituents)
                            // console.log(this.$refs.basicFeatures)
                            resolve()
                        })                       
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                })
        },               
        getEmergentBehaviorsFromSoS(sos_external_id) {
            this.BasicFeaturesEmergentBehaviorsLines.forEach(line => line.remove())
            this.ConstituentsBasicFeaturesLines = []
            this.BasicFeaturesEmergentBehaviorsLines = []
            const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/basic_features/emergent_behaviors/get`;
            // console.log(path, {params: {sos_external_id: sos_external_id}})
            
            return new Promise((resolve, reject) => {
                axios.get(path)
                    .then((res) => {
                        this.emergentBehaviors = res.data;
                        // console.log('Loaded emergent behaviors...')
                        
                        this.emergentBehaviors.forEach(emergentBehavior => {
                            emergentBehavior.type = 'emergentBehavior'
                        })

                        this.$nextTick(() => {
                            resolve()
                        })    
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                })
        },
        getRelationsConstituentsBasicFeatures() {
            let payload = {
                        constituent_list: this.constituents,
                        features_list: this.basicFeatures
                    }
            const path_addRelationsConstituentsBasicFeatures = `${process.env.VUE_APP_BASE_URL}/relation/constituent_basic_feature/post`;
            return new Promise((resolve, reject) => {
                axios({
                    url: path_addRelationsConstituentsBasicFeatures,
                    method: 'post',
                    data: payload
                    })
                    .then((res) => {
                        // console.log(res.data)
                        let relations = res.data
                        relations.forEach(relation => {
                        // var startElement = document.getElementById(sos);
                        // var endElement = document.getElementById(constituent);
                        let constituent = this.$refs.constituents.find(constituent => {   
                            // console.log(constituent)                         
                            return constituent.$attrs.id == relation.constituent_external_id
                        })

                        let basicFeature = this.$refs.basicFeatures.find(basicFeature => {     
                            // console.log(basicFeature)                       
                            return basicFeature.$attrs.id == relation.feature_external_id
                        })

                        // console.log('Constituent => ', constituent.$attrs.id, 'relation constituent id =>>> ', relation.constituent_external_id)
                        // console.log('Basic Feature => ', basicFeature.$attrs.id, 'relation feature id =>>> ', relation.feature_external_id)

                        const line = new LeaderLine(LeaderLine.mouseHoverAnchor(constituent.$el), basicFeature.$el, {
                            size: 3,
                            color: '#000000',
                            startPlug: 'disc',
                            endPlug: 'disc',
                            path: 'straight'                            
                        });

                        let lineObj = {}
                        lineObj.constituent_external_id = relation.constituent_external_id
                        lineObj.feature_external_id = relation.feature_external_id
                        lineObj.line = line

                        // let elmLine = document.querySelector('.leader-line:last-of-type')
                        // let myuuid = uuidv4();
                        // console.log('id =>>> ', myuuid)
                        
                        // elmLine.setAttribute('id', myuuid)

                        // constituent.$el.appendChild(elmLine);
                        
                        // constituent.$el.addEventListener('click', () => {
                        //     console.log(this.ConstituentsBasicFeaturesLines.find(line => line.endLabel == number.toString()))
                        //     let droppedLine = this.ConstituentsBasicFeaturesLines.find(line => line.endLabel == number.toString())
                        //     droppedLine.remove()
                        //     // let children = document.getElementById(constituent.$el.id).children;
                        //     // line.show() 
                        //     // console.log(elmLine)
                        //     // var div = document.getElementById(myuuid);
                        //     // console.log(children)
                        //     // if (children.style.display === "none") {
                        //     //     children.style.display = "block";
                        //     //     line.show()
                        //     // } else {
                        //     //     children.style.display = "none";
                        //     //     line.hide()
                        //     // }
                        // });

                        // const line = new LeaderLine(LeaderLine.mouseHoverAnchor(constituent.$el), basicFeature.$el, {
                        //     color: this.rbgToHex(this.randomRgbColor()), 
                        //     size: 3,
                        //     startPlug: 'disc',
                        //     endPlug: 'disc',
                        //     path: 'straight'
                        // });

                        this.ConstituentsBasicFeaturesLines.push(lineObj)
                        resolve()
                        })                       
                    })
                    .catch((error) => {
                    // your action on error success
                        console.log('ERROR ON ADD RELATION CONSTITUENTS/BASIC FEATURES =>>> ', error);
                    });
            })
        },
        getRelationsBasicFeaturesEmergentBehaviors() {
            let payload = {                
                        features_list: this.basicFeatures,
                        emergents_list: this.emergentBehaviors
                    }
            const path_addRelationsBasicFeaturesEmergentBehaviors = `${process.env.VUE_APP_BASE_URL}/relation/basic_feature_emergent_behavior/post`;
            return new Promise((resolve, reject) => {
                axios({
                    url: path_addRelationsBasicFeaturesEmergentBehaviors,
                    method: 'post',
                    data: payload
                    })
                    .then((res) => {
                        // console.log(res.data)
                        let relations = res.data
                        relations.forEach(relation => {
                        // var startElement = document.getElementById(sos);
                        // var endElement = document.getElementById(constituent);

                        let basicFeature = this.$refs.basicFeatures.find(basicFeature => {     
                            // console.log(basicFeature)                       
                            return basicFeature.$attrs.id == relation.feature_external_id
                        })

                        let emergentBehavior = this.$refs.emergentBehaviors.find(emergentBehavior => {     
                            // console.log(emergentBehavior)                       
                            return emergentBehavior.$attrs.id == relation.emergent_external_id
                        })

                        // console.log('Constituent => ', constituent)
                        // console.log('Basic Feature => ', basicFeature)

                        // var line = new LeaderLine(LeaderLine.mouseHoverAnchor(basicFeature.$el), emergentBehavior.$el, {
                        //     size: 3,
                        //     color: '#000000',
                        //     startPlug: 'disc',
                        //     endPlug: 'disc',
                        //     path: 'straight'
                        // });

                        const line = new LeaderLine(LeaderLine.mouseHoverAnchor(basicFeature.$el), emergentBehavior.$el, {
                            size: 3,
                            color: '#000000',
                            startPlug: 'disc',
                            endPlug: 'disc',
                            path: 'straight',
                        });

                        let lineObj = {}
                        lineObj.feature_external_id = relation.feature_external_id
                        lineObj.emergent_external_id = relation.emergent_external_id
                        lineObj.line = line

                        this.BasicFeaturesEmergentBehaviorsLines.push(lineObj)
                        resolve()
                        })                       
                    })
                    .catch((error) => {
                    // your action on error success
                        console.log('ERROR ON ADD RELATION CONSTITUENTS/BASIC FEATURES =>>> ', error);
                    });
            })
        },
        loadSoS(sos_external_id) {
            this.clearAll()
            this.getConstituentsFromSoS(sos_external_id).then(result => {
                this.getBasicFeaturesFromSoS(sos_external_id).then(result => {
                    this.getEmergentBehaviorsFromSoS(sos_external_id).then(result => {
                        this.getRelationsConstituentsBasicFeatures().then(result => {
                            this.getRelationsBasicFeaturesEmergentBehaviors().then(result => {
                                // console.log('this.ConstituentsBasicFeaturesLines =>>> ', this.ConstituentsBasicFeaturesLines)
                                // console.log('this.BasicFeaturesEmergentBehaviorsLines =>>> ', this.BasicFeaturesEmergentBehaviorsLines)
                                // console.log('DONE!')
                            })
                        })
                    })               
                })
            })
        },
        clearAll() {
            // console.log('this.ConstituentsBasicFeaturesLines =>>> ', this.ConstituentsBasicFeaturesLines)
            // console.log('this.BasicFeaturesEmergentBehaviorsLines =>>> ', this.BasicFeaturesEmergentBehaviorsLines)
            this.ConstituentsBasicFeaturesLines.forEach(line => {
                // console.log('removing ConstituentsBasicFeaturesLines')
                line.remove()
            })
            this.BasicFeaturesEmergentBehaviorsLines.forEach(line => {
                // console.log('removing BasicFeaturesEmergentBehaviorsLines')
                line.remove()
            })
            this.constituents = []
            this.basicFeatures = []
            this.emergentBehaviors = []
            this.ConstituentsBasicFeaturesLines = []
            this.BasicFeaturesEmergentBehaviorsLines = []
        },
        removeConstituent(index){            
            this.ConstituentsBasicFeaturesLines.forEach(line => {
                // console.log('removing ConstituentsBasicFeaturesLines')
                line.remove()
            })
            this.ConstituentsBasicFeaturesLines = []
            this.constituents.splice(index, 1)
            this.getRelationsConstituentsBasicFeatures()
        },
        removeBasicFeature(index){
            this.ConstituentsBasicFeaturesLines.forEach(line => {
                // console.log('removing ConstituentsBasicFeaturesLines')
                line.remove()
            })
            this.BasicFeaturesEmergentBehaviorsLines.forEach(line => {
                // console.log('removing BasicFeaturesEmergentBehaviorsLines')
                line.remove()
            })
            this.ConstituentsBasicFeaturesLines = []
            this.BasicFeaturesEmergentBehaviorsLines = []
            this.basicFeatures.splice(index, 1)
            this.getRelationsConstituentsBasicFeatures()
            this.getRelationsBasicFeaturesEmergentBehaviors()
        },
        removeEmergentBehavior(index){
            this.BasicFeaturesEmergentBehaviorsLines.forEach(line => {
                // console.log('removing BasicFeaturesEmergentBehaviorsLines')
                line.remove()
            })
            this.BasicFeaturesEmergentBehaviorsLines = []
            this.emergentBehaviors.splice(index, 1)
            this.getRelationsBasicFeaturesEmergentBehaviors()
        },
        randomRgbColor() {
            const r = this.randomInteger(255);
            const g = this.randomInteger(255);
            const b = this.randomInteger(255);
            return [r, g, b]
        },
        randomInteger(max) {
            return Math.floor(Math.random() * (max + 1))
        },
        rbgToHex(rgb)  {
            const [r, g, b] = rgb;

            const hr = r.toString(16).padStart(2, '0');
            const hg = g.toString(16).padStart(2, '0');
            const hb = b.toString(16).padStart(2, '0');
            return `#${hr}${hg}${hb}`
        }
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
