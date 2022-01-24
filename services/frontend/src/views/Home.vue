<template>
  <div class="home">
    <div class="container">
      <div class="row">
        <div class="col-1 col-sm-2"></div>
        <div class="col-10 col-sm-8">
          <router-link to="/"><img class="logo w-30" alt="Retex logo" src="@/assets/retex.svg"/></router-link>
          <SearchBox q=""/>
        </div>
        <div class="col-1 col-sm-2"></div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import SearchBox from '@/components/SearchBox.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'Home',
  components: {
    SearchBox,
    Footer,
}
}
</script>

<style>
.shadow {
  box-shadow: 0px 8px 20px 0px rgba(61, 60, 60, 0.068) !important;
}
.logo
{
  margin-bottom: 3%;
}

.w-30{
  width: 30% !important;
}
</style>

<style scoped>
.home{
  margin-top: 5%;
}
</style>