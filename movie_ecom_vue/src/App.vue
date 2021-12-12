<template>
  <div id="wrapper">
    

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      

      <div class="navbar d-flex " id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link to="/" class="nav-link">Movie</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/summer" class="nav-link">Summer</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/winter" class="nav-link">Winter</router-link>
          </li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item">
            <router-link to="/login" class="btn btn-light">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/cart" class="nav-link"
              >Cart <span><i class="fas fa-shopping-cart"></i></span
            ></router-link>
          </li>
        </ul>
      </div>
    </nav>

    <section class="section">
      <router-view />
    </section>
    <p>copyright</p>
  </div>
</template>

<script>
import "bootstrap/dist/css/bootstrap.css";
export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
