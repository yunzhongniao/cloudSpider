from django.http import HttpResponse

class BookController:
    def get_books(request):
        book_list = [
            {
                'book_name':'alibaba',
                'book_id':'alibaba',
            },
            {
                'book_name':'三国演义',
                'book_id':'sanguoyanyi'
            }
        ]
        return HttpResponse(json.dumps(book_list))