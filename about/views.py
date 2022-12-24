from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "about/about.html"


class DevInfoView(TemplateView):
    template_name = "about/devinfo.html"
