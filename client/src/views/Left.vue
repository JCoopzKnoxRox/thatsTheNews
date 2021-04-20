<template lang="html">
  <div class="Left">
    <h1>Left Wing News</h1>
      <li v-for="artic in articles" :key="artic.link">
      <img :src= artic.image 
        width="800" 
        height="500"
      />
      <br> 
      <a v-bind:href= artic.link>Link</a>
      <br>
      {{ artic.wing }}
      <br>
      {{ artic.text }}
      </li>
  </div>
</template>


<script>
import PostsService from '@/services/PostsService'
export default {
    name: 'Left',

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
li {
  padding-left: 50px;
  text-align:left;
}

</style>