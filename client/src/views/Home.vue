<template lang="html">
  <div class="Home">
    <h1>Top Headlines News</h1>
      <ol v-for="artic in articles" :key="artic.link">
      <h2><img :src= artic.image 
        width="800" 
        height="500"
      /> </h2>
      <br> 
      <h2> <a v-bind:href= artic.link>Link To Article</a> </h2>
      <br> <br> 
        <h2>
        {{ artic.title }} 
        </h2>
      <br>
        <div style="margin-left: 1em; line-height:2;">
        {{ artic.text }}
        </div>
     
      <br> <br> <br>
      </ol>
  </div>
</template>


<script>
import PostsService from '@/services/PostsService'
export default {
    name: 'Home',

    data() {
        return {
          articles: null
        }
    },
  mounted() {
    PostsService.get_articles("everything")
      .then(response => {
        this.articles = response.data
      })
    }
  }


</script>


<style scoped lang="css">

h1 {
  text-align: center;
  border: 15px solid black;
  color:rgb(230, 228, 228);
  background-color: rgb(29, 29, 29);
}
h2 {
  text-align: center;
}
ol {
  padding-left: 50px;
  padding-right: 50px;
  text-align:left;
  color:rgb(255, 253, 253);
  background-color: rgb(29, 29, 29);
  border: 2px solid black;
}

</style>