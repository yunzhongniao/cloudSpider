<template>
    <div>
        <home-carousel></home-carousel>
        <div :style="{ background: '#fff', marginTop:'20px' }">
            <home-collapse></home-collapse>
        </div>
    </div>
</template>
<script>
import HomeCarousel from './HomeCarousel'
import HomeCollapse from './HomeCollapse'

export default {
  name: 'Home',
  components: {HomeCarousel, HomeCollapse},
  data () {
    return {

    }
  }

}
</script>
