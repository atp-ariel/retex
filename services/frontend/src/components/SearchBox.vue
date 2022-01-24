<template>
    <div class="search-box">
        <form class="input-group search" v-on:submit.prevent="submitForm">
            <div class="input-append zoom">
                <button type="submit" class="btn btn-primary" tabindex="-1">
                    <i class="fas fa-search"></i>
                </button>
            </div>
            <input type="search" placeholder="Search Retex ..." v-model="form.q" id="input-search-box" class="form-control" tabindex="-1">
        </form>
    </div>
</template>

<script>
import axios from "axios"
import router from "@/router/index"

export default {
  name: 'SearchBox',
  props: {
    q: String
  },
  data(){
      return {
          form: {
              q: ''
          }
      }
  },
  methods: {
      submitForm(){
          axios.get("/search", {params: {q: this.form.q}})
            .then(res => { 
                if (res.status == 200)
                {
                    router.push("?temp")
                        .then(() => router.push({name: "Search", params:{result: res.data}}))
                }
            })
      }
  }
}
</script>

<style scoped>
.search-box{
    margin-top:3%;
}

.search > .form-control
{
    border-width: 1px 1px 1px 0;
    border-radius: 0 3rem 3rem 0;
    border-color: darkgray;
    color: gray;
    background-color: white;
    font-weight: 300;
    font-family: Roboto, sans-serif;
    box-shadow: 0px 8px 20px 0px rgba(61, 60, 60, 0.068);
}


.search > .zoom > button:active,
.search > .zoom > button:focus,
.search > .zoom > button:active
{
    color: darkgray;
    background-color: white;
    border-color: darkgray;
}

.search > .zoom > button
{
    border-width: 1px 0 1px 1px;
    border-color: darkgray;
    color: darkgray;
    background-color: white;
    border-radius: 3rem 0 0 3rem;
    z-index:999;
}
</style>