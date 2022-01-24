<template>
    <div class="doc">
        <NavSearchBox/>

        <div class="container">
            <div class="row justify-content-center">
                <div class="col-1"></div>
                <div class="col-10 ">
                    <p v-if="this.doc == null" class="mt-5">Oops! Sorry, the desired document does not exist, please contact <router-link to="/credits">the developers</router-link></p>
                    <div v-if="this.doc != null" class="text-left">
                        <h3  class="mt-5">{{this.titleCaps(this.doc.title)}}</h3>
                        <p  class="mt-3">{{this.doc.text.replace(/\.\s+([a-z])[^\.]|^(\s*[a-z])[^\.]/g, s => s.replace(/([a-z])/,s => s.toUpperCase()))}}</p>
                    </div>
                </div>
                <div class="col-1"></div>
            </div>

            <div class="row">
                <div class="col-1"></div>
                <div class="col-10 mt-5 mb-3">
                    <Footer />
                </div>
                <div class="col-1"></div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import NavSearchBox from "@/components/NavSearchBox.vue";
import Footer from "@/components/Footer.vue"

export default {
    name: "Doc",
    components: {
        NavSearchBox,
        Footer
    },
    props: {
        id: Number, 
        titleCaps: Function
    },
    data() {
        return {
            doc: null,
        };
    },
    mounted() {
        this.fetchPost();

        var small = "(a|an|and|as|at|but|by|en|for|if|in|of|on|or|the|to|v[.]?|via|vs[.]?)";
        var punct = "([!\"#$%&'()*+,./:;<=>?@[\\\\\\]^_`{|}~-]*)";
        
        this.titleCaps = function(title){
        var parts = [], split = /[:.;?!] |(?: |^)["Ò]/g, index = 0;
        
        while (typeof x === "undefined") {
            var m = split.exec(title);

            parts.push( title.substring(index, m ? m.index : title.length)
            .replace(/\b([A-Za-z][a-z.'Õ]*)\b/g, function(all){
                return /[A-Za-z]\.[A-Za-z]/.test(all) ? all : upper(all);
            })
            .replace(RegExp("\\b" + small + "\\b", "ig"), lower)
            .replace(RegExp("^" + punct + small + "\\b", "ig"), function(all, punct, word){
                return punct + upper(word);
            })
            .replace(RegExp("\\b" + small + punct + "$", "ig"), upper));
            
            index = split.lastIndex;
            
            if ( m ) parts.push( m[0] );
            else break;
        }
        
        return parts.join("").replace(/ V(s?)\. /ig, " v$1. ")
            .replace(/(['Õ])S\b/ig, "$1s")
            .replace(/\b(AT&T|Q&A)\b/ig, function(all){
            return all.toUpperCase();
            });
        };
        
        function lower(word){
        return word.toLowerCase();
        }
        
        function upper(word){
        return word.substr(0,1).toUpperCase() + word.substr(1);
        }
    },
    methods: {
        fetchPost() {
            axios.get("/collection?doc_id=" + this.id)
                .then(response => this.doc = response.data)
        },
    }
}
</script>