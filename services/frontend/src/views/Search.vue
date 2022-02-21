<template>
    <div class="search-page">
        <NavSearchBox/>

        <div class="container">
            <div class="row justify-content-center">
                <div class="col-1"></div>
                <div class="col-10 mt-3" id="result" ref="result">
                    <div v-if="result == null || result.length === 0">
                        <p>No results available please try another query</p>
                    </div>
                    <div v-if="result != null && result.length != 0" class="text-left">
                        <p>Show {{this.result.length}} results </p>
                    </div>
                </div>
                <div class="col-1"></div>
            </div>
            <div class="row mt-5 mb-3 justify-content-center">
                <div class="col-1"></div>
                <div class="col-10">
                    <Footer />
                </div>
                <div class="col-1"></div>
            </div>
        </div>
    </div>
</template>

<script>
import NavSearchBox from "@/components/NavSearchBox.vue"
import DocResult from "@/components/DocResult.vue"
import Footer from "@/components/Footer.vue"
import Vue from "vue"

export default{
    name: "Search", 
    components: {
        NavSearchBox, 
        Footer
    }, 
    props: ["result"],
    data() {
        return {
            doc: null,
        };
    },
    mounted() {
        this.showResult();
    },
    methods: {
        showResult(){
            var result_area = this.$refs.result;
            console.log("jJAJA")
            if(this.result != null){
                var old = document.getElementsByClassName("doc-result");
                console.log(old);
                while (old.length > 0){
                    old[0].parentNode.removeChild(old[0]);
                }
                var ComponentClass = Vue.extend(DocResult);
                this.result.forEach(element => {
                    var instance = new ComponentClass({
                        propsData: {
                            doc: element
                        }
                    })
                    instance.$mount()
                    result_area.appendChild(instance.$el)
                });
                return
            }
        }
    }
}
</script>