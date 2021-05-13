<template lang="html">
  <nav>
    <router-link class="title" :to="{ name: 'Home', params: {} }">ThatsTheNewsHome</router-link>
    <router-link class="politics" :to="{ name: 'Politics', params: {} }">Political News</router-link>
    <router-link class="covid" :to="{ name: 'Covid', params: {} }">Covid News</router-link>
    <router-link class="stocks" :to="{ name: 'Stocks', params: {} }">Stock News</router-link>
    <router-link class="tech" :to="{ name: 'Tech', params: {} }">Tech News</router-link>
    <router-link class="sports" :to="{ name: 'Sports', params: {} }">Sporting News</router-link>
    <router-link class="entertainment" :to="{ name: 'Entertainment', params: {} }">Entertainment News</router-link>
    <router-link class="crypto" :to="{ name: 'Crypto', params: {} }">Crypto Currency News</router-link>
    <router-link class="climate" :to="{ name: 'Climate', params: {} }">Climate Change News</router-link>
  </nav>
</template>

<script>
export default {
  name: 'nav',

  methods: {
    
  }
}
</script>

<style scoped lang="css">
nav {
  overflow: hidden;
  background-color: #333;
  font-family: Arial;
}

nav a {
  float: left;
  font-size: 16px;
  color: rgb(255, 255, 255);
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.title {
  font-weight: bold;
}
.covid{
  font-weight: bold;
  background-size: 120px 50px;
  background-image: url('https://image.freepik.com/free-photo/top-view-medical-syringe-pattern-blue-background_108611-1823.jpg');

}
.politics{
  font-weight: bold;
  background: linear-gradient(to right, #0400ff 0%, #fc0000 100%);
}
.stocks{
  font-weight: bold;
  background-size: 120px 50px;
  background-image: url('https://freepngimg.com/thumb/stock_market/25650-5-stock-market-graph-up-transparent-background.png');
}
.tech{
  font-weight: bold;
  background-size: 120px 50px;
  background-image: url('https://d1ymz67w5raq8g.cloudfront.net/Pictures/480xAny/8/4/0/130840_shutterstock_476872021.jpg');
}
.sports{
  font-weight: bold;
  background-size: 144px 50px;
  background-image: url('https://media.istockphoto.com/vectors/football-field-vector-id523631979?b=1&k=6&m=523631979&s=612x612&w=0&h=b-9ygrLHJ-NI1CCOhj01E3NkOQYV245xJY-44YOI5fk=');
}
.entertainment{
  font-weight: bold;
  background-size: 180px 50px;
  background-image: url('https://valleyadvocate.com/wp-content/uploads/2020/07/theater-stage-red-curtain.jpg');
}
.crypto{
  font-weight: bold;
  background-size: 205px 75px;
  background-image: url('https://d32ijn7u0aqfv4.cloudfront.net/wp/wp-content/uploads/raw/bitcoin-yellow-background_SOIN19040_1907151_St_780x440.jpg');
}
.climate{
  font-weight: bold;
  background-size: 205px 50px;
  background-image: url('https://www.nortonabrasives.com/sites/sga.na.com/files/styles/paragraphs_item__field_paragraph_slide_image__home/public/banner-market-energyenviroment-turbines.jpg?t=444341&itok=YT3gNM98');
}
.dropdown {
  float: left;
  overflow: hidden;
}

.dropdown .dropbtn {
  font-size: 16px;
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font: inherit;
  margin: 0;
}

nav a:hover, .dropdown:hover .dropbtn {
  background-color: #111;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  float: none;
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}
</style>
