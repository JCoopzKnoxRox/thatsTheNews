<template lang="html">
  <div class="Politics">
    <h1>Political News</h1>
      <ol v-for="artic in articles" :key="artic.link">
      <img :src= artic.image 
        width="800" 
        height="500"
      />
      <br> 
      <a v-bind:href= artic.link>Link</a>
      <br> <br> 
        <h2>
        {{ artic.date }} 
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
    name: 'Politics',

    data() {
        return {
          articles: null
        }
    },
  mounted() {
    PostsService.get_articles("political")
      .then(response => {
        this.articles = response.data
      })
    }
  }


</script>


<style scoped lang="css">

h1 {
  text-align: center;
  color:rgb(230, 228, 228);
  background: linear-gradient(to right, #0400ff 0%, #fc0000 100%);
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