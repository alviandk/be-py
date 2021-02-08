from django.views.generic import TemplateView


class PrivacyPolicy(TemplateView):
    template_name = "static_page/privacy_policy.html"

class TermOfUse(TemplateView):
    template_name = "static_page/terms.html"

class AboutUs(TemplateView):
    template_name = "static_page/about.html"
