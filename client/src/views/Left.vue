<template lang="html">
  <div class="Left">
    <h1>Left Wing News</h1>
      <ol v-for="artic in articles" :key="artic.link">
      <img :src= artic.image 
        width="800" 
        height="500"
      />
      <br> 
      <a v-bind:href= artic.link>Link</a>
      <br> <br> 
        <h2>
        {{ artic.wing }} 
        </h2>
      <br>
        <div style="margin-left: 1em;">
        {{ artic.text }}
        </div>
     
      <br> <br> <br>
      </ol>
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
h2 {
  text-align: center;
  
}
ol {
  padding-left: 50px;
  padding-right: 50px;
  text-align:left;
  background-color: orange;
  border: 2px solid black;
}

</style>