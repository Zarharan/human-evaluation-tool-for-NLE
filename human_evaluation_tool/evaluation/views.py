from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from .models import *
from .forms import *
from .utils import *


def index(request):
    context = {}
    return render(request, 'home.html', context)


@login_required
def evaluate(request):

    context = {'FACT_CHECKING_CLASSES': zip([item[1] for item in FACT_CHECKING_CLASSES], [item[0] for item in FACT_CHECKING_CLASSES])
        ,'FLUENCY_RATING': zip([item[1] for item in FLUENCY_RATING], [item[0] for item in FLUENCY_RATING])
        ,'INTERNAL_CONSISTENCY_RATING': zip([item[1] for item in CONSISTENCY_RATING], [item[0] for item in CONSISTENCY_RATING])
        ,'EXTERNAL_CONSISTENCY_RATING': zip([item[1] for item in CONSISTENCY_RATING], [item[0] for item in CONSISTENCY_RATING])
        ,'MISSING_INFORMATION_RATING': zip([item[1] for item in MISSING_INFORMATION_RATING], [item[0] for item in MISSING_INFORMATION_RATING])}

    # Get and return an incompleted annotated instance if exists
    target_annotation= Annotation.objects.filter(user= request.user, annotated= False).select_related().first()
    if target_annotation != None:
        context['annotation']= target_annotation
        return render(request, 'evaluate.html', context)

    annotated_ids= Annotation.objects.filter(user= request.user, annotated=True).values('instance_id')
    new_instance = Instance.objects.exclude(id__in=annotated_ids).first()

    # If there is no sample to evaluate, return the template and show appropriate message on the client-side
    if new_instance == None:
        return render(request, 'evaluate.html', context)

    # Assign a new instance to current user for evaluating
    target_annotation = Annotation.objects.create(user= request.user, annotated= False, instance= new_instance)
    target_annotation.save()
    context['annotation']= target_annotation

    return render(request, 'evaluate.html', context)


@login_required
def save_annotation(request, annotation_id):
    # Edit an existing annotation
    target_annotation = Annotation.objects.get(id= annotation_id)
    form = AnnotationForm(request.POST, instance= target_annotation)

    if form.is_valid():
        updated_record = form.save(commit=False)
        updated_record.annotated= True
        updated_record.save()
        form.save_m2m()
        return JsonResponse({'success': True})
    else:
        context= {'error_message': form.errors, 'success': False}
        return JsonResponse(context)