from django.http import FileResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from dotenv import load_dotenv
import telebot
import os
from website.models import (
    WorkExperience,
    StudyExperience,
    PortfolioExample,
    Certificate,
    Skill,
    Language,
    Document,
    CertificateTag,
    PortfolioTag
)

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_USER_ID = int(os.getenv('TELEGRAM_USER_ID'))


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
    if request.method == 'POST':
        bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        telegram_message = (f"New message from your website!"
                            f"\n\nName: {name}\nEmail: {email}\nMessage: {message}")
        bot.send_message(TELEGRAM_USER_ID, telegram_message)

        return redirect("website:index")

    return render(request, 'website/contact.html')


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
