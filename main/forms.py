from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["first_name", "last_name", "email", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 6}),
        }
