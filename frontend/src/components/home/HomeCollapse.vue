<template>
  <div>
    <a-collapse v-model="activeKey">
      <a-collapse-panel header="Reading With Parents" key="1">
        <div>
          <a-row :gutter="16">
            <a-col :span="8">
              <a-card title="Card title" :bordered=true>
                <img
                  alt="example"
                  src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
                  slot="cover"
                />
                <a-card-meta
                  title="Europe Street beat">
                  <template slot="description">www.instagram.com</template>
                </a-card-meta>
              </a-card>
            </a-col>
            <a-col :span="8">
              <a-card title="Card title" :bordered=true>
                <img
                  alt="example"
                  src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
                  slot="cover"
                />
                <a-card-meta
                  title="Europe Street beat">
                  <template slot="description">www.instagram.com</template>
                </a-card-meta>
              </a-card>
            </a-col>
            <a-col :span="8">
              <a-card title="Card title" :bordered=true>
                <img
                  alt="example"
                  src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
                  slot="cover"
                />
                <a-card-meta
                  title="Europe Street beat">
                  <template slot="description">www.instagram.com</template>
                </a-card-meta>
              </a-card>
            </a-col>
          </a-row>
        </div>
      </a-collapse-panel>
      <a-collapse-panel header="Reading with Self" key="2">
        <p>{{text}}</p>
      </a-collapse-panel>
      <a-collapse-panel header="Reading for Parents" key="3">
        <p>{{text}}</p>
      </a-collapse-panel>
    </a-collapse>
  </div>
</template>
<script>

export default {
  name: 'HomeCollapse',
  data () {
    return {
      text: `A dog is a type of domesticated animal.Known for its loyalty and faithfulness,it can be found as a welcome guest in many households across the world.`,
      activeKey: ['1']
    }
  },
  watch: {
    activeKey (key) {
      console.log(key)
    }
  }
}
</script>
