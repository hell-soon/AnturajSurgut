from django import forms


class FeedBackForm(forms.Form):

    message = forms.CharField(widget=forms.Textarea, label="")
