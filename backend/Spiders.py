from django.http import HttpResponse

class SpiderController:
    def get_spiders(request):
        spider_list = [
            {
                'spider_name':'alibaba',
                'spider_id':'alibaba',
            },
            {
                'spider_name':'credit_info',
                'spider_id':'credit_info'
            }
        ]
        return HttpResponse(json.dumps(spider_list))