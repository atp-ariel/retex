<template>
    <div class="doc-result mt-3">
        <div class="card border-less text-left shadow p-0">
            <div class="card-boby p-3">
                <h5><a :href="'/docs/' + doc.id">{{this.titleCaps(doc.title)}}</a></h5>
                <small>{{doc.text.substr(0, 200).replace(/\.\s+([a-z])[^\.]|^(\s*[a-z])[^\.]/g, s => s.replace(/([a-z])/,s => s.toUpperCase()))}} ...</small>
            </div>
        </div>
    </div>
</template>


<script>
export default {
  name: 'SearchBox',
  props: {
    doc: JSON, 
    titleCaps: Function
  },
  data(){
      return {
      };
  },
  mounted(){
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
  }
}


</script>

<style scoped>
.border-less {
  border-width: 0px !important;
}
</style>
