<template>
<div>
    <a-table :dataSource="datas" :columns="columns" bordered>
      <template slot="operation" slot-scope="text, record">
        <a-popconfirm
          v-if="datas.length"
          title="Sure to delete?"
          @confirm="() => onDelete(record)">
          <a href="javascript:;">Delete</a>
        </a-popconfirm>
        <a-button @click="() => onRun(record)" type="link">run</a-button>
      </template>
    </a-table>
</div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'SpiderInstanceList',
  props: {
  },
  data () {
    const columns = [{
      title: 'Name',
      dataIndex: 'spider_name',
      key: 'name'
    }, {
      title: 'Site',
      dataIndex: 'spider_id',
      key: 'site'
    }, {
      title: 'operation',
      key: 'operation',
      scopedSlots: { customRender: 'operation' }
    }]
    const datas = []
    return {
      columns,
      datas
    }
  },
  methods: {
    onDelete: function (record) {
      console.log('delete', record)
    },
    onRun: function (record) {
      console.log('edit', record)
    }
  },
  mounted () {
    axios.get('cloud/spiders')
      .then(function (response) {
        console.log(response)
        this.datas = response
      })
      .catch(function (err) {
        console.log(err)
      })
  }

}
</script>
