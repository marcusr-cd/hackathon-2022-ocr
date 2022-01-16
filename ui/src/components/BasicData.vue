<template>
  <div class="basic-data">
    <h2 class="text-2xl font-bold my-5">Fill your basic data:</h2>
    <form class="flex flex-col items-center">
      <div class="form-row">
        <label for="" class="basic-data__input">
          <span>First Name</span>
          <input
            placeholder="John"
            type="text"
            name="firstName"
            v-model="userData.firstName"
          />
        </label>
        <label for="" class="basic-data__input">
          <span>Last Name</span>
          <input
            placeholder="Doe"
            type="text"
            name="lastName"
            v-model="userData.lastName"
          />
        </label>
      </div>
      <div class="w-full">
        <label for="" class="basic-data__input">
          <span>Address</span>
          <input
            placeholder="123 Street Name"
            type="text"
            name="street"
            v-model="userData.address.street"
          />
        </label>
      </div>

      <div class="form-row">
        <label for="" class="basic-data__input">
          <span>City</span>
          <input
            placeholder="Vancouver"
            type="text"
            name="City"
            v-model="userData.address.City"
          /> </label
        ><label for="" class="basic-data__input">
          <span>Province</span>
          <input
            placeholder="BC"
            type="text"
            name="province"
            v-model="userData.address.province"
          />
        </label>
      </div>
      <button class="button mt-10" type="button" @click="submit">
        Next Step
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: "BasicData",

  data() {
    return {
      userData: {
        firstName: "",
        lastName: "",
        address: {
          street: "",
          city: "",
          province: "",
        },
      },
    };
  },

  methods: {
    submit() {
      this.$emit("submit", this.userData);
    },
  },
};
</script>

<style scoped lang="scss">
.basic-data {
  @apply mx-auto;
  max-width: 400px;

  &__input {
    @apply flex flex-col items-start mb-5 w-full;

    input {
      @apply w-full rounded-lg;
    }
  }

  .form-row {
    @apply flex justify-between w-full;
    grid-column-gap: 20px;
  }
}
</style>
