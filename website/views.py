from django.shortcuts import render


def index(request):
    # num_topics = Topic.objects.count()
    # num_redactors = Redactor.objects.count()
    # num_newspapers = Newspaper.objects.count()
    #
    # context = {
    #     "num_topics": 1,
    #     "num_redactors": 2,
    #     "num_newspapers": 3,
    # }

    return render(request, "base.html")
