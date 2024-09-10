from django.urls import path
from website.views import index, resume, PortfolioExampleListView, CertificateListView, contact

app_name = "website"

urlpatterns = [
    path('index/', index, name='index'),
    path("home/", index, name="index"),
    path("", index, name='index'),
    path("resume/", resume, name="resume"),
    path("portfolio/", PortfolioExampleListView.as_view(), name="portfolio"),
    path("certificates/", CertificateListView.as_view(), name="certificates"),
    path("contact/", contact, name="contact")
]
