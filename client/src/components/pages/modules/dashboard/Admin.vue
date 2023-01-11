<template>
  <div class="admin">
    <v-container>
      <v-row>
        <v-col>
          <div class="admin__group">
            <label class="admin__label">Exportar Base de Dados</label>
            <div class="admin__behaviors">
              <v-btn color="#A4BE7B" dark @click="dumpDatabase()"
                >Dump Database</v-btn
              >
            </div>
          </div>
        </v-col>
        <v-col>
          <div class="admin__group">
            <label class="admin__label">Restaurar Base de Dados</label>
            <div class="admin__behaviors d-flex">
              <v-file-input
                multiple
                hide-input
                truncate-length="15"
                v-model="files"
                @change="setInputFiles(files)"
                style="padding-top: 0; margin-top: 0"
              />
              <v-btn
                color="#A4BE7B"
                dark
                @click="
                  dialog = true;
                  restoreDatabase();
                "
              >
                Restore Database
              </v-btn>
            </div>
          </div>
        </v-col>
        <v-col>
          <div class="admin__group">
            <label class="admin__label">Remover Base de Dados</label>
            <div class="admin__behaviors">
              <v-btn
                color="#A4BE7B"
                dark
                @click="
                  dialog = true;
                  dropDatabase();
                "
              >
                Drop Database
              </v-btn>
            </div>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <div class="admin__group">
            <label class="admin__label">Treinar Modelo</label>
            <div class="admin__behaviors">
              <v-btn
                :disabled="dialog"
                :loading="dialog"
                color="#A4BE7B"
                dark
                @click="
                  dialog = true;
                  trainModel();
                "
              >
                Train Model
              </v-btn>
            </div>
          </div>
        </v-col>
        <v-col>
          <div class="admin__group">
            <label class="admin__label">Salvar Diretório de Dados</label>
            <div class="admin__behaviors">
              <v-btn
                :disabled="dialog"
                :loading="dialog"
                color="#A4BE7B"
                dark
                @click="
                  dialog = true;
                  saveEntireDirectory();
                "
              >
                Save Directory
              </v-btn>
            </div>
          </div>
        </v-col>
        <v-col>
          <div class="admin__group">
            <label class="admin__label">Resetar Plataforma</label>
            <div class="admin__behaviors">
              <v-btn
                :disabled="dialog"
                :loading="dialog"
                color="#A4BE7B"
                dark
                @click="
                  dialog = true;
                  resetPlatform();
                "
              >
                Reset Platform
              </v-btn>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>

    <v-dialog v-model="dialog" hide-overlay persistent width="300">
      <v-card color="#A4BE7B" dark>
        <v-card-text>
          Processing request...
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>

    <v-dialog transition="dialog-top-transition" max-width="600">
      <template v-slot:default="errorDialog">
        <v-card>
          <v-toolbar color="#A4BE7B" dark>Error</v-toolbar>
          <v-card-text>
            <div class="text-h5 pa-12">Sorry, an error occurred!</div>
          </v-card-text>
          <v-card-actions class="justify-end">
            <v-btn text @click="errorDialog = false">Close</v-btn>
          </v-card-actions>
        </v-card>
      </template>
    </v-dialog>

    <v-dialog
      v-model="successDialog"
      transition="dialog-top-transition"
      max-width="600"
    >
      <v-card>
        <v-toolbar color="#A4BE7B" dark>Success</v-toolbar>
        <v-card-text>
          <div class="text-h5 pa-12">Request processed successfully!</div>
        </v-card-text>
        <v-card-actions class="justify-end">
          <v-btn text @click="successDialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
import { saveAs } from "file-saver";
import store from "@/store";

export default {
  data: () => ({
    dialog: false,
    files: [],
    readers: [],
    errorDialog: false,
    successDialog: false,
  }),
  methods: {
    resetPlatform() {
      const path_reset = `${process.env.VUE_APP_BASE_URL}/database/reset`;
      const path_processing = `${process.env.VUE_APP_BASE_URL}/database/process`;
      axios
        .get(path_reset)
        .then((res) => {
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
              console.log("Plataform reseted successfully!");
              this.dialog = false;
              this.successDialog = true;
            })
            .catch((error) => {
              console.error(error);
              this.dialog = false;
              this.errorDialog = true;
            });
        })
        .catch((error) => {
          console.error(error);
          this.dialog = false;
          this.errorDialog = true;
        });
    },
    trainModel() {
      const path_processing = `${process.env.VUE_APP_BASE_URL}/database/process`;
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
          console.log("Model trained successfully!");
          this.dialog = false;
          this.successDialog = true;
        })
        .catch((error) => {
          console.error(error);
          this.dialog = false;
          this.errorDialog = true;
        });
    },
    str2bytes(str) {
      var bytes = new Uint8Array(str.length);
      for (var i = 0; i < str.length; i++) {
        bytes[i] = str.charCodeAt(i);
      }
      return bytes;
    },
    dumpDatabase() {
      const path_dump = `${process.env.VUE_APP_BASE_URL}/database/dump`;
      axios
        .post(path_dump)
        .then((res) => {
          // console.log(res);
          var xhr = new XMLHttpRequest();
          xhr.open("POST", path_dump, true);
          xhr.responseType = "blob";
          xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
              var blob = xhr.response;
              saveAs(blob, "dump.zip");
            }
          };
          xhr.send();
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
    saveEntireDirectory() {
      const path_save = `${process.env.VUE_APP_BASE_URL}/database/saveall`;
      axios
        .post(path_save)
        .then((res) => {
          // console.log(res);
          var xhr = new XMLHttpRequest();
          xhr.open("POST", path_save, true);
          xhr.responseType = "blob";
          xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
              var blob = xhr.response;
              saveAs(blob, "shared_folder.zip");
            }
          };
          xhr.send();
          this.dialog = false;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
    setInputFiles(inputs) {
      this.files = inputs;
      console.log("INPUTS => ", this.files);
    },
    restoreDatabase() {
      const API_ENDPOINT = `${process.env.VUE_APP_BASE_URL}/database/restore`;

      console.log("Submitting file for upload...");
      let formData = new FormData();
      this.files.forEach((file) => {
        formData.append("file", file);
      });

      console.log("formData => ", formData);

      axios
        .post(API_ENDPOINT, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          timeout: 5000,
        })
        .then((response) => {
          console.log("File upload successful!");
          console.log(response);
          this.dialog = false;
          this.successDialog = true;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.log("File upload failed.");
          console.error(error);
        });
    },
    restoreFile(file, index) {
      let payload = {
        file: file,
      };
      // console.log('Writing inputs...')
      // console.log(inputs)
      const path_restore = `${process.env.VUE_APP_BASE_URL}/database/restore`;
      return new Promise((resolve, reject) => {
        axios({
          url: path_restore,
          method: "post",
          data: payload,
          headers: {
            "Content-Type": "multipart/form-data",
          },
          responseType: "blob",
        })
          .then((res) => {
            console.log("FILE RESTORED SUCCESSFULLY. INDEX => ", index);
            resolve();
          })
          .catch((error) => {
            this.errorDialog = true;
            console.log("ERROR ON IMPORTING FILE =>>> ", error);
          });
      });
    },
    dropDatabase() {
      const path_drop = `${process.env.VUE_APP_BASE_URL}/database/drop`;
      axios
        .get(path_drop)
        .then((res) => {
          console.log("Database droped successfully!");
          this.dialog = false;
          this.successDialog = true;
        })
        .catch((error) => {
          this.errorDialog = true;
          console.error(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.admin {
  $self: &;
  // height: calc(100vh - 160px);
  display: grid;
  // grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  background-color: #dfe8cc;
  padding: 10px;

  & > div {
    flex: 1 0 100%;
  }

  &__group {
    padding: 10px;
    background-color: #eee;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
    border-radius: 6px;
    height: fit-content;

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
      width: 100%;
      padding: 10px;
    }
  }

  .d-flex {
    display: flex;
  }
}
</style>
