<template>
    <div id="eval">
        <nav-search-box></nav-search-box>
        <div class="container">
            <div class="row">
                <div class="col-1"></div>
                <div class="col-10 mt-5">
                    <p>Wait a few seconds please, we are evaluating the system</p>
                    <table class="table">
                        <thead>
                            <tr>
                                <th>Collection</th>
                                <th>Precission</th>
                                <th>Recall</th>
                                <th>F Mean</th>
                                <th>F1 Mean</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Cranfield</td>
                                <td>{{p}}</td>
                                <td>{{r}}</td>
                                <td>{{f}}</td>
                                <td>{{f1}}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="col-1"></div>
            </div>
                <div class="row">
                    <div class="col-12">
                        <Footer />
                    </div>
                </div>
        </div>
    </div>
</template>

<script>
import NavSearchBox from "@/components/NavSearchBox.vue"
import Footer from "@/components/Footer.vue"
import axios from 'axios';

export default {
    name: 'Eval',
    components: {
        NavSearchBox,
        Footer
    },
    props:{
        p: Number,
        r: Number,
        f: Number,
        f1: Number
    },
    mounted: function(){
        axios.get("/eval")
            .then((response) => {
                this.p = Number.parseFloat(response.data["P"]).toPrecision(3)
                this.r = Number.parseFloat(response.data["R"]).toPrecision(3)
                this.f = Number.parseFloat(response.data["F"]).toPrecision(3)
                this.f1 = Number.parseFloat(response.data["F1"]).toPrecision(3)
            })
    }
}
</script>


