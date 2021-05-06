<template lang="html">
  <nav>
    <router-link class="title" :to="{ name: 'Home', params: {} }">ThatsTheNewsHome</router-link>
    <router-link class="left" :to="{ name: 'Left', params: {} }">Left Wing News</router-link>
    <router-link class="politics" :to="{ name: 'Politics', params: {} }">Political News</router-link>
    <router-link class="stocks" :to="{ name: 'Stocks', params: {} }">Stock News</router-link>
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
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.title {
  font-weight: bold;
}
.left{
  font-weight: bold;
  background-color:rgb(0, 119, 255);
}
.politics{
  font-weight: bold;
  background: linear-gradient(to right, #0400ff 0%, #fc0000 100%);
}
.stocks{
  font-weight: bold;
  background-color:rgb(3, 146, 10);
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
