<template>
<div>
    <a-table
    :dataSource="datas"
    :columns="columns"
    bordered>
    <template slot="operation" slot-scope="text, record">
        <a-button @click="() => onDetail(record)" type="link">detail</a-button>
      </template>
    </a-table>
</div>
</template>
<script>

export default {
  name: 'BookChapters',
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
    return {
      columns,
      datas: {
        bookId: {}
      }
    }
  },
  methods: {
    onDetail: function (record) {
      console.log('record', record)
      this.$router.push('/books/book/' + this.bookId + '/chapters/' + record.id)
    }

  },
  mounted () {
    this.datas = [{
      'id': 1,
      'name': '话说天下大势，合久必分分久必合',
      'desc': '三国演义的故事概要介绍'
    }, {
      'id': 2,
      'name': '桃园三结义',
      'desc': '刘备，关羽，张飞'
    }, {
      'id': 3,
      'name': '十八路诸侯',
      'desc': '水浒传的故事概要介绍'
    }, {
      'id': 4,
      'name': '温酒斩华雄',
      'desc': '水浒传的故事概要介绍'
    }]
  }

}
</script>
