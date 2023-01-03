<template>
  <div class="top-down">
    <div class="top-down__panel">
      <div class="top-down__title">Avaliable Emergent Behaviors</div>
      <div class="top-down__content">
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

        <v-btn elevation="2" @click="addEmergentBehavior()">Add Behavior</v-btn>
      </div>
    </div>
    <div class="top-down__panel">
      <div class="top-down__title">Chosen Emergent Behaviors</div>
      <div class="top-down__content">
        <v-chip
          close
          close-icon="mdi-delete"
          color="orange"
          v-for="(behavior, index) in chosenEmergentBehaviors"
          :key="index"
          :id="behavior.emergent_external_id"
          @click:close="removeEmergentBehavior(index)"
          >{{ behavior.description }}</v-chip
        >
      </div>
    </div>
    <div class="top-down__panel">
      <div class="top-down__title">Necessary Constituents</div>
      <div class="top-down__content">
        <v-btn elevation="2" @click="getConstituentsFromEmergentBehaviors()"
          >Get!</v-btn
        >

        <v-chip
          v-for="(constituent, index) in necessaryConstituents"
          :key="index"
          :id="constituent.constituent_external_id"
          color="green"
          >{{ constituent.constituent_name }}</v-chip
        >
      </div>
    </div>

    <v-dialog transition="dialog-top-transition" max-width="600">
      <!-- <template v-slot:activator="{ on, attrs }">
                <v-btn
                    color="#A4BE7B"
                    v-bind="attrs"
                    v-on="on"
                >Error Dialog</v-btn>
                </template> -->
      <template v-slot:default="errorDialog">
        <v-card>
          <v-toolbar color="#A4BE7B" dark>Error</v-toolbar>
          <v-card-text>
            <div class="text-h5 pa-12">Sorry, an error occurred!</div>
          </v-card-text>
          <v-card-actions class="justify-end">
            <v-btn text @click="errorDialog.value = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data: () => ({
    availableEmergentBehaviors: [],
    selectedEmergentBehavior: null,
    chosenEmergentBehaviors: [],
    necessaryConstituents: [],
    errorDialog: false,
  }),
  created() {
    this.getEmergentBehaviors();
  },
  methods: {
    getEmergentBehaviors() {
      const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/get`;
      axios
        .get(path)
        .then((res) => {
          this.availableEmergentBehaviors = res.data;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
    selectBehavior(obj) {
      this.selectedEmergentBehavior = obj;
      console.log("chosen Behavior => ", this.selectedEmergentBehavior);
    },
    addEmergentBehavior() {
      this.chosenEmergentBehaviors.push(this.selectedEmergentBehavior);

      let uniqBehaviors = [];

      const filterDuplicates = this.chosenEmergentBehaviors.reduce(
        (arr, el) => {
          if (
            !arr.some(
              (current) =>
                current.emergent_external_id === el.emergent_external_id
            )
          ) {
            arr.push(el);
          }
          return arr;
        },
        uniqBehaviors
      );

      console.log("uniqBehaviors => ", uniqBehaviors);
      console.log("filterDuplicates => ", filterDuplicates);
      this.chosenEmergentBehaviors = uniqBehaviors;
    },
    removeEmergentBehavior(index) {
      this.chosenEmergentBehaviors.splice(index, 1);
    },
    getConstituentsFromEmergentBehaviors() {
      const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/basic_features/constituents/post`;
      let payload = {
        behaviors_list: this.chosenEmergentBehaviors,
      };
      axios({
        url: path,
        method: "post",
        data: payload,
      })
        .then((res) => {
          // console.log(res.data)
          this.necessaryConstituents = res.data;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error("ERROR =>>> ", error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.top-down {
  $self: &;
  height: calc(100vh - 160px);
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  background-color: #dfe8cc;
  padding: 10px;

  & > div {
    flex: 1 0 100%;
  }

  &__panel {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    #{$self}__title {
      background-color: #373640;
      color: #ffffff;
      font-size: 1.2rem;
      font-weight: bold;
      padding: 4px 10px;
      border-radius: 6px;
      margin-block-end: 0.625rem;
    }

    #{$self}__content {
      display: flex;
      flex-direction: column;
      gap: 10px;
      border-radius: 6px;
      height: 100%;
      padding: 4px 10px;
      overflow-y: auto;
    }
  }
}

.v-chip.v-size--default {
  height: auto !important;
}

.v-chip {
  white-space: normal !important;
  text-align: left;
  overflow: initial;

  &__content {
    justify-content: space-between;
    width: 100%;
  }
}
</style>
