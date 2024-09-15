from django.urls import path
from website.views import (
    index,
    resume,
    contact,
    PortfolioExampleListView,
    CertificateListView,
    PortfolioExampleDetailView
)

app_name = "website"

urlpatterns = [
    path("", index, name='index'),
    path("resume/", resume, name="resume"),
    path("portfolio/", PortfolioExampleListView.as_view(), name="portfolio"),
    path('portfolio/<int:pk>/', PortfolioExampleDetailView.as_view(), name='portfolio_detail'),
    path("certificates/", CertificateListView.as_view(), name="certificates"),
    path("contact/", contact, name="contact")
]
