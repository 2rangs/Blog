<template>
  <div class="wrapper">
    
{{test}}
제목
내용
이미지



  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import api from '../api/api'

export default defineComponent({
  name: 'HelloWorld',
data() {
  return{
    test : "asf"
  }
}
,
mounted(){
  api.test().then(
              (response: any) => {
                this.test = response.data[0].msg
                })
}
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
