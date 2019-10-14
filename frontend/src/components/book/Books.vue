<template>
<div>
    <a-table :dataSource="datas" :columns="columns" bordered>
      <template slot="operation" slot-scope="text, record">
        <a-button @click="() => onPreview(record)" type="link">preview</a-button>
        <a-button @click="() => onEdit(record)" type="link">edit</a-button>
        <a-popconfirm
          v-if="datas.length"
          title="Sure to delete?"
          @confirm="() => onDelete(record)">
          <a href="javascript:;">Delete</a>
        </a-popconfirm>
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
      title: 'Id',
      dataIndex: 'id',
      key: 'id'
    }, {
      title: 'Name',
      dataIndex: 'name',
      key: 'name'
    }, {
      title: 'Description',
      dataIndex: 'desc',
      key: 'desc'
    }, {
      title: 'operation',
      key: 'operation',
      scopedSlots: { customRender: 'operation' }
    }]
    const datas = [{
      'id': 1,
      'name': '三国演义',
      'desc': '三国演义的故事概要介绍'
    }, {
      'id': 2,
      'name': '隋唐英雄传',
      'desc': '隋唐英雄传的故事概要介绍'
    }, {
      'id': 3,
      'name': '水浒传',
      'desc': '水浒传的故事概要介绍'
    }]
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
    },
    onPreview: function (record) {
      console.log('preview', record)
      this.$router.push('/books/book/' + record.id + '/record.chapters')
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
