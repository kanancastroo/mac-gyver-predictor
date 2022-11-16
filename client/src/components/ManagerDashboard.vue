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
                    close
                    v-for="(constituent, index) in constituents" :key="index"
                    @click:close="removeConstituent(index)">
                        {{ constituent.constituent_name }}
            </v-chip>
        </div>
        <div class="panel">
            <div class="title">Basic Features</div>
            <v-chip
                    class="ma-2"
                    close
                    v-for="(feature, index) in basicFeatures" :key="index"
                    @click:close="removeBasicFeature(index)">
                        {{ feature.description }}
            </v-chip>
        </div>
        <div class="panel">
            <div class="title">Emergent Behaviors</div> 
            <v-chip
                    class="ma-2"
                    close
                    v-for="(behavior, index) in emergentBehaviors" :key="index"
                    @click:close="removeEmergentBehavior(index)">
                        {{ behavior.description }}
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
        basicFeatures: [],
        emergentBehaviors: [],
        selectedSoS: null
    }),
    created() {
        this.getSoS();
    },
    methods: {
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
        getConstituentsFromSoS(sos_external_id) {
            const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/get`;
            // console.log(path, {params: {sos_external_id: sos_external_id}})
            
            return new Promise((resolve, reject) => {
                axios.get(path)
                    .then((res) => {
                        console.log('Loaded constituents...')
                        this.constituents = res.data;
                        resolve()
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                })
        },
        getBasicFeaturesFromSoS(sos_external_id) {
            const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/basic_features/get`;
            // console.log(path, {params: {sos_external_id: sos_external_id}})
            
            return new Promise((resolve, reject) => {
                axios.get(path)
                    .then((res) => {
                        this.basicFeatures = res.data;
                        console.log('Loaded basic features...')
                        resolve()
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                })
        },               
        getEmergentBehaviorsFromSoS(sos_external_id) {
            const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/basic_features/emergent_behaviors/get`;
            // console.log(path, {params: {sos_external_id: sos_external_id}})
            
            return new Promise((resolve, reject) => {
                axios.get(path)
                    .then((res) => {
                        this.emergentBehaviors = res.data;
                        console.log('Loaded emergent behaviors...')
                        resolve()
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                })
        },
        loadSoS(sos_external_id) {
            this.getConstituentsFromSoS(sos_external_id).then(result => {
                this.getBasicFeaturesFromSoS(sos_external_id).then(result => {
                    this.getEmergentBehaviorsFromSoS(sos_external_id).then(result => {
                        console.log('DONE!')
                    })
                })
            })
        },
        removeConstituent(index){
            this.constituents.splice(index, 1)
        },
        removeBasicFeature(index){
            this.basicFeatures.splice(index, 1)
        },
        removeEmergentBehavior(index){
            this.emergentBehaviors.splice(index, 1)
        },
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
