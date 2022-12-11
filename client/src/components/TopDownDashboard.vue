<template>
    <div class="dashboard">
        <div class="panel">
            <div class="title">Avaliable Emergent Behaviors</div>

            <v-select
                :items="this.availableEmergentBehaviors"
                item-text="description"
                item-value="emergent_external_id"
                label="Pick an emergent behavior"
                v-model="selectedEmergentBehavior"
                @change="selectBehavior(selectedEmergentBehavior)"
                dense
                return-object
                ></v-select>

                <v-btn
                elevation="2"
                @click="addEmergentBehavior()"
                >Add Behavior</v-btn>
        </div>
        <div class="panel">
            <div class="title">Chosen Emergent Behaviors</div>
            <v-chip
                close
                close-icon="mdi-delete"
                color="orange"
                v-for="(behavior, index) in chosenEmergentBehaviors" :key="index" :id="behavior.emergent_external_id"
                @click:close="removeEmergentBehavior(index)"
            >{{ behavior.description }}</v-chip>
        </div>
        <div class="panel">
            <div class="title">Necessary Constituents</div>

            <v-btn
                elevation="2"
                @click="getConstituentsFromEmergentBehaviors()"
                >Get!</v-btn>

                <v-chip
                v-for="(constituent, index) in necessaryConstituents" :key="index" :id="constituent.constituent_external_id"
                color="green"
                >{{ constituent.constituent_name }}</v-chip>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    data: () => ({
        availableEmergentBehaviors: [],
        selectedEmergentBehavior: null,
        chosenEmergentBehaviors: [],
        necessaryConstituents: []
    }),
    created() {
        this.getEmergentBehaviors();
    },
    methods:{
        getEmergentBehaviors() {
            const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/get`;
            axios.get(path)
                .then((res) => {
                    this.availableEmergentBehaviors = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        selectBehavior(obj) {
            this.selectedEmergentBehavior = obj
            console.log('chosen Behavior => ', this.selectedEmergentBehavior)
        },
        addEmergentBehavior() {
            this.chosenEmergentBehaviors.push(this.selectedEmergentBehavior)
            
            let uniqBehaviors = []

            const filterDuplicates = this.chosenEmergentBehaviors.reduce((arr, el) => {
                if(!arr.some(current => current.emergent_external_id === el.emergent_external_id)) {
                arr.push(el);
                }
                return arr;
            }, uniqBehaviors);
            
            console.log('uniqBehaviors => ', uniqBehaviors)
            console.log('filterDuplicates => ', filterDuplicates)
            this.chosenEmergentBehaviors = uniqBehaviors
        },
        removeEmergentBehavior(index) {
            this.chosenEmergentBehaviors.splice(index, 1)
        },
        getConstituentsFromEmergentBehaviors() {
            const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/basic_features/constituents/post`;
            let payload = {
                        behaviors_list: this.chosenEmergentBehaviors,
                    }    
            axios({
                    url: path,
                    method: 'post',
                    data: payload
                    })
                    .then((res) => {
                        // console.log(res.data)
                        this.necessaryConstituents = res.data
                    })
                    .catch((error) => {
                        console.error('ERROR =>>> ', error);
                    })
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