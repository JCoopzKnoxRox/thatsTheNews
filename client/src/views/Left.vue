<template lang="html">
  <div class="Left">
    <h1>Left Wing News</h1>
    <p> {{ articles }} <br> </p>
    <CreateButton> </CreateButton>
  </div>
</template>


<script>
import CreateButton from '@/components/CreateButton'
import PostsService from '@/services/PostsService'
export default {
    name: 'Left',

    components: {CreateButton},

    data() {
        return {
          articles: null
        }
    },
  mounted() {
    PostsService.get_articles()
      .then(response => {
        this.articles = response.data
      })
    }
  }


</script>


<style scoped lang="css">

h1 {
  text-align: center;
}

</style>