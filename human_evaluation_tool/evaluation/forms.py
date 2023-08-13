from django.forms import ModelForm
from .models import *


class AnnotationForm(ModelForm):
    """Auto generated form to create Annotation models."""

    class Meta:
        model = Annotation
        exclude = ["register_date", "user", "instance", "annotated"]