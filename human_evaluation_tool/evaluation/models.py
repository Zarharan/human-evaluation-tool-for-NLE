from django.db import models
from django.contrib.auth.models import User
from .utils import *


class Instance(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    claim_id = models.IntegerField()
    claim = models.TextField()
    context = models.TextField()
    explanation = models.TextField()
    tag = models.CharField(max_length=512)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.claim


class Annotation(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    suggested_class = models.IntegerField(choices=FACT_CHECKING_CLASSES, null=True)
    internal_consistency = models.IntegerField(choices=CONSISTENCY_RATING, null=True)
    external_consistency = models.IntegerField(choices=CONSISTENCY_RATING, null=True)
    extra_information = models.IntegerField(choices=YES_NO_CHOICES, null=True)
    missing_information = models.IntegerField(choices=MISSING_INFORMATION_RATING, null=True)
    internal_repetition = models.IntegerField(choices=YES_NO_CHOICES, null=True)
    claim_repetition = models.IntegerField(choices=YES_NO_CHOICES, null=True)
    register_date = models.DateTimeField(auto_now_add=True)

    suggested_class_comment = models.TextField(null=True, blank=True)
    internal_consistency_comment = models.TextField(null=True, blank=True)
    external_consistency_comment = models.TextField(null=True, blank=True)
    extra_information_comment = models.TextField(null=True, blank=True)
    missing_information_comment = models.TextField(null=True, blank=True)
    internal_repetition_comment = models.TextField(null=True, blank=True)
    claim_repetition_comment = models.TextField(null=True, blank=True)

    annotated = models.BooleanField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='annotation', null=True)
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT, related_name='annotation', null=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def suggested_class_label(self):
        return FACT_CHECKING_CLASSES[self.suggested_class][1]

    @property
    def internal_consistency_label(self):
        return CONSISTENCY_RATING[self.internal_consistency][1]

    @property
    def external_consistency_label(self):
        if self.external_consistency is not None:
            return CONSISTENCY_RATING[self.external_consistency][1]
        return ""

    @property
    def extra_information_label(self):
        if self.extra_information is not None:
            return YES_NO_CHOICES[self.extra_information][1]
        return ""

    @property
    def missing_information_label(self):
        if self.missing_information is not None:
            return MISSING_INFORMATION_RATING[self.missing_information][1]
        return ""

    @property
    def internal_repetition_label(self):
        return YES_NO_CHOICES[self.internal_repetition][1]

    @property
    def claim_repetition_label(self):
        return YES_NO_CHOICES[self.claim_repetition][1]

    class Meta:
        unique_together = (("instance", "user"),)
