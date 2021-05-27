# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import smtplib
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
import os, sys, subprocess
import json
from django.http import JsonResponse
from jira import JIRA
from urllib.parse import urljoin
import requests
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from web.models import *
import json
import requests

def get_user_object(request):
    user = request.user
    d = {"authenticated": user.is_authenticated}
    if user.is_authenticated:
        d['full_name'] = user.get_full_name()
        d['username'] = user.username
        d['email'] = user.email
    return d

def login(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponseRedirect(reverse("web:index"))
    return render(request, 'web/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:login"))

def index(request):
	user = get_user_object(request)
	return render(request, 'web/index.html', {'user': user})

def page(request):
    return render(request,'web/page.html')

def googleID(request):
    return HttpResponse("This ID is Created near Jhilmil, Dilshad Garden")

