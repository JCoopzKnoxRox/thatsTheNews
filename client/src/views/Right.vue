<template lang="html">
  <div class="Right">
    <h1>Right Wing News</h1>
    <CreateButton> </CreateButton>
  </div>
</template>


<script>
import CreateButton from '@/components/CreateButton'
export default {
    name: 'Right',

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