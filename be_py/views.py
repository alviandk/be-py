from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"

class PrivacyPolicy(TemplateView):
    template_name = "static_page/privacy_policy.html"

class TermOfUse(TemplateView):
    template_name = "static_page/terms.html"

class AboutUs(TemplateView):
    template_name = "static_page/about.html"

class ContactUs(TemplateView):
    template_name = "static_page/contact_us.html"