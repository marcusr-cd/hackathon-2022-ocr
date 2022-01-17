<template>
  <div class="main">
    <h1 class="text-4xl font-bold">Spring OCR POC</h1>
    <div v-if="step === 1">
      <BasicData :user-data="userData" @submit="saveForm" />
    </div>
    <div v-if="step === 2">
      <h2 class="text-2xl font-bold mb-10">Upload your documents</h2>
      <div class="main-steps mx-auto mb-10">
        <FileStep docName="Proof of Address" @submit="saveFile" />
      </div>
    </div>
    <div v-if="step === 3">
      <h2
        v-if="ocrMatching.name < 40 || ocrMatching.address < 40"
        class="text-2xl font-bold my-5"
      >
        Hey!
      </h2>
      <div v-if="ocrMatching.name < 40">
        <p>
          The file you attached as proof of address doesn't fully match your
          name:
        </p>
        <h3 class="text-xl font-bold">
          {{ fullName }} vs {{ this.ocrResponse.name }}
        </h3>
        <p>
          Please check if the file you uploaded is a correct valid document or
          it has your name in it
        </p>
      </div>
      <div v-if="ocrMatching.address < 40" class="mt-5">
        <p>
          The file you attached as proof of address doesn't fully match your
          address:
        </p>
        <h3 class="text-xl font-bold">
          {{ fullAddress }} vs {{ this.ocrResponse.address }}
        </h3>
        <p>
          Please check if the file you uploaded is a correct valid document or
          it has your full address in it
        </p>
      </div>
      <div v-else>
        <h2 class="text-2xl font-bold my-10">Thanks for applying!</h2>
      </div>
    </div>
    <br />
  </div>
</template>

<script>
import BasicData from "./BasicData.vue";
import FileStep from "./FileStep.vue";
import axios from "axios";
import { similarity } from "../mixins/stringHelpers";

export default {
  name: "Main",

  components: { FileStep, BasicData },

  data() {
    return {
      step: 1,
      userData: undefined,
      documents: {
        poa: undefined,
      },
      ocrResponse: {
        name: "",
        billing_date: "",
        address: "",
      },
      ocrMatching: {
        name: 0,
        address: 0,
      },
    };
  },

  computed: {
    fullName() {
      return `${this.userData.firstName} ${this.userData.lastName}`.toUpperCase();
    },
    fullAddress() {
      return `${this.userData.address.street} ${this.userData.address.city} ${this.userData.address.province}`.toUpperCase();
    },
  },

  methods: {
    nextStep() {
      this.step++;
    },

    saveForm(data) {
      this.userData = data;
      this.nextStep();
    },

    saveFile(file) {
      this.documents.poa = file;
      this.submitForm();
    },

    async submitForm() {
      const formData = new FormData();
      formData.append("image", this.documents.poa);
      axios
        .post("http://localhost:5000", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(({ data }) => {
          console.log(data);
          this.ocrResponse = { ...data };
        })
        .then(() => {
          this.calculateDataMatching();
          this.nextStep();
        });
    },

    calculateDataMatching() {
      this.ocrMatching.name = Math.floor(
        similarity(this.fullName, this.ocrResponse.name) * 100,
        2
      );
      this.ocrMatching.address = Math.floor(
        similarity(this.fullAddress, this.ocrResponse.address) * 100,
        2
      );
    },
  },
};
</script>

<style scoped lang="scss">
.main {
  &-steps {
    @apply flex items-center flex-col my-5 mx-auto;
  }
}
</style>
