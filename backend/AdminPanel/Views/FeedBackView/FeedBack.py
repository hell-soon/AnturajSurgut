from django.shortcuts import render
from AdminPanel.forms.feedback.FeedbackForm import FeedBackForm


def test(request):
    form = FeedBackForm()
    return render(request, "feedback/feedback.html", {"form": form})
