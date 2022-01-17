<template>
  <div class="step max-w-800">
    <div class="step__file">
      <h2 class="step__label text-2xl mr-10">{{ docName }}:</h2>
      <input
        type="file"
        id="poa"
        accept="image/png, image/jpeg, application/pdf"
        @change="preloadFile"
      />
    </div>
    <button class="button mt-10" type="button" @click="submit">Submit</button>
  </div>
</template>

<script>
export default {
  name: "FileStep",

  props: {
    docName: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      file: undefined,
    };
  },

  methods: {
    preloadFile(event){
      const file = event.target.files[0]
      this.file = file
    },
    
    submit() {
      this.$emit("submit", this.file);
    },
  },
};
</script>

<style scoped lang="scss">
.step {
  &__file {
    @apply flex items-center;
  }

  &__label {
  }
}
</style>
