<template>
    <div>
        <v-btn
        elevation="2"
        @click="dumpDatabase()"
        >Dump Database</v-btn>

        <v-row>
            <v-col>
                <v-file-input
                    multiple
                    hide-input
                    truncate-length="15"
                    v-model="files"
                    @change="setInputFiles(files)"
                ></v-file-input>
            </v-col>
            <v-col>
                <v-btn
                elevation="2"
                @click="restoreDatabase()"
                > Restore Database</v-btn>
            </v-col>
        </v-row>

      <v-btn
        elevation="2"
        @click="dropDatabase()"
        >Drop Database</v-btn>

        <v-btn
            :disabled="dialog"
            :loading="dialog"
            class="white--text"
            color="purple darken-2"
            @click="dialog = true; resetPlatform()"
            >
            Reset Platform
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
                Reseting platform...
                <v-progress-linear
                    indeterminate
                    color="white"
                    class="mb-0"
                ></v-progress-linear>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import axios from 'axios';
import { saveAs } from 'file-saver';

  export default {
    data: () => ({
        dialog: false,
        files: [],
        readers: []
    }),
    methods: {
        resetPlatform() {
            const path_reset = `${process.env.VUE_APP_BASE_URL}/database/reset`;
            const path_processing = `${process.env.VUE_APP_BASE_URL}/database/process`;
            axios.get(path_reset)
                .then((res) => {
                    axios.get(path_processing)
                        .then((res) => {                            
                            console.log('Plataform reseted successfully!')
                            this.dialog = false
                        })
                        .catch((error) => {
                            console.error(error);
                            this.dialog = false
                        });

                })
                .catch((error) => {
                    console.error(error);
                    this.dialog = false
                });
        },
        str2bytes (str) {
            var bytes = new Uint8Array(str.length);
            for (var i=0; i<str.length; i++) {
                bytes[i] = str.charCodeAt(i);
            }
            return bytes;
        },
        dumpDatabase() {
            const path_reset = `${process.env.VUE_APP_BASE_URL}/database/dump`;
            axios.post(path_reset)
            .then(res => {
                // console.log(res);
                var xhr = new XMLHttpRequest();
                xhr.open('POST', path_reset, true);
                xhr.responseType = "blob";
                xhr.onreadystatechange = function (){
                    if (xhr.readyState === 4) {
                        var blob = xhr.response;
                        saveAs(blob, "dump.zip");
                    }
                };
                xhr.send();
            }).catch(error => {
                console.error(error);
            });
        },
        setInputFiles(inputs){
            this.files = inputs
            console.log('INPUTS => ', this.files)
        },
        restoreDatabase() {
            const API_ENDPOINT = `${process.env.VUE_APP_BASE_URL}/database/restore`;

            console.log("Submitting file for upload...");
            let formData = new FormData();
            this.files.forEach(file => {
                formData.append('file', file);
            })
            
            console.log('formData => ', formData)

            axios.post(API_ENDPOINT, formData, {
                headers: { 
                'Content-Type': 'multipart/form-data' 
                },
                timeout: 5000
            })
            .then(response => {
                console.log("File upload successful!");
                console.log(response);
            }).catch(error => {
                console.log("File upload failed.");
                console.error(error);
            });
            
        },
        restoreFile(file, index){
            let payload = {
                file: file
            }
            // console.log('Writing inputs...')
            // console.log(inputs)
            const path_restore = `${process.env.VUE_APP_BASE_URL}/database/restore`;
            return new Promise((resolve, reject) => {
                axios({
                    url: path_restore,
                    method: 'post',
                    data: payload,
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                    responseType: 'blob'
                    })
                    .then((res) => {
                        console.log('FILE RESTORED SUCCESSFULLY. INDEX => ', index)
                        resolve()
                    })
                    .catch((error) => {
                        console.log('ERROR ON IMPORTING FILE =>>> ', error);
                    });
            })
        },
        dropDatabase() {
            const path_reset = `${process.env.VUE_APP_BASE_URL}/database/drop`;
            axios.get(path_reset)
                .then((res) => {
                    console.log('Database droped successfully!')
                })
                .catch((error) => {
                    console.error(error);
                });
        }
    }
}
</script>
