from django.shortcuts import render
from django.views import generic

from website.models import WorkExperience, StudyExperience, PortfolioExample, Certificate


def index(request):
    return render(request, "website/index.html")


def resume(request):
    context = {
        "work_expirience": WorkExperience.objects.all,
        "study_expirience": StudyExperience.objects.all,
    }

    return render(request, "website/resume.html", context=context)


def contact(request):
    return render(request, "website/contact.html")


class PortfolioExampleListView(generic.ListView):
    model = PortfolioExample
    template_name = "website/portfolio.html"


class PortfolioExampleDetailView(generic.DetailView):
    model = PortfolioExample
    template_name = "website/project.html"


class CertificateListView(generic.ListView):
    model = Certificate
    template_name = "website/certificates.html"
