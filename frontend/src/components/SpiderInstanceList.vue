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

export default {
  name: 'SpiderInstanceList',
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
    const datas = [{
      key: '1',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '2',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '3',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '4',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '5',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '6',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '7',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '8',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '9',
      name: 'firstName',
      site: 'http://localhost'
    }, {
      key: '10',
      name: 'firstName',
      site: 'http://localhost'
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
    }
  }
}
</script>
