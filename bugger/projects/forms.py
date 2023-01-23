from django import forms

from bugger.projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "description",
            "public",
        )
