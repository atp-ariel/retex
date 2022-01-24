<template>
    <nav class="d-flex justify-content-start p-3" id="nav-search">
        <img class="logo w-15 h-15 mb-0 p-2 mr-5 mw-80" src="@/assets/retex.svg">
        <div class="w-30">
            <SearchBox :q="qry"/>
        </div>
        <div class="ml-5 mt-3">
            <small><router-link to="/"><i class="fa fa-arrow-left"></i> Go Home</router-link></small>
        </div>
    </nav>
</template>

<script>
import SearchBox from "./SearchBox.vue";

export default {
  name: 'NavSearchBox',
  components: {
    SearchBox
  }, 
  props : {
      qry: String
  }
}
</script>

<style>
nav {
    border-width: 1px;
    border-bottom: darkgray;
    box-shadow: 0px 8px 20px 0px rgba(61, 60, 60, 0.068);
}
.h-15 {
    height: 8% !important;
}
.w-15 {
    width: 8% !important;
}
.mw-80{
    min-width: 180px !important;
}
</style>
