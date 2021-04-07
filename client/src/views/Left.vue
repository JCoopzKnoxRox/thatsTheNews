<template lang="html">
  <div class="Left">
    <h1>Left Wing News</h1>
    <CreateButton> </CreateButton>
  </div>
</template>


<script>
import CreateButton from '@/components/CreateButton'
export default {
    name: 'Left',

    components: {CreateButton},

    data() {
        return {
        }
    }
}
</script>


<style scoped lang="css">

h1 {
  text-align: center;
}

</style>