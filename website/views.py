from django.http import HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from website.models import (
    WorkExperience,
    StudyExperience,
    PortfolioExample,
    Certificate,
    Skill,
    Language, Document, CertificateTag, PortfolioTag
)


def index(request):
    context = {
        "skills": Skill.objects.all,
        "languages": Language.objects.all,
    }

    return render(request, "website/index.html", context=context)


def resume(request):
    context = {
        "work_expirience": WorkExperience.objects.all,
        "study_expirience": StudyExperience.objects.all,
    }

    return render(request, "website/resume.html", context=context)


def contact(request):
    return render(request, "website/contact.html")


def document_view(request, name):
    document = get_object_or_404(Document, name=name)
    response = FileResponse(document.document.open(), content_type='application/pdf')
    return response


class PortfolioExampleListView(generic.ListView):
    model = PortfolioExample
    template_name = "website/portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = PortfolioTag.objects.all()
        return context

class PortfolioExampleDetailView(generic.DetailView):
    model = PortfolioExample
    template_name = "website/project.html"


class CertificateListView(generic.ListView):
    model = Certificate
    template_name = "website/certificates.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = CertificateTag.objects.all()
        return context
