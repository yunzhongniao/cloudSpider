<template>
  <div>
    <mavon-editor v-model="content"/>
  </div>
</template>
<script>

export default {
  name: 'BookChapterDetail',
  props: {'bookId': String,
    'chapter': String},
  data () {
    return {
      content: ''
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
    }

  },
  mounted () {
    console.log('book detail bookid:', this.bookId, ' chapter:', this.chapter)
    this.content = '###Head'
  }

}
</script>
