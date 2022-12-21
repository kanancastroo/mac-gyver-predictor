<template>
  <div class="manager">
    <div class="manager__panel h-100">
      <div class="manager__title">SoS</div>
      <div class="manager__content">
        <v-dialog v-model="sosDialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">
              Create
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">Create SoS</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-col cols="12" sm="12"> </v-col>
                <v-col cols="12">
                  <v-text-field
                    v-model="addingSoS"
                    label="Type a name for the new SoS"
                  ></v-text-field>
                </v-col>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="sosDialog = false">
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="
                  sosDialog = false;
                  createSoS(addingSoS);
                "
              >
                Create
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-spacer></v-spacer>
        <v-select
          :items="this.sos"
          item-text="sos_name"
          item-value="sos_external_id"
          label="Pick a SoS"
          v-model="selectedSoS"
          ref="sos"
          @change="loadSoS(selectedSoS.sos_external_id)"
          dense
          return-object
        ></v-select>
        <v-dialog
          v-model="editSoSDialog"
          :retain-focus="false"
          persistent
          max-width="600px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn color="primary" dark v-bind="attrs" v-on="on">
              <v-icon>
                {{ icons.mdiPencil }}
              </v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">Edit SoS</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-col cols="12" sm="12"> </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="Type a name for this SoS"
                    v-model="sosNewName"
                  ></v-text-field>
                </v-col>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="editSoSDialog = false">
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="
                  editSoSDialog = false;
                  editSoS(sosNewName);
                "
              >
                Edit
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

        <v-btn depressed color="primary" @click="removeSoS()">
          <v-icon>
            {{ icons.mdiDelete }}
          </v-icon>
        </v-btn>
        <v-spacer></v-spacer>

        <v-btn color="primary" elevation="2" @click="saveSoS()"
          >Save Changes</v-btn
        >
        <v-btn color="primary" elevation="2" @click="redrawLines()"
          >Redraw lines</v-btn
        >
      </div>
    </div>
    <div class="manager__panel">
      <div class="manager__title">Constituents</div>
      <div class="manager__content">
        <v-dialog v-model="constituentDialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              v-bind="attrs"
              v-on="on"
              @click="getConstituents()"
            >
              Add
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">Add constituent</span>
              <small
                >Pick one from the list or type a name for a new constituent in
                the textbox</small
              >
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-col cols="12" sm="12">
                  <v-select
                    :items="this.availableConstituents"
                    item-text="constituent_name"
                    item-value="constituent_external_id"
                    label="Pick a constituent"
                    v-model="addingConstituent"
                    return-object
                  ></v-select>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="...or type a new one here"
                    v-model="addingConstituent"
                  ></v-text-field>
                </v-col>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="blue darken-1"
                text
                @click="constituentDialog = false"
              >
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="
                  constituentDialog = false;
                  addConstituent(addingConstituent);
                "
              >
                Add
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-chip
          :color="
            selectedConstituents.includes(constituent.constituent_external_id)
              ? 'error'
              : 'primary'
          "
          close
          ref="constituents"
          v-for="(constituent, index) in constituents"
          :key="index"
          :id="constituent.constituent_external_id"
          @click:close="removeConstituent(constituent, index)"
          @click="handleColorConstituents(constituent)"
        >
          <v-dialog
            v-model="editConstituentDialog"
            :retain-focus="false"
            persistent
            max-width="600px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                icon
                dark
                v-bind="attrs"
                v-on="on"
                @click="selectConstituentForEdition(constituent)"
              >
                <v-icon>
                  {{ icons.mdiPencil }}
                </v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">Edit Constituent</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-col cols="12" sm="12"> </v-col>
                  <v-col cols="12">
                    <v-text-field
                      label="Type a name for this constituent"
                      v-model="constituentNewName"
                    ></v-text-field>
                  </v-col>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="editConstituentDialog = false"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="
                    editConstituentDialog = false;
                    editConstituent(constituentNewName);
                  "
                >
                  Edit
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          {{ constituent.constituent_name }}
        </v-chip>
      </div>
    </div>
    <div class="manager__panel">
      <div class="manager__title">Basic Features</div>
      <div class="manager__content">
        <v-dialog v-model="featureDialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              v-bind="attrs"
              v-on="on"
              @click="getBasicFeatures()"
            >
              Add
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">Add basic feature</span>
              <small
                >Pick one from the list or type a name for a new basic feature
                in the textbox</small
              >
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-col cols="12" sm="12">
                  <v-select
                    :items="this.availableBasicFeatures"
                    item-text="description"
                    item-value="feature_external_id"
                    label="Pick a basic feature"
                    v-model="addingFeature"
                    return-object
                  ></v-select>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="...or type a new one here"
                    v-model="addingFeature"
                  ></v-text-field>
                </v-col>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="featureDialog = false">
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="
                  featureDialog = false;
                  addBasicFeature(addingFeature);
                "
              >
                Add
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-chip
          :color="
            selectedFeatures.includes(feature.feature_external_id)
              ? 'error'
              : 'primary'
          "
          close
          ref="basicFeatures"
          v-for="(feature, index) in basicFeatures"
          :key="index"
          :id="feature.feature_external_id"
          @click:close="removeBasicFeature(feature, index)"
          @click="handleColorBasicFeatures(feature)"
        >
          <v-dialog
            v-model="editBasicFeatureDialog"
            :retain-focus="false"
            persistent
            max-width="600px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                icon
                dark
                v-bind="attrs"
                v-on="on"
                @click="selectBasicFeatureForEdition(feature)"
              >
                <v-icon>
                  {{ icons.mdiPencil }}
                </v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">Edit Basic Feature</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-col cols="12" sm="12"> </v-col>
                  <v-col cols="12">
                    <v-text-field
                      label="Type a description for this basic feature"
                      v-model="featureNewDescription"
                    ></v-text-field>
                  </v-col>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="editBasicFeatureDialog = false"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="
                    editBasicFeatureDialog = false;
                    editBasicFeature(featureNewDescription);
                  "
                >
                  Edit
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          {{ feature.description }}
        </v-chip>
      </div>
    </div>
    <div class="manager__panel">
      <div class="manager__title">Emergent Behaviors</div>
      <div class="manager__content">
        <v-dialog v-model="behaviorDialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              v-bind="attrs"
              v-on="on"
              @click="getEmergentBehaviors()"
            >
              Add
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">Add emergent behavior</span>
              <small
                >Pick one from the list or type a name for a new emergent
                behavior in the textbox</small
              >
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-col cols="12" sm="12">
                  <v-select
                    :items="this.availableEmergentBehaviors"
                    item-text="description"
                    item-value="emergent_external_id"
                    label="Pick an emergent behavior"
                    v-model="addingEmergent"
                    return-object
                  ></v-select>
                </v-col>
                <v-col cols="12">
                  <v-text-field
                    label="...or type a new one here"
                    v-model="addingEmergent"
                  ></v-text-field>
                </v-col>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="behaviorDialog = false">
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="
                  behaviorDialog = false;
                  addEmergentBehavior(addingEmergent);
                "
              >
                Add
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>

        <v-chip
          :color="
            selectedBehaviors.includes(behavior.emergent_external_id)
              ? 'error'
              : 'primary'
          "
          close
          ref="emergentBehaviors"
          v-for="(behavior, index) in emergentBehaviors"
          :key="index"
          :id="behavior.emergent_external_id"
          @click:close="removeEmergentBehavior(behavior, index)"
          @click="handleColorEmergentBehaviors(behavior)"
        >
          <v-dialog
            v-model="editEmergentBehaviorDialog"
            :retain-focus="false"
            persistent
            max-width="600px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                icon
                dark
                v-bind="attrs"
                v-on="on"
                @click="selectEmergentBehaviorForEdition(behavior)"
              >
                <v-icon>
                  {{ icons.mdiPencil }}
                </v-icon>
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="text-h5">Edit Emergent Behavior</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-col cols="12" sm="12"> </v-col>
                  <v-col cols="12">
                    <v-text-field
                      label="Type a description for this emergent behavior"
                      v-model="emergentNewDescription"
                    ></v-text-field>
                  </v-col>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="editEmergentBehaviorDialog = false"
                >
                  Cancel
                </v-btn>
                <v-btn
                  color="blue darken-1"
                  text
                  @click="
                    editEmergentBehaviorDialog = false;
                    editEmergentBehavior(emergentNewDescription);
                  "
                >
                  Edit
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          {{ behavior.description }}
        </v-chip>
      </div>
    </div>
    <div class="text-center">
      <v-dialog v-model="dialog" width="500">
        <v-card>
          <v-card-title class="text-h5 grey lighten-2">
            Forbidden action
          </v-card-title>

          <v-card-text> An invalid action was detected! </v-card-text>

          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click="dialog = false"> OK </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-dialog v-model="saveDialog" hide-overlay persistent width="300">
        <v-card color="blue" dark>
          <v-card-text>
            Saving SoS and updating model...
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
</template>

<script>
import axios from "axios";
import LeaderLine from "leader-line-new";
import { v4 as uuidv4 } from "uuid";
import { mdiPencil, mdiDelete } from "@mdi/js";

export default {
  data: () => ({
    icons: {
      mdiPencil,
      mdiDelete,
    },

    sos: [],
    constituents: [],
    basicFeatures: [],
    emergentBehaviors: [],

    availableConstituents: [],
    availableBasicFeatures: [],
    availableEmergentBehaviors: [],

    addingConstituent: null,
    constituentNewName: null,

    addingFeature: null,
    featureNewDescription: null,

    addingEmergent: null,
    emergentNewDescription: null,

    addingSoS: null,
    editingSoS: null,
    sosNewName: null,

    operationsQueue: [],

    ConstituentsBasicFeaturesLines: [],
    BasicFeaturesEmergentBehaviorsLines: [],

    selectedSoS: null,
    selectedConstituent: null,
    selectedBasicFeature: null,
    selectedEmergentBehavior: null,

    selectedConstituents: [],
    selectedFeatures: [],
    selectedBehaviors: [],
    selectedForCheck: [],

    dialog: false,
    sosDialog: false,
    constituentDialog: false,
    featureDialog: false,
    behaviorDialog: false,
    saveDialog: false,
    errorDialog: false,

    editConstituentDialog: false,
    editBasicFeatureDialog: false,
    editEmergentBehaviorDialog: false,
    editSoSDialog: false,
  }),
  created() {
    this.clearAll();
    this.getSoS();
  },
  methods: {
    updateModel() {
      const path_processing = `${process.env.VUE_APP_BASE_URL}/database/process`;
      return new Promise((resolve, reject) => {
        axios
          .get(path_processing)
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
    async saveSoS() {
      this.saveDialog = true;
      let promisesArray = [];

      for (let i = 0; i < this.operationsQueue.length; i++) {
        try {
          if (this.operationsQueue[i].type == "element") {
            if (this.operationsQueue[i].subtype == "sos") {
              if (this.operationsQueue[i].operation == "add") {
                promisesArray.push(
                  await this.addSoSDB(
                    this.operationsQueue[i].sos_external_id,
                    this.operationsQueue[i].sos_name
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "update") {
                promisesArray.push(
                  await this.updateSoSDB(
                    this.operationsQueue[i].sos_external_id,
                    this.operationsQueue[i].sos_name
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "remove") {
                promisesArray.push(
                  await this.removeSoSDB(
                    this.operationsQueue[i].sos_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
            }
            if (this.operationsQueue[i].subtype == "constituent") {
              if (this.operationsQueue[i].operation == "add") {
                promisesArray.push(
                  await this.addConstituentDB(
                    this.operationsQueue[i].constituent_external_id,
                    this.operationsQueue[i].constituent_name
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "update") {
                promisesArray.push(
                  await this.updateConstituentDB(
                    this.operationsQueue[i].constituent_external_id,
                    this.operationsQueue[i].constituent_name
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "remove") {
                promisesArray.push(
                  await this.removeConstituentDB(
                    this.operationsQueue[i].constituent_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
            }
            if (this.operationsQueue[i].subtype == "basicFeature") {
              if (this.operationsQueue[i].operation == "add") {
                promisesArray.push(
                  await this.addBasicFeatureDB(
                    this.operationsQueue[i].feature_external_id,
                    this.operationsQueue[i].description
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "update") {
                promisesArray.push(
                  await this.updateBasicFeatureDB(
                    this.operationsQueue[i].feature_external_id,
                    this.operationsQueue[i].description
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "remove") {
                promisesArray.push(
                  await this.removeBasicFeatureDB(
                    this.operationsQueue[i].feature_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
            }
            if (this.operationsQueue[i].subtype == "emergentBehavior") {
              if (this.operationsQueue[i].operation == "add") {
                promisesArray.push(
                  await this.addEmergentBehaviorDB(
                    this.operationsQueue[i].emergent_external_id,
                    this.operationsQueue[i].description
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "update") {
                promisesArray.push(
                  await this.updateEmergentBehaviorDB(
                    this.operationsQueue[i].emergent_external_id,
                    this.operationsQueue[i].description
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "remove") {
                promisesArray.push(
                  await this.removeEmergentBehaviorDB(
                    this.operationsQueue[i].emergent_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
            }
          }
          if (this.operationsQueue[i].type == "connection") {
            if (this.operationsQueue[i].subtype == "sos/constituent") {
              if (this.operationsQueue[i].operation == "add") {
                promisesArray.push(
                  await this.addConnectionSoSConstituentDB(
                    this.operationsQueue[i].sos_external_id,
                    this.operationsQueue[i].constituent_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "remove") {
                promisesArray.push(
                  await this.removeConnectionSoSConstituentDB(
                    this.operationsQueue[i].sos_external_id,
                    this.operationsQueue[i].constituent_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
            }
            if (this.operationsQueue[i].subtype == "constituent/basicFeature") {
              if (this.operationsQueue[i].operation == "add") {
                promisesArray.push(
                  await this.addConnectionConstituentBasicFeatureDB(
                    this.operationsQueue[i].constituent_external_id,
                    this.operationsQueue[i].feature_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "remove") {
                promisesArray.push(
                  await this.removeConnectionConstituentBasicFeatureDB(
                    this.operationsQueue[i].constituent_external_id,
                    this.operationsQueue[i].feature_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
            }
            if (
              this.operationsQueue[i].subtype == "basicFeature/emergentBehavior"
            ) {
              if (this.operationsQueue[i].operation == "add") {
                promisesArray.push(
                  await this.addConnectionBasicFeatureEmergentBehaviorDB(
                    this.operationsQueue[i].feature_external_id,
                    this.operationsQueue[i].emergent_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "remove") {
                promisesArray.push(
                  await this.removeConnectionBasicFeatureEmergentBehaviorDB(
                    this.operationsQueue[i].feature_external_id,
                    this.operationsQueue[i].emergent_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
            }
            if (this.operationsQueue[i].subtype == "sos/emergentBehavior") {
              if (this.operationsQueue[i].operation == "add") {
                promisesArray.push(
                  await this.addConnectionSoSEmergentBehaviorDB(
                    this.operationsQueue[i].sos_external_id,
                    this.operationsQueue[i].emergent_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
              if (this.operationsQueue[i].operation == "remove") {
                promisesArray.push(
                  await this.removeConnectionSoSEmergentBehaviorDB(
                    this.operationsQueue[i].sos_external_id,
                    this.operationsQueue[i].emergent_external_id
                  ).then((result) =>
                    console.log("Executed operation index => ", i)
                  )
                );
              }
            }
          }
        } catch (err) {
          console.log("ERR => ", err);
          continue;
        }
      }

      let operations = await Promise.all(promisesArray);
      this.updateModel().then((result) => {
        this.clearAll();
        this.getSoS();
        console.log("Database Updated Successfully!");
      });
    },
    selectConstituentForEdition(constituent) {
      this.selectedConstituent = constituent;
    },
    selectBasicFeatureForEdition(feature) {
      this.selectedBasicFeature = feature;
    },
    selectEmergentBehaviorForEdition(behavior) {
      this.selectedEmergentBehavior = behavior;
    },
    removeSoS() {
      // console.log('this.editingSoS => ', this.editingSoS)
      let sos = this.sos.find((sos) => {
        return sos.sos_external_id == this.editingSoS.sos_external_id;
      });

      this.sos.splice(this.sos.indexOf(sos), 1);

      this.clearAll();

      let queuedItem = {};
      queuedItem.type = "element";
      queuedItem.subtype = sos.type;
      queuedItem.operation = "remove";
      queuedItem.sos_external_id = this.editingSoS.sos_external_id;

      this.operationsQueue.push(queuedItem);
      console.log("this.editingSoS => ", this.editingSoS);
      console.log("operations Queue => ", this.operationsQueue);
      this.sosNewName = null;
    },
    editSoS(newName) {
      let sos = this.sos.find((sos) => {
        return sos.sos_external_id == this.editingSoS.sos_external_id;
      });
      sos.sos_name = newName;

      let queuedItem = {};
      queuedItem.type = "element";
      queuedItem.subtype = sos.type;
      queuedItem.operation = "update";
      queuedItem.sos_external_id = sos.sos_external_id;
      queuedItem.sos_name = newName;

      this.operationsQueue.push(queuedItem);
      console.log("selectedSoS => ", this.editingSoS);
      console.log("operations Queue => ", this.operationsQueue);
      this.sosNewName = null;
    },
    editConstituent(newName) {
      let constituent = this.constituents.find((constituent) => {
        return (
          constituent.constituent_external_id ==
          this.selectedConstituent.constituent_external_id
        );
      });
      constituent.constituent_name = newName;

      let queuedItem = {};
      queuedItem.type = "element";
      queuedItem.subtype = constituent.type;
      queuedItem.operation = "update";
      queuedItem.constituent_external_id = constituent.constituent_external_id;
      queuedItem.constituent_name = newName;

      this.operationsQueue.push(queuedItem);
      console.log("constituents => ", this.constituents);
      console.log("operations Queue => ", this.operationsQueue);
      this.constituentNewName = null;
    },
    editBasicFeature(newDescription) {
      let feature = this.basicFeatures.find((feature) => {
        return (
          feature.feature_external_id ==
          this.selectedBasicFeature.feature_external_id
        );
      });
      feature.description = newDescription;

      let queuedItem = {};
      queuedItem.type = "element";
      queuedItem.subtype = feature.type;
      queuedItem.operation = "update";
      queuedItem.feature_external_id = feature.feature_external_id;
      queuedItem.description = newDescription;

      this.operationsQueue.push(queuedItem);
      console.log("basic Features => ", this.basicFeatures);
      console.log("operations Queue => ", this.operationsQueue);
      this.featureNewDescription = null;
    },
    editEmergentBehavior(newDescription) {
      let emergent = this.emergentBehaviors.find((emergent) => {
        return (
          emergent.emergent_external_id ==
          this.selectedEmergentBehavior.emergent_external_id
        );
      });
      emergent.description = newDescription;

      let queuedItem = {};
      queuedItem.type = "element";
      queuedItem.subtype = emergent.type;
      queuedItem.operation = "update";
      queuedItem.emergent_external_id = emergent.emergent_external_id;
      queuedItem.description = newDescription;

      this.operationsQueue.push(queuedItem);
      console.log("emergent Behaviors => ", this.emergentBehaviors);
      console.log("operations Queue => ", this.operationsQueue);
      this.emergentNewDescription = null;
    },
    createSoS(item) {
      this.clearAll();

      let sos = {};
      let id = uuidv4();
      sos.sos_external_id = id;
      sos.sos_name = item;
      sos.type = "sos";
      this.sos.push(sos);

      this.editingSoS = sos;
      this.selectedSoS = sos;

      let queuedItem = {};
      queuedItem.type = "element";
      queuedItem.subtype = "sos";
      queuedItem.operation = "add";
      queuedItem.sos_external_id = id;
      queuedItem.sos_name = item;
      this.operationsQueue.push(queuedItem);

      console.log("editingSoS => ", this.editingSoS);
      console.log("operations Queue => ", this.operationsQueue);
    },
    addConstituent(item) {
      if (typeof item == "object") {
        this.constituents.push(item);
      } else {
        let constituent = {};
        let id = uuidv4();
        constituent.constituent_external_id = id;
        constituent.constituent_name = item;
        constituent.type = "constituent";
        this.constituents.push(constituent);

        let queuedItem = {};
        queuedItem.type = "element";
        queuedItem.subtype = "constituent";
        queuedItem.operation = "add";
        queuedItem.constituent_external_id = id;
        queuedItem.constituent_name = item;
        this.operationsQueue.push(queuedItem);

        let queuedItem_connection = {};
        queuedItem_connection.type = "connection";
        queuedItem_connection.subtype = "sos/constituent";
        queuedItem_connection.operation = "add";
        queuedItem_connection.constituent_external_id = id;
        queuedItem_connection.sos_external_id = this.editingSoS.sos_external_id;
        this.operationsQueue.push(queuedItem_connection);
      }
      console.log("constituents => ", this.constituents);
      console.log("operations Queue => ", this.operationsQueue);
    },
    addBasicFeature(item) {
      if (typeof item == "object") {
        this.basicFeatures.push(item);
      } else {
        let basicFeature = {};
        let id = uuidv4();
        basicFeature.feature_external_id = id;
        basicFeature.description = item;
        basicFeature.type = "basicFeature";
        this.basicFeatures.push(basicFeature);

        let queuedItem = {};
        queuedItem.type = "element";
        queuedItem.subtype = "basicFeature";
        queuedItem.operation = "add";
        queuedItem.feature_external_id = id;
        queuedItem.description = item;
        this.operationsQueue.push(queuedItem);
      }
      console.log("basic Features => ", this.basicFeatures);
      console.log("operations Queue => ", this.operationsQueue);
    },
    addEmergentBehavior(item) {
      if (typeof item == "object") {
        this.emergentBehaviors.push(item);
      } else {
        let emergentBehavior = {};
        let id = uuidv4();
        emergentBehavior.emergent_external_id = id;
        emergentBehavior.description = item;
        emergentBehavior.type = "emergentBehavior";
        this.emergentBehaviors.push(emergentBehavior);

        let queuedItem = {};
        queuedItem.type = "element";
        queuedItem.subtype = "emergentBehavior";
        queuedItem.operation = "add";
        queuedItem.emergent_external_id = id;
        queuedItem.description = item;
        this.operationsQueue.push(queuedItem);

        let queuedItem_connection = {};
        queuedItem_connection.type = "connection";
        queuedItem_connection.subtype = "sos/emergentBehavior";
        queuedItem_connection.operation = "add";
        queuedItem_connection.emergent_external_id = id;
        queuedItem_connection.sos_external_id = this.editingSoS.sos_external_id;
        this.operationsQueue.push(queuedItem_connection);
      }
      console.log("emergent Behaviors Features => ", this.emergentBehaviors);
      console.log("operations Queue => ", this.operationsQueue);
    },
    redrawLines() {
      this.ConstituentsBasicFeaturesLines.forEach((item) => {
        // console.log('Constituent/Feature =>>> ', item)
        let color = item.line.color;
        item.line.remove();

        let constituent = this.$refs.constituents.find((constituent) => {
          return constituent.$attrs.id == item.constituent_external_id;
        });

        let basicFeature = this.$refs.basicFeatures.find((basicFeature) => {
          return basicFeature.$attrs.id == item.feature_external_id;
        });

        const line = new LeaderLine(
          LeaderLine.mouseHoverAnchor(constituent.$el),
          basicFeature.$el,
          {
            size: 3,
            color: color,
            startPlug: "disc",
            endPlug: "disc",
            path: "straight",
          }
        );

        item.line = line;
      });
      this.BasicFeaturesEmergentBehaviorsLines.forEach((item) => {
        // console.log('Feature/Behavior =>>> ', item)
        let color = item.line.color;
        item.line.remove();

        let emergentBehavior = this.$refs.emergentBehaviors.find(
          (emergentBehavior) => {
            return emergentBehavior.$attrs.id == item.emergent_external_id;
          }
        );

        let basicFeature = this.$refs.basicFeatures.find((basicFeature) => {
          return basicFeature.$attrs.id == item.feature_external_id;
        });

        const line = new LeaderLine(
          LeaderLine.mouseHoverAnchor(basicFeature.$el),
          emergentBehavior.$el,
          {
            size: 3,
            color: color,
            startPlug: "disc",
            endPlug: "disc",
            path: "straight",
          }
        );

        item.line = line;
      });
    },
    checkConnection() {
      if (this.selectedForCheck.length > 2) {
        this.dialog = true;
        this.selectedForCheck = [];
        this.selectedConstituents = [];
        this.selectedFeatures = [];
        this.selectedBehaviors = [];
      } else if (this.selectedForCheck.length == 2) {
        if (this.selectedForCheck[0].type == "constituent") {
          if (this.selectedForCheck[1].type == "emergentBehavior") {
            this.dialog = true;
            this.selectedForCheck = [];
            this.selectedConstituents = [];
            this.selectedFeatures = [];
            this.selectedBehaviors = [];
          } else {
            let connection = this.ConstituentsBasicFeaturesLines.filter(
              (lineObj) => {
                return (
                  lineObj.constituent_external_id ==
                    this.selectedForCheck[0].constituent_external_id &&
                  lineObj.feature_external_id ==
                    this.selectedForCheck[1].feature_external_id
                );
              }
            );

            if (connection.length == 0) {
              let constituent = this.$refs.constituents.find((constituent) => {
                return (
                  constituent.$attrs.id ==
                  this.selectedForCheck[0].constituent_external_id
                );
              });

              let basicFeature = this.$refs.basicFeatures.find(
                (basicFeature) => {
                  return (
                    basicFeature.$attrs.id ==
                    this.selectedForCheck[1].feature_external_id
                  );
                }
              );

              const line = new LeaderLine(
                LeaderLine.mouseHoverAnchor(constituent.$el),
                basicFeature.$el,
                {
                  size: 3,
                  color: "red",
                  startPlug: "disc",
                  endPlug: "disc",
                  path: "straight",
                }
              );

              let lineObj = {};
              lineObj.constituent_external_id =
                this.selectedForCheck[0].constituent_external_id;
              lineObj.feature_external_id =
                this.selectedForCheck[1].feature_external_id;
              lineObj.line = line;

              //AVALIAR PARA ADICIONAR EM OUTRO ARRAY
              this.ConstituentsBasicFeaturesLines.push(lineObj);

              let queuedItem = {};
              queuedItem.type = "connection";
              queuedItem.subtype = "constituent/basicFeature";
              queuedItem.operation = "add";
              queuedItem.constituent_external_id =
                this.selectedForCheck[0].constituent_external_id;
              queuedItem.feature_external_id =
                this.selectedForCheck[1].feature_external_id;
              this.operationsQueue.push(queuedItem);

              console.log("operations Queue => ", this.operationsQueue);
            } else if (connection.length == 1) {
              connection[0].line.remove();
              this.ConstituentsBasicFeaturesLines.splice(
                this.ConstituentsBasicFeaturesLines.indexOf(connection[0]),
                1
              );

              let queuedItem = {};
              queuedItem.type = "connection";
              queuedItem.subtype = "constituent/basicFeature";
              queuedItem.operation = "remove";
              queuedItem.constituent_external_id =
                connection[0].constituent_external_id;
              queuedItem.feature_external_id =
                connection[0].feature_external_id;
              this.operationsQueue.push(queuedItem);

              console.log("operations Queue => ", this.operationsQueue);
            } else {
              this.dialog = true;
            }

            this.selectedForCheck = [];
            this.selectedConstituents = [];
            this.selectedFeatures = [];
            this.selectedBehaviors = [];
          }
        } else if (this.selectedForCheck[0].type == "emergentBehavior") {
          if (this.selectedForCheck[1].type == "constituent") {
            this.dialog = true;
            this.selectedForCheck = [];
            this.selectedConstituents = [];
            this.selectedFeatures = [];
            this.selectedBehaviors = [];
          } else {
            let connection = this.BasicFeaturesEmergentBehaviorsLines.filter(
              (lineObj) => {
                return (
                  lineObj.emergent_external_id ==
                    this.selectedForCheck[0].emergent_external_id &&
                  lineObj.feature_external_id ==
                    this.selectedForCheck[1].feature_external_id
                );
              }
            );

            if (connection.length == 0) {
              let emergentBehavior = this.$refs.emergentBehaviors.find(
                (emergentBehavior) => {
                  return (
                    emergentBehavior.$attrs.id ==
                    this.selectedForCheck[0].emergent_external_id
                  );
                }
              );

              let basicFeature = this.$refs.basicFeatures.find(
                (basicFeature) => {
                  return (
                    basicFeature.$attrs.id ==
                    this.selectedForCheck[1].feature_external_id
                  );
                }
              );

              const line = new LeaderLine(
                LeaderLine.mouseHoverAnchor(basicFeature.$el),
                emergentBehavior.$el,
                {
                  size: 3,
                  color: "red",
                  startPlug: "disc",
                  endPlug: "disc",
                  path: "straight",
                }
              );

              let lineObj = {};
              lineObj.emergent_external_id =
                this.selectedForCheck[0].emergent_external_id;
              lineObj.feature_external_id =
                this.selectedForCheck[1].feature_external_id;
              lineObj.line = line;

              //AVALIAR PARA ADICIONAR EM OUTRO ARRAY
              this.BasicFeaturesEmergentBehaviorsLines.push(lineObj);

              let queuedItem = {};
              queuedItem.type = "connection";
              queuedItem.subtype = "basicFeature/emergentBehavior";
              queuedItem.operation = "add";
              queuedItem.emergent_external_id =
                this.selectedForCheck[0].emergent_external_id;
              queuedItem.feature_external_id =
                this.selectedForCheck[1].feature_external_id;
              this.operationsQueue.push(queuedItem);

              console.log("operations Queue => ", this.operationsQueue);
            } else if (connection.length == 1) {
              connection[0].line.remove();
              this.BasicFeaturesEmergentBehaviorsLines.splice(
                this.BasicFeaturesEmergentBehaviorsLines.indexOf(connection[0]),
                1
              );

              let queuedItem = {};
              queuedItem.type = "connection";
              queuedItem.subtype = "basicFeature/emergentBehavior";
              queuedItem.operation = "remove";
              queuedItem.emergent_external_id =
                connection[0].emergent_external_id;
              queuedItem.feature_external_id =
                connection[0].feature_external_id;
              this.operationsQueue.push(queuedItem);

              console.log("operations Queue => ", this.operationsQueue);
            } else {
              this.dialog = true;
            }

            this.selectedForCheck = [];
            this.selectedConstituents = [];
            this.selectedFeatures = [];
            this.selectedBehaviors = [];
          }
        } else {
          if (this.selectedForCheck[1].type == "constituent") {
            let connection = this.ConstituentsBasicFeaturesLines.filter(
              (lineObj) => {
                return (
                  lineObj.constituent_external_id ==
                    this.selectedForCheck[1].constituent_external_id &&
                  lineObj.feature_external_id ==
                    this.selectedForCheck[0].feature_external_id
                );
              }
            );

            if (connection.length == 0) {
              let constituent = this.$refs.constituents.find((constituent) => {
                return (
                  constituent.$attrs.id ==
                  this.selectedForCheck[1].constituent_external_id
                );
              });

              let basicFeature = this.$refs.basicFeatures.find(
                (basicFeature) => {
                  return (
                    basicFeature.$attrs.id ==
                    this.selectedForCheck[0].feature_external_id
                  );
                }
              );

              const line = new LeaderLine(
                LeaderLine.mouseHoverAnchor(constituent.$el),
                basicFeature.$el,
                {
                  size: 3,
                  color: "red",
                  startPlug: "disc",
                  endPlug: "disc",
                  path: "straight",
                }
              );

              let lineObj = {};
              lineObj.constituent_external_id =
                this.selectedForCheck[1].constituent_external_id;
              lineObj.feature_external_id =
                this.selectedForCheck[0].feature_external_id;
              lineObj.line = line;

              //AVALIAR PARA ADICIONAR EM OUTRO ARRAY
              this.ConstituentsBasicFeaturesLines.push(lineObj);

              let queuedItem = {};
              queuedItem.type = "connection";
              queuedItem.subtype = "constituent/basicFeature";
              queuedItem.operation = "add";
              queuedItem.feature_external_id =
                this.selectedForCheck[0].feature_external_id;
              queuedItem.constituent_external_id =
                this.selectedForCheck[1].constituent_external_id;
              this.operationsQueue.push(queuedItem);

              console.log("operations Queue => ", this.operationsQueue);
            } else if (connection.length == 1) {
              connection[0].line.remove();
              this.ConstituentsBasicFeaturesLines.splice(
                this.ConstituentsBasicFeaturesLines.indexOf(connection[0]),
                1
              );

              let queuedItem = {};
              queuedItem.type = "connection";
              queuedItem.subtype = "constituent/basicFeature";
              queuedItem.operation = "remove";
              queuedItem.constituent_external_id =
                connection[0].constituent_external_id;
              queuedItem.feature_external_id =
                connection[0].feature_external_id;
              this.operationsQueue.push(queuedItem);

              console.log("operations Queue => ", this.operationsQueue);
            } else {
              this.dialog = true;
            }

            this.selectedForCheck = [];
            this.selectedConstituents = [];
            this.selectedFeatures = [];
            this.selectedBehaviors = [];
          } else {
            let connection = this.BasicFeaturesEmergentBehaviorsLines.filter(
              (lineObj) => {
                return (
                  lineObj.emergent_external_id ==
                    this.selectedForCheck[1].emergent_external_id &&
                  lineObj.feature_external_id ==
                    this.selectedForCheck[0].feature_external_id
                );
              }
            );

            if (connection.length == 0) {
              let emergentBehavior = this.$refs.emergentBehaviors.find(
                (emergentBehavior) => {
                  return (
                    emergentBehavior.$attrs.id ==
                    this.selectedForCheck[1].emergent_external_id
                  );
                }
              );

              let basicFeature = this.$refs.basicFeatures.find(
                (basicFeature) => {
                  return (
                    basicFeature.$attrs.id ==
                    this.selectedForCheck[0].feature_external_id
                  );
                }
              );

              const line = new LeaderLine(
                LeaderLine.mouseHoverAnchor(basicFeature.$el),
                emergentBehavior.$el,
                {
                  size: 3,
                  color: "red",
                  startPlug: "disc",
                  endPlug: "disc",
                  path: "straight",
                }
              );

              let lineObj = {};
              lineObj.emergent_external_id =
                this.selectedForCheck[1].emergent_external_id;
              lineObj.feature_external_id =
                this.selectedForCheck[0].feature_external_id;
              lineObj.line = line;

              //AVALIAR PARA ADICIONAR EM OUTRO ARRAY
              this.BasicFeaturesEmergentBehaviorsLines.push(lineObj);

              let queuedItem = {};
              queuedItem.type = "connection";
              queuedItem.subtype = "basicFeature/emergentBehavior";
              queuedItem.operation = "add";
              queuedItem.feature_external_id =
                this.selectedForCheck[0].feature_external_id;
              queuedItem.emergent_external_id =
                this.selectedForCheck[1].emergent_external_id;
              this.operationsQueue.push(queuedItem);

              console.log("operations Queue => ", this.operationsQueue);
            } else if (connection.length == 1) {
              connection[0].line.remove();
              this.BasicFeaturesEmergentBehaviorsLines.splice(
                this.BasicFeaturesEmergentBehaviorsLines.indexOf(connection[0]),
                1
              );

              let queuedItem = {};
              queuedItem.type = "connection";
              queuedItem.subtype = "basicFeature/emergentBehavior";
              queuedItem.operation = "remove";
              queuedItem.emergent_external_id =
                connection[0].emergent_external_id;
              queuedItem.feature_external_id =
                connection[0].feature_external_id;
              this.operationsQueue.push(queuedItem);

              console.log("operations Queue => ", this.operationsQueue);
            } else {
              this.dialog = true;
            }

            this.selectedForCheck = [];
            this.selectedConstituents = [];
            this.selectedFeatures = [];
            this.selectedBehaviors = [];
          }
        }
      } else {
        // console.log('waiting for more chips...')
      }
    },
    handleColorConstituents(item) {
      const id = item.constituent_external_id;
      if (
        this.selectedConstituents.length == 1 &&
        this.selectedConstituents[0] !== id
      ) {
        this.dialog = true;
        this.selectedForCheck = [];
        this.selectedConstituents = [];
        this.selectedFeatures = [];
        this.selectedBehaviors = [];
      } else {
        const el = this.selectedConstituents.findIndex((el) => el === id);
        if (el < 0) {
          this.selectedConstituents.push(id);
          this.selectedForCheck.push(item);
          this.checkConnection();
        } else {
          this.selectedConstituents.splice(el, 1);
          this.selectedForCheck.splice(item, 1);
        }
      }
    },
    handleColorBasicFeatures(item) {
      const id = item.feature_external_id;
      if (
        this.selectedFeatures.length == 1 &&
        this.selectedFeatures[0] !== id
      ) {
        this.dialog = true;
        this.selectedForCheck = [];
        this.selectedConstituents = [];
        this.selectedFeatures = [];
        this.selectedBehaviors = [];
      } else {
        const el = this.selectedFeatures.findIndex((el) => el === id);
        if (el < 0) {
          this.selectedFeatures.push(id);
          this.selectedForCheck.push(item);
          this.checkConnection();
        } else {
          this.selectedFeatures.splice(el, 1);
          this.selectedForCheck.splice(item, 1);
        }
      }
    },
    handleColorEmergentBehaviors(item) {
      const id = item.emergent_external_id;
      if (
        this.selectedBehaviors.length == 1 &&
        this.selectedBehaviors[0] !== id
      ) {
        this.dialog = true;
        this.selectedForCheck = [];
        this.selectedConstituents = [];
        this.selectedFeatures = [];
        this.selectedBehaviors = [];
      } else {
        const el = this.selectedBehaviors.findIndex((el) => el === id);
        if (el < 0) {
          this.selectedBehaviors.push(id);
          this.selectedForCheck.push(item);
          this.checkConnection();
        } else {
          this.selectedBehaviors.splice(el, 1);
          this.selectedForCheck.splice(item, 1);
        }
      }
    },
    addConnectionSoSConstituentDB(sos_external_id, constituent_external_id) {
      const path = `${process.env.VUE_APP_BASE_URL}/relation/sos_constituent/add`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              sos_external_id: sos_external_id,
              constituent_external_id: constituent_external_id,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    removeConnectionSoSConstituentDB(sos_external_id, constituent_external_id) {
      const path = `${process.env.VUE_APP_BASE_URL}/relation/sos_constituent/delete`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              sos_external_id: sos_external_id,
              constituent_external_id: constituent_external_id,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    addConnectionSoSEmergentBehaviorDB(sos_external_id, emergent_external_id) {
      const path = `${process.env.VUE_APP_BASE_URL}/relation/sos_emergent_behavior/add`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              sos_external_id: sos_external_id,
              emergent_external_id: emergent_external_id,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    removeConnectionSoSEmergentBehaviorDB(
      sos_external_id,
      emergent_external_id
    ) {
      const path = `${process.env.VUE_APP_BASE_URL}/relation/sos_emergent_behavior/delete`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              sos_external_id: sos_external_id,
              emergent_external_id: emergent_external_id,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    addConnectionConstituentBasicFeatureDB(
      constituent_external_id,
      feature_external_id
    ) {
      const path = `${process.env.VUE_APP_BASE_URL}/relation/constituent_basic_feature/add`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              constituent_external_id: constituent_external_id,
              feature_external_id: feature_external_id,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    removeConnectionConstituentBasicFeatureDB(
      constituent_external_id,
      feature_external_id
    ) {
      const path = `${process.env.VUE_APP_BASE_URL}/relation/constituent_basic_feature/delete`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              constituent_external_id: constituent_external_id,
              feature_external_id: feature_external_id,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    addConnectionBasicFeatureEmergentBehaviorDB(
      feature_external_id,
      emergent_external_id
    ) {
      const path = `${process.env.VUE_APP_BASE_URL}/relation/basic_feature_emergent_behavior/add`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              emergent_external_id: emergent_external_id,
              feature_external_id: feature_external_id,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    removeConnectionBasicFeatureEmergentBehaviorDB(
      feature_external_id,
      emergent_external_id
    ) {
      const path = `${process.env.VUE_APP_BASE_URL}/relation/basic_feature_emergent_behavior/delete`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              emergent_external_id: emergent_external_id,
              feature_external_id: feature_external_id,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    addSoSDB(sos_external_id, sos_name) {
      const path = `${process.env.VUE_APP_BASE_URL}/sos/add`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: { sos_id: sos_external_id, sos_name: sos_name },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    addConstituentDB(constituent_external_id, constituent_name) {
      const path = `${process.env.VUE_APP_BASE_URL}/constituents/add`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              constituent_id: constituent_external_id,
              constituent_name: constituent_name,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    addBasicFeatureDB(feature_external_id, description) {
      const path = `${process.env.VUE_APP_BASE_URL}/basic_features/add`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              feature_id: feature_external_id,
              description: description,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    addEmergentBehaviorDB(emergent_external_id, description) {
      const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/add`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, {
            params: {
              emergent_id: emergent_external_id,
              description: description,
            },
          })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    updateSoSDB(sos_external_id, sos_name) {
      const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/update`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, { params: { sos_name: sos_name } })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    updateConstituentDB(constituent_external_id, constituent_name) {
      const path = `${process.env.VUE_APP_BASE_URL}/constituents/${constituent_external_id}/update`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, { params: { constituent_name: constituent_name } })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    updateBasicFeatureDB(feature_external_id, description) {
      const path = `${process.env.VUE_APP_BASE_URL}/basic_features/${feature_external_id}/update`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, { params: { description: description } })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    updateEmergentBehaviorDB(emergent_external_id, description) {
      const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/${emergent_external_id}/update`;

      return new Promise((resolve, reject) => {
        axios
          .get(path, { params: { description: description } })
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    removeSoSDB(sos_external_id) {
      const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/delete`;

      return new Promise((resolve, reject) => {
        axios
          .get(path)
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    removeConstituentDB(constituent_external_id) {
      const path = `${process.env.VUE_APP_BASE_URL}/constituents/${constituent_external_id}/delete`;

      return new Promise((resolve, reject) => {
        axios
          .get(path)
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    removeBasicFeatureDB(feature_external_id) {
      const path = `${process.env.VUE_APP_BASE_URL}/basic_features/${feature_external_id}/delete`;

      return new Promise((resolve, reject) => {
        axios
          .get(path)
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    removeEmergentBehaviorDB(emergent_external_id) {
      const path = `${process.env.VUE_APP_BASE_URL}/emergent_behaviors/${emergent_external_id}/delete`;

      return new Promise((resolve, reject) => {
        axios
          .get(path)
          .then((res) => {
            console.log(res.data);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    getSoS() {
      const path = `${process.env.VUE_APP_BASE_URL}/sos/get`;
      axios
        .get(path)
        .then((res) => {
          this.sos = res.data;

          this.sos.forEach((sos) => {
            sos.type = "sos";
          });
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
    getConstituents() {
      const path = `${process.env.VUE_APP_BASE_URL}/constituents/get`;
      axios
        .get(path)
        .then((res) => {
          this.availableConstituents = res.data;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
    getBasicFeatures() {
      const path = `${process.env.VUE_APP_BASE_URL}/basic_features/get`;
      axios
        .get(path)
        .then((res) => {
          this.availableBasicFeatures = res.data;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
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
    getConstituentsFromSoS(sos_external_id, el) {
      this.ConstituentsBasicFeaturesLines.forEach((line) => line.remove());
      this.ConstituentsBasicFeaturesLines = [];
      this.BasicFeaturesEmergentBehaviorsLines = [];
      const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/get`;

      return new Promise((resolve, reject) => {
        axios
          .get(path)
          .then((res) => {
            // console.log('Loaded constituents...')
            this.constituents = res.data;

            this.constituents.forEach((constituent) => {
              constituent.type = "constituent";
            });

            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.error(error);
          });
      });
    },
    getBasicFeaturesFromSoS(sos_external_id) {
      this.ConstituentsBasicFeaturesLines.forEach((line) => line.remove());
      this.ConstituentsBasicFeaturesLines = [];
      this.BasicFeaturesEmergentBehaviorsLines = [];
      const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/basic_features/get`;

      return new Promise((resolve, reject) => {
        axios
          .get(path)
          .then((res) => {
            this.basicFeatures = res.data;
            // console.log('Loaded basic features...')

            this.basicFeatures.forEach((basicFeature) => {
              basicFeature.type = "basicFeature";
            });

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
    getEmergentBehaviorsFromSoS(sos_external_id) {
      this.BasicFeaturesEmergentBehaviorsLines.forEach((line) => line.remove());
      this.ConstituentsBasicFeaturesLines = [];
      this.BasicFeaturesEmergentBehaviorsLines = [];
      const path = `${process.env.VUE_APP_BASE_URL}/sos/${sos_external_id}/constituents/basic_features/emergent_behaviors/get`;

      return new Promise((resolve, reject) => {
        axios
          .get(path)
          .then((res) => {
            this.emergentBehaviors = res.data;
            // console.log('Loaded emergent behaviors...')

            this.emergentBehaviors.forEach((emergentBehavior) => {
              emergentBehavior.type = "emergentBehavior";
            });

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
    getRelationsConstituentsBasicFeatures() {
      let payload = {
        constituent_list: this.constituents,
        features_list: this.basicFeatures,
      };
      const path_addRelationsConstituentsBasicFeatures = `${process.env.VUE_APP_BASE_URL}/relation/constituent_basic_feature/post`;
      return new Promise((resolve, reject) => {
        axios({
          url: path_addRelationsConstituentsBasicFeatures,
          method: "post",
          data: payload,
        })
          .then((res) => {
            let relations = res.data;
            relations.forEach((relation) => {
              let constituent = this.$refs.constituents.find((constituent) => {
                return (
                  constituent.$attrs.id == relation.constituent_external_id
                );
              });

              let basicFeature = this.$refs.basicFeatures.find(
                (basicFeature) => {
                  return basicFeature.$attrs.id == relation.feature_external_id;
                }
              );

              const line = new LeaderLine(
                LeaderLine.mouseHoverAnchor(constituent.$el),
                basicFeature.$el,
                {
                  size: 3,
                  color: "#000000",
                  startPlug: "disc",
                  endPlug: "disc",
                  path: "straight",
                }
              );

              let lineObj = {};
              lineObj.constituent_external_id =
                relation.constituent_external_id;
              lineObj.feature_external_id = relation.feature_external_id;
              lineObj.line = line;

              this.ConstituentsBasicFeaturesLines.push(lineObj);
              resolve();
            });
          })
          .catch((error) => {
            this.errorDialog = true;
            console.log(
              "ERROR ON ADD RELATION CONSTITUENTS/BASIC FEATURES =>>> ",
              error
            );
          });
      });
    },
    getRelationsBasicFeaturesEmergentBehaviors() {
      let payload = {
        features_list: this.basicFeatures,
        emergents_list: this.emergentBehaviors,
      };
      const path_addRelationsBasicFeaturesEmergentBehaviors = `${process.env.VUE_APP_BASE_URL}/relation/basic_feature_emergent_behavior/post`;
      return new Promise((resolve, reject) => {
        axios({
          url: path_addRelationsBasicFeaturesEmergentBehaviors,
          method: "post",
          data: payload,
        })
          .then((res) => {
            let relations = res.data;
            relations.forEach((relation) => {
              let basicFeature = this.$refs.basicFeatures.find(
                (basicFeature) => {
                  return basicFeature.$attrs.id == relation.feature_external_id;
                }
              );

              let emergentBehavior = this.$refs.emergentBehaviors.find(
                (emergentBehavior) => {
                  return (
                    emergentBehavior.$attrs.id == relation.emergent_external_id
                  );
                }
              );

              const line = new LeaderLine(
                LeaderLine.mouseHoverAnchor(basicFeature.$el),
                emergentBehavior.$el,
                {
                  size: 3,
                  color: "#000000",
                  startPlug: "disc",
                  endPlug: "disc",
                  path: "straight",
                }
              );

              let lineObj = {};
              lineObj.feature_external_id = relation.feature_external_id;
              lineObj.emergent_external_id = relation.emergent_external_id;
              lineObj.line = line;

              this.BasicFeaturesEmergentBehaviorsLines.push(lineObj);
              resolve();
            });
          })
          .catch((error) => {
            this.errorDialog = true;
            console.log(
              "ERROR ON ADD RELATION CONSTITUENTS/BASIC FEATURES =>>> ",
              error
            );
          });
      });
    },
    loadSoS(sos_external_id) {
      this.editingSoS = this.sos.find((sos) => {
        return sos.sos_external_id == sos_external_id;
      });
      console.log("editingSoS => ", this.editingSoS);
      this.clearAll();
      this.sos = [];
      this.getSoS();
      this.getConstituentsFromSoS(sos_external_id).then((result) => {
        this.getBasicFeaturesFromSoS(sos_external_id).then((result) => {
          this.getEmergentBehaviorsFromSoS(sos_external_id).then((result) => {
            this.getRelationsConstituentsBasicFeatures().then((result) => {
              this.getRelationsBasicFeaturesEmergentBehaviors().then(
                (result) => {
                  // console.log('this.ConstituentsBasicFeaturesLines =>>> ', this.ConstituentsBasicFeaturesLines)
                  // console.log('this.BasicFeaturesEmergentBehaviorsLines =>>> ', this.BasicFeaturesEmergentBehaviorsLines)
                  // console.log('DONE!')
                }
              );
            });
          });
        });
      });
    },
    clearAll() {
      this.ConstituentsBasicFeaturesLines.forEach((item) => {
        // console.log('Constituent/Feature =>>> ', item)
        item.line.remove();
      });
      this.BasicFeaturesEmergentBehaviorsLines.forEach((item) => {
        // console.log('Feature/Behavior =>>> ', item)
        item.line.remove();
      });

      this.constituents = [];
      this.basicFeatures = [];
      this.emergentBehaviors = [];
      this.ConstituentsBasicFeaturesLines = [];
      this.BasicFeaturesEmergentBehaviorsLines = [];

      this.availableConstituents = [];
      this.availableBasicFeatures = [];
      this.availableEmergentBehaviors = [];

      this.addingConstituent = null;
      this.constituentNewName = null;

      this.addingFeature = null;
      this.featureNewDescription = null;

      this.addingEmergent = null;
      this.emergentNewDescription = null;

      this.addingSoS = null;
      this.sosNewName = null;

      this.operationsQueue = [];

      this.selectedSoS = null;
      this.selectedConstituent = null;
      this.selectedBasicFeature = null;
      this.selectedEmergentBehavior = null;

      this.selectedConstituents = [];
      this.selectedFeatures = [];
      this.selectedBehaviors = [];
      this.selectedForCheck = [];
    },
    removeConstituent(constituent, index) {
      this.ConstituentsBasicFeaturesLines.forEach((item) => {
        item.line.remove();
      });
      this.ConstituentsBasicFeaturesLines = [];
      this.constituents.splice(index, 1);
      this.getRelationsConstituentsBasicFeatures();

      let queuedItem = {};
      queuedItem.constituent_external_id = constituent.constituent_external_id;
      queuedItem.constituent_name = constituent.constituent_name;
      queuedItem.type = "element";
      queuedItem.subtype = constituent.type;
      queuedItem.operation = "remove";

      this.operationsQueue.push(queuedItem);
      console.log("constituents => ", this.constituents);
      console.log("operations Queue => ", this.operationsQueue);
    },
    removeBasicFeature(feature, index) {
      this.ConstituentsBasicFeaturesLines.forEach((item) => {
        console.log("line Constituents/Features =>>> ", item);
        item.line.remove();
      });
      this.BasicFeaturesEmergentBehaviorsLines.forEach((item) => {
        console.log("line Features/Behaviors =>>> ", item);
        item.line.remove();
      });
      this.ConstituentsBasicFeaturesLines = [];
      this.BasicFeaturesEmergentBehaviorsLines = [];
      this.basicFeatures.splice(index, 1);
      this.getRelationsConstituentsBasicFeatures();
      this.getRelationsBasicFeaturesEmergentBehaviors();

      let queuedItem = {};
      queuedItem.feature_external_id = feature.feature_external_id;
      queuedItem.description = feature.description;
      queuedItem.type = "element";
      queuedItem.subtype = feature.type;
      queuedItem.operation = "remove";

      this.operationsQueue.push(queuedItem);
      console.log("basic Features => ", this.basicFeatures);
      console.log("operations Queue => ", this.operationsQueue);
    },
    removeEmergentBehavior(behavior, index) {
      this.BasicFeaturesEmergentBehaviorsLines.forEach((item) => {
        item.line.remove();
      });
      this.BasicFeaturesEmergentBehaviorsLines = [];
      this.emergentBehaviors.splice(index, 1);
      this.getRelationsBasicFeaturesEmergentBehaviors();

      let queuedItem = {};
      queuedItem.emergent_external_id = behavior.emergent_external_id;
      queuedItem.description = behavior.description;
      queuedItem.type = "element";
      queuedItem.subtype = behavior.type;
      queuedItem.operation = "remove";

      this.operationsQueue.push(queuedItem);
      console.log("emergent Behaviors => ", this.emergentBehaviors);
      console.log("operations Queue => ", this.operationsQueue);
    },
  },
};
</script>

<style lang="scss">
.manager {
  $self: &;
  height: calc(100vh - 160px);
  display: grid;
  grid-template-columns: repeat(4, 1fr);
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

  .h-100 {
    height: 100%;
  }
}

.v-chip.v-size--default {
  height: auto !important;
  min-height: 32px;
}

.v-chip {
  white-space: normal !important;
  text-align: left;

  &__content {
    justify-content: space-between;
    width: 100%;
  }
}
</style>
