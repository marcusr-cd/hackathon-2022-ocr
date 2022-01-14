<template>
  <div class="container">
    <h1>Spring OCR</h1>
    <h1>Upload a file to read its contents!</h1>
    <input
      type="file"
      id="file"
      accept="image/png, image/jpeg"
      @change="preloadFile"
    />
    <button v-if="file" class="loadButton" @click="readImage">
      Read from image!
    </button>

    <div class="loading" v-if="flooredProgress > 0">
      {{ status }}
      <br />
      Progress: {{ flooredProgress }}%
    </div>

    <div v-if="imageText">
      <h2>Full text:</h2>
      <p class="imageContent">{{ imageText }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: "Main",

  data() {
    return {
      file: undefined,
      status: "",
      progress: 0,
      imageText: "",
    };
  },

  computed: {
    flooredProgress() {
      return Math.floor(this.progress * 100);
    },
  },

  methods: {

  },
};
</script>

<style scoped>
.container {
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 800px;
}

.loadButton {
  margin: 35px 0;
}

.imageContent {
  white-space: pre-line;
}
</style>
