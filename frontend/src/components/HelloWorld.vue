<template>
  <div class="wrapper">
    
{{test}}



  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import api from '../api/api'

export default defineComponent({
  name: 'HelloWorld',
data() {
  return{
    test : "테스트"
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

<style>
</style>
