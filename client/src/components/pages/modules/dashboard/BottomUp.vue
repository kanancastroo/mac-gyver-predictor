<template>
  <div class="bottom-up">
    <div class="bottom-up__panel">
      <div class="bottom-up__title">SoS</div>
      <div class="bottom-up__content">
        <v-select
          :items="this.sos"
          item-text="sos_name"
          item-value="sos_external_id"
          label="Pick a SoS"
          v-model="selectedSoS"
          ref="sos"
          @change="getConstituentsWithFeatures(selectedSoS.sos_external_id)"
          dense
          return-object
        ></v-select>

        <div class="bottom-up__title">
          {{ this.getConstituentsColumnLabel() }}
        </div>
        <div class="bottom-up__content">
          <v-tooltip
            v-for="(constituent, index) in constituents"
            :key="index"
            right
          >
            <template v-slot:activator="{ on, attrs }">
              <span v-bind="attrs" v-on="on">
                <v-chip
                  color="primary"
                  dark
                  ref="constituents"
                  @click="addConstituent(constituent)"
                >
                  {{ constituent.constituent_name }}
                </v-chip>
              </span>
            </template>
            <p
              v-for="(feature, index) in constituent.basic_features"
              :key="index"
            >
              {{ feature.description }}
            </p>
            <!-- <span>{{ constituent.basic_features }}</span> -->
          </v-tooltip>

          <!-- <v-tooltip right>
          <template v-slot:activator="{ on, attrs }">
            <v-chip
              color="primary"
              ref="constituents"
              v-bind="attrs"
              v-on="on"
              v-for="(constituent, index) in constituents"
              :key="index"
              @click="addConstituent(constituent)"
            >
              {{ constituent.constituent_name }}
            </v-chip>
          </template>
          <span>Right tooltip</span>
        </v-tooltip> -->
        </div>

        <!-- <v-chip
          color="primary"
          ref="sos"
          v-for="(sos, index) in sos"
          :key="index"
          @click="getConstituents(sos.sos_external_id, $refs.sos[index])"
        >
          {{ sos.sos_name }}
        </v-chip> -->
      </div>
    </div>
    <!-- <div class="bottom-up__panel">

    </div> -->
    <div class="bottom-up__panel">
      <div class="bottom-up__title">SoS Modeling Space</div>
      <div class="bottom-up__content">
        <div v-for="(constituent, index) in composedSoS" :key="index">
          <v-tooltip right>
            <template v-slot:activator="{ on, attrs }">
              <span v-bind="attrs" v-on="on">
                <v-chip
                  class="d-flex justify-between"
                  color="primary"
                  dark
                  close
                  @click:close="removeConstituent(index)"
                >
                  {{ constituent.constituent_name }}
                </v-chip>
              </span>
            </template>
            <p
              v-for="(feature, index) in constituent.basic_features"
              :key="index"
            >
              {{ feature.description }}
            </p>
            <!-- <span>{{ constituent.basic_features }}</span> -->
          </v-tooltip>
        </div>

        <!-- <v-chip
          class="d-flex justify-between"
          color="primary"
          close
          v-for="(constituent, index) in composedSoS"
          :key="index"
          @click:close="removeConstituent(index)"
        >
          {{ constituent.constituent_name }}
        </v-chip> -->
      </div>
    </div>
    <div class="bottom-up__panel">
      <div class="bottom-up__title">
        Emergent Behaviors (from constituents in the SoS Modeling Space)
      </div>
      <div class="bottom-up__content">
        <v-dialog v-model="addSoSDialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="#A4BE7B" dark v-bind="attrs" v-on="on">
              Save new SoS
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
                    <v-text-field v-model="sosName" label=""></v-text-field>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="addSoSDialog = false">
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="
                  addSoSDialog = false;
                  saveSoS(sosName);
                "
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="saveDialog" hide-overlay persistent width="300">
          <v-card color="#A4BE7B" dark>
            <v-card-text>
              Saving new SoS and updating model...
              <v-progress-linear
                indeterminate
                color="white"
                class="mb-0"
              ></v-progress-linear>
            </v-card-text>
          </v-card>
        </v-dialog>
        <!-- <div class="bottom-up__group">
          <label class="bottom-up__label">Known:</label>
          <div class="bottom-up__behaviors">
            <v-chip
              class="ma-2"
              color="#A4BE7B"
              close
              v-for="(behavior, index) in knownBehaviors"
              :key="index"
              @click:close="removeKnownBehavior(index)"
            >
              {{ behavior.description }}
            </v-chip>
          </div>
          <v-btn color="#A4BE7B" dark @click="showKnownEmergentBehaviors()"
            >Show</v-btn
          >
        </div> -->
        <div class="bottom-up__group">
          <label class="bottom-up__label">Predicted:</label>
          <div class="bottom-up__behaviors">
            <v-tooltip
              v-for="(prediction, index) in predictions"
              :key="index"
              left
            >
              <template v-slot:activator="{ on, attrs }">
                <span v-bind="attrs" v-on="on">
                  <v-chip
                    class="ma-2"
                    color="primary"
                    close
                    @click:close="removePrediction(index)"
                  >
                    {{ prediction.description }}
                  </v-chip>
                </span>
              </template>
              Probability: {{ prediction.probability }} %
              <!-- <span>{{ constituent.basic_features }}</span> -->
            </v-tooltip>
          </div>
          <v-btn
            :disabled="predictDialog"
            :loading="predictDialog"
            color="#A4BE7B"
            dark
            @click="
              predictDialog = true;
              predict();
            "
          >
            Predict
          </v-btn>
          <v-dialog v-model="predictDialog" hide-overlay persistent width="300">
            <v-card color="#A4BE7B" dark>
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
        <div class="bottom-up__group">
          <label class="bottom-up__label">Observed:</label>
          <div class="bottom-up__behaviors">
            <v-chip
              class="ma-2"
              color="primary"
              close
              v-for="(behavior, index) in observedBehaviors"
              :key="index"
              @click:close="removeObservedBehavior(index)"
            >
              {{ behavior.description }}
            </v-chip>
          </div>
          <v-dialog v-model="behaviorDialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="#A4BE7B" dark v-bind="attrs" v-on="on"> Add </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">Emergent Behavior</span>
                <small
                  >Pick one from the list or type a new behavior in the
                  textbox</small
                >
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="12">
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
                  @click="
                    behaviorDialog = false;
                    addObservedBehavior(selectedBehavior, insertedBehavior);
                  "
                >
                  Add
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>

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
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { v4 as uuidv4 } from "uuid";
// import LeaderLine from 'leader-line-new';

export default {
  data: () => ({
    selectedSoS: null,
    sos: [],
    constituents: [],
    composedSoS: [],
    featuresFromChosenConstituents: [],
    message: "Train Model",
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
    errorDialog: false,
    sosName: "Unnamed SoS",
  }),
  watch: {
    predictDialog(val) {
      if (!val) return;

      // setTimeout(() => (this.dialog = false), 4000)
    },
    saveDialog(val) {
      if (!val) return;

      // setTimeout(() => (this.dialog = false), 4000)
    },
    behaviorDialog(val) {
      if (!val) return;

      // setTimeout(() => (this.dialog = false), 4000)
    },
    addSoSDialog(val) {
      if (!val) return;

      // setTimeout(() => (this.dialog = false), 4000)
    },
  },
  methods: {
    getConstituentsColumnLabel() {
      if (this.selectedSoS != null)
        return "Constituents from " + this.selectedSoS.sos_name;
      return "Constituents";
    },
    addObservedBehavior(selectedBehavior, insertedBehavior) {
      // console.log('selectedBehavior: ', selectedBehavior)
      // console.log('insertedBehavior: ', insertedBehavior)
      if (insertedBehavior) {
        const addBehavior = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/add`;
        axios
          .get(addBehavior, { params: { description: insertedBehavior } })
          .then((res) => {
            let newBehavior = {};
            newBehavior.emergent_external_id = res.data;
            newBehavior.description = insertedBehavior;
            this.observedBehaviors.push(newBehavior);
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      } else {
        this.observedBehaviors.push(selectedBehavior);
      }
    },
    showKnownEmergentBehaviors() {
      const path = `${process.env.VUE_APP_BASE_URL}/constituents/basic_features/emergent_behaviors/post`;
      let payload = {
        constituent_list: this.composedSoS,
      };
      axios({
        url: path,
        method: "post",
        data: payload,
      })
        .then((res) => {
          this.knownBehaviors = res.data;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error("ERROR ON SHOW KNOWN EMERGENT BEHAVIORS =>>> ", error);
        });
    },
    getAllEmergentBehaviors() {
      const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/get`;
      axios
        .get(path)
        .then((res) => {
          this.emergentBehaviors = res.data;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
    saveSoS(sosName) {
      this.saveDialog = true;
      const path_addSoS = `${process.env.VUE_APP_BASE_URL}/sos/add`;
      console.log(path_addSoS);
      let sos_name = sosName;
      let sos_external_id = uuidv4();
      axios
        .get(path_addSoS, {
          params: { sos_name: sos_name, sos_id: sos_external_id },
        })
        .then(async (res) => {
          console.log(res.data);

          const path_addRelationSoSConstituent = `${process.env.VUE_APP_BASE_URL}/relation/sos_constituent/add`;
          console.log(path_addRelationSoSConstituent);
          let promises = [];
          for (let i = 0; i < this.composedSoS.length; i++) {
            promises.push(
              axios
                .get(path_addRelationSoSConstituent, {
                  params: {
                    sos_external_id: sos_external_id,
                    constituent_external_id:
                      this.composedSoS[i].constituent_external_id,
                  },
                })
                .then((res) => {
                  console.log(
                    `Added relation between ${sos_name} and ${this.composedSoS[i].constituent_name}`
                  );
                })
                .catch((error) => {
                  this.errorDialog = true;
                  console.error(
                    "ERROR ON ADD RELATION SOS/CONSTITUENT =>>> ",
                    error
                  );
                  this.saveDialog = false;
                })
            );
          }

          await Promise.all(promises);
          console.log(
            "Relations SoS/Constituent added Successfully. Now adding relations Basic Features/Emergent Behaviors..."
          );

          console.log(
            "Executing addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.predictions)"
          );
          this.addRelationBasicFeaturesEmergentBehaviors(
            sos_external_id,
            this.predictions
          ).then((result) => {
            console.log(
              "Executing addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.knownBehaviors)"
            );
            this.addRelationBasicFeaturesEmergentBehaviors(
              sos_external_id,
              this.knownBehaviors
            ).then((result) => {
              console.log(
                "Executing addRelationBasicFeaturesEmergentBehaviors(sos_external_id, this.observedBehaviors)"
              );
              this.addRelationBasicFeaturesEmergentBehaviors(
                sos_external_id,
                this.observedBehaviors
              ).then((result) => {
                console.log("Executing updateModel()");
                this.updateModel().then((result) => console.log("DONE!"));
              });
            });
          });
        })
        .catch((error) => {
          this.saveDialog = false;
          this.errorDialog = true;
          console.error("ERROR ON ADD SOS =>>> ", error);
        });
    },
    updateModel() {
      const path_processing = `${process.env.VUE_APP_BASE_URL}/database/process`;
      return new Promise((resolve, reject) => {
        let payload = {
          token: store.getters.getJwt.token,
        };
        console.log("PAYLOAD => ", payload);
        axios({
          url: path_processing,
          method: "post",
          data: payload,
        })
          .then((res) => {
            console.log("Model updated successfully!");
            this.saveDialog = false;
            resolve();
          })
          .catch((error) => {
            console.error(error);
            this.saveDialog = false;
            this.errorDialog = true;
          });
      });
    },
    addRelationBasicFeaturesEmergentBehaviors(sos_external_id, behaviorsList) {
      console.log("sos_external_id =>>> ", sos_external_id);
      let payload = {
        basic_features_list: this.featuresFromChosenConstituents,
        emergent_behaviors_list: behaviorsList,
      };
      const path_addRelationsFeaturesBehaviors = `${process.env.VUE_APP_BASE_URL}/relation/basic_feature_emergent_behavior/add`;
      return new Promise((resolve, reject) => {
        axios({
          url: path_addRelationsFeaturesBehaviors,
          method: "post",
          data: payload,
        })
          .then((res) => {
            // your action after success
            // this.dialog = false
            console.log(
              "Relations Basic Features/Emergent Behaviors added Successfully. Now adding relations SoS/Emergent Behaviors..."
            );
            let payload_final = {
              sos_external_id: sos_external_id,
              emergent_behaviors_list: behaviorsList,
            };
            const path_addRelationsSoSBehaviors = `${process.env.VUE_APP_BASE_URL}/relation/sos_emergent_behavior/add`;
            axios({
              url: path_addRelationsSoSBehaviors,
              method: "post",
              data: payload_final,
            })
              .then((res) => {
                // your action after success
                // this.dialog = false
                console.log("SUBPROCESS FINISHED!!!");
                resolve();
              })
              .catch((error) => {
                // your action on error success
                console.log("ERROR ON ADD RELATION SoS/BEHAVIORS =>>> ", error);
                this.saveDialog = false;
                this.errorDialog = true;
              });
          })
          .catch((error) => {
            // your action on error success
            console.log(
              "ERROR ON ADD RELATION FEATURES/BEHAVIORS =>>> ",
              error
            );
            this.saveDialog = false;
            this.errorDialog = true;
          });
      });
    },
    closeDialog() {
      this.dialog = false;
    },
    getSoS() {
      const path = `${process.env.VUE_APP_BASE_URL}/sos/get`;
      console.log(path);
      axios
        .get(path)
        .then((res) => {
          this.sos = res.data;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
    getConstituents(sos_id) {
      this.constituents = [];
      // this.SoSLines.forEach(line => line.remove())
      // this.SoSLines = []
      const constituents_path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_id}/constituents/get`;
      return new Promise((resolve, reject) => {
        axios
          .get(constituents_path)
          .then((res) => {
            this.constituents = res.data;
            console.log(this.constituents);
            this.$nextTick(() => {
              resolve();
            });
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    async getFeaturesForConstituents() {
      let promisesArray = [];

      for (let i = 0; i < this.constituents.length; i++) {
        let constituent_id = this.constituents[i].constituent_external_id;
        const features_path = `${process.env.VUE_APP_BASE_URL}/constituents/${constituent_id}/basic_features/get`;
        promisesArray.push(
          axios
            .get(features_path)
            .then((res) => {
              this.constituents[i].basic_features = res.data;
            })
            .catch((error) => {
              this.errorDialog = true;
              console.error(error);
            })
        );
      }

      await Promise.all(promisesArray);
    },
    getConstituentsWithFeatures(sos_id) {
      this.getConstituents(sos_id).then((result) => {
        console.log("Got constituents!");
        this.getFeaturesForConstituents().then((result) => {
          console.log("Got features for constituents!");
          this.$nextTick(() => {
            let auxConstituents = this.constituents;
            this.constituents = [];
            this.constituents = auxConstituents;
            console.log("Resolving after $nextTick");
          });
        });
      });

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
    },
    preProcessDatabase() {
      const path = `${process.env.VUE_APP_BASE_URL}/database/process`;
      let payload = {
        token: store.getters.getJwt.token,
      };
      console.log("PAYLOAD => ", payload);
      axios({
        url: path,
        method: "post",
        data: payload,
      })
        .then((res) => {
          this.message = res.data;
        })
        .catch((error) => {
          this.errorDialog = true;
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
        constituent_list: this.composedSoS,
      };
      axios({
        url: path,
        method: "post",
        data: payload,
      })
        .then((res) => {
          // your action after success
          this.predictions = res.data;
          console.log("PREDICTIONS => ", this.predictions);
          // this.dialog = false
          console.log(this.predictions);

          const featuresPath = `${process.env.VUE_APP_BASE_URL}/constituents/basic_features/post`;
          axios({
            url: featuresPath,
            method: "post",
            data: payload,
          })
            .then((res) => {
              // your action after success
              this.featuresFromChosenConstituents = res.data;
              console.log("BASIC FEATURES:");
              console.log(this.featuresFromChosenConstituents);
              this.predictDialog = false;
            })
            .catch((error) => {
              // your action on error success
              this.predictDialog = false;
              this.errorDialog = true;
              console.log(error);
            });
        })
        .catch((error) => {
          this.errorDialog = true;
          // your action on error success
          console.log(error);
        });
    },
    addConstituent(constituent) {
      this.composedSoS.push(constituent);
      console.log("composed SoS => ", this.composedSoS);
    },
    removeConstituent(index) {
      this.composedSoS.splice(index, 1);
    },
    removePrediction(index) {
      this.predictions.splice(index, 1);
    },
    removeKnownBehavior(index) {
      this.knownBehaviors.splice(index, 1);
    },
    removeObservedBehavior(index) {
      this.observedBehaviors.splice(index, 1);
    },
  },
  created() {
    this.getSoS();
    this.getAllEmergentBehaviors();
  },
};
</script>

<style lang="scss">
.bottom-up {
  $self: &;
  // height: calc(100vh - 160px);
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
      width: 100%;
      padding: 15px 10px;
      margin: auto;
      overflow-y: auto;
    }
  }

  &__group {
    padding: 10px;
    background-color: #eee;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    border-radius: 6px;

    #{$self}__label {
      background-color: #bbbbbb;
      padding: 4px 10px;
      color: #ffffff;
      text-align: left;
      font-weight: bold;
      font-size: 14px;
      border-radius: 4px;
    }

    #{$self}__behaviors {
      background-color: #e3e3e3;
      height: clamp(100px, 100px, 150px);
      width: 100%;
      overflow-y: auto;
    }
  }
}

.v-chip.v-size--default {
  height: auto !important;
  max-width: 95%;
}

.v-chip .v-chip__content {
  height: auto;
  min-height: 32px;
  white-space: pre-wrap;
}

.v-chip {
  width: 100%;
  white-space: normal !important;
  text-align: left;
  overflow: initial !important;

  &__content {
    justify-content: space-between;
    width: 100%;
  }
}
</style>
