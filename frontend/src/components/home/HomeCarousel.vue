<template>
    <div >
        <a-carousel autoplay arrows>
            <div><img :src="require('../../assets/images/cpage1.png')" /></div>
            <div><img :src="require('../../assets/images/cpage2.png')" /></div>
            <div><h3>3</h3></div>
            <div><h3>4</h3></div>
        </a-carousel>
    </div>
</template>

<script>
export default {
  name: 'HomeCarousel',
  data () {
    return {

    }
  }
}
</script>

<style>

</style>
