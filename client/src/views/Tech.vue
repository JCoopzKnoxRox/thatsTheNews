<template lang="html">
  <div class="Tech">
    <h1>Tech News</h1>
      <ol v-for="artic in articles" :key="artic.link">
      <img :src= artic.image 
        width="800" 
        height="500"
      />
      <br> 
      <a v-bind:href= artic.link>Link</a>
      <br> <br> 
        <h2>
        {{ artic.title }} 
        </h2>
      <br>
        <textarea rows ="10" cols = "200" v-model="artic.text" disabled=true dark=true></textarea>
        
     
      <br> <br> <br>
      </ol>
  </div>
</template>


<script>
import PostsService from '@/services/PostsService'
export default {
    name: 'Tech',

    data() {
        return {
          articles: null
        }
    },
  mounted() {
    PostsService.get_articles("tech")
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
  background: linear-gradient(to right, #000000 0%, #00d6fc 100%);
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