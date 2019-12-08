<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <div> {{users}} </div>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      users: {}
    }
  },
  components: {
  },
  beforeCreate: function () {
    console.log(this.users)
    const baseURI = '/authorize'
    this.$http.get(baseURI).then((result) => {
      this.users = result.data
    })
  }
}
</script>
