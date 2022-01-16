<template>
  <div class="step max-w-800 flex flex-row">
    <div class="step__file">
      <h2 class="step__label text-2xl mr-10">{{docName}}:</h2>
      <input
        type="file"
        id="poa"
        accept="image/png, image/jpeg"
        @change="preloadFile"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "Step",

  props: {
    docName: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      file: undefined,
      progress: 0,
    };
  },

  computed: {
    flooredProgress() {
      return Math.floor(this.progress * 100);
    },
  },

  methods: {},
};
</script>

<style scoped lang="scss">
.step{
    &__file{
        display: flex;
        align-items: center;
    }

    &__label{

    }
}
</style>
