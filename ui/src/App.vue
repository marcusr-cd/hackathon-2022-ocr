<template>
  <div class="main container mx-auto">
    <Main />
  </div>
</template>

<script>
import Main from './components/Main.vue'

export default {
  name: 'App',
  components: {
    Main
  }
}
</script>

<style lang="scss">

#app {
    padding: 90px 0;
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  
  :root{
    --purple: #5957C1;
    --purple2: #7378D8;
    --green: #06BE9E;
  }
  
  .button{
    @apply text-white py-1 px-4 h-12 w-full;
    @apply inline-flex items-center justify-center;
    @apply rounded-2xl text-2xl duration-500;
    background-color: var(--purple);
  
    &:hover{
      background-color: var(--purple2);
    }
  }
</style>