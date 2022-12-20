from django.http import HttpResponse


class HomePageView():
    template_name = ''


def todo(request):
    return HttpResponse('todo')
