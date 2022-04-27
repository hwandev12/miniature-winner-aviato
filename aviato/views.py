from django.views.generic import (
    TemplateView,
)


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class BlogPageView(TemplateView):
    template_name = 'pages/blog_page.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class DashboardPageView(TemplateView):
    template_name = 'pages/dashboard.html'
