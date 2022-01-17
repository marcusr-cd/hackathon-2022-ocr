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
    <br />
  </div>
</template>

<script>
import BasicData from "./BasicData.vue";
import FileStep from "./FileStep.vue";
import axios from "axios";

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
    };
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
      axios.post("https://localhost:5000", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
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
