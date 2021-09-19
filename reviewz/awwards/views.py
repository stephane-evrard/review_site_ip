from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer, ProjectSerializer

# Create your views here.

def index(request):
    date = dt.date.today()
    projects = Projects.get_projects()
    

    return render(request, 'index.html', {"date": date, "projects":projects})
