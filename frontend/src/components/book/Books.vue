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
        <a-button @click="() => onEdit(record)" type="link">edit</a-button>
      </template>
    </a-table>
</div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Books',
  props: {
  },
  data () {
    const columns = [{
      title: 'Name',
      dataIndex: 'name',
      key: 'name'
    }, {
      title: 'Site',
      dataIndex: 'site',
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
    onEdit: function (record) {
      console.log('edit', record)
    }
  },
  mounted () {
    axios.get('books/list')
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
