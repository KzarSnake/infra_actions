from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')

# Тут вторая страница
def second_page(request):
    return HttpResponse('А это вторая страница!')
