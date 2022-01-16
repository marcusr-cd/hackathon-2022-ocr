<template>
  <div class="main">
    <h1 class="text-4xl font-bold">Spring OCR POC</h1>
    <div v-if="step === 1">
      <BasicData :user-data="userData" @submit="saveForm" />
    </div>
    <div v-if="step === 2">
      <h2 class="text-2xl font-bold mb-10">Upload your documents</h2>
      <div class="main-steps mx-auto mb-10">
        <Step docName="Proof of Address" />
      </div>
    </div>
    <br />

    <!-- <input type="text" v-model="input1" />
    <input type="text" v-model="input2" /> -->
    <!-- <span>{{ inputSimilarity }}</span> -->

    <!-- <div class="loading" v-if="flooredProgress > 0">
      {{ status }}
      <br />
      Progress: {{ flooredProgress }}%
    </div> -->
  </div>
</template>

<script>
import BasicData from "./BasicData.vue";
import Step from "./Step.vue";
// import similarity from "../mixins/stringHelpers";

export default {
  name: "Main",

  components: { Step, BasicData },

  data() {
    return {
      step: 1,
      userData: undefined,
      documents: {
        poa: undefined,
      },
    };
  },

  computed: {
    // flooredProgress() {
    //   return Math.floor(this.progress * 100);
    // },
    // inputSimilarity() {
    //   return similarity(this.input1, this.input2);
    // },
  },

  methods: {
    nextStep() {
      this.step++;
    },

    saveForm(data) {
      this.userData = data
      this.nextStep()
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
