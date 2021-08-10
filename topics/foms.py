from django import forms
from .models import ProjectTopics


class ProposeForm(forms.ModelForm):
    class Meta:
        model = ProjectTopics
        fields = ('topic_title', 'topic_author', 'topic_body',)

        widgets = {
            'topic_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'topic'}),
            'topic_author': forms.Select(attrs={'class': 'form-control'}),
            'topic_body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'please describe your form '
                                                                                        'details'}),

        }


class EditForm(forms.ModelForm):
    class Meta:
        model = ProjectTopics
        fields = ('topic_title', 'topic_body',)

        widgets = {
            'topic_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'topic'}),
            'topic_body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'please describe your form '
                                                                                        'details'}),

        }
