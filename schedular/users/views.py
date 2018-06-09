# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from users.forms import LoginForm, SearchStudent, UserEditForm
# from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login as auth_login
from django.utils.translation import ugettext
from django.contrib import messages
from schedular.email import send_email
from django.db.models import Q
from .models import User
from .forms import UserForm
from schedular.decorators import teacher_required
from absente.models import Absente
from django.http import JsonResponse
from absente.models import SchoolObject
import datetime
from django.http import HttpResponse


def login(request):
    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, ugettext("Invalid login credentials."))
    else:
        if request.user.is_authenticated():
            return redirect('home')
        else:
            form = LoginForm()
    return render(request, 'users/login.html', {
        'form': form
    })


def student_details(request):
    return render(request, "users/student_details.html", {
        "student": request.user
    })


def get_teacher(request):
    return render(request, 'users/get_teacher.html', {
        'teachers': User.objects.filter(is_teacher=True)
    })


def search_student(request):
    students = User.objects.none()
    if request.POST:
        form = SearchStudent(request.POST)
        search_term = form.data['search']
        students = User.objects.filter(is_student=True).filter(
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term) |
            Q(email__icontains=search_term))
    form = SearchStudent()
    return render(request, 'users/search.html', {
        'student': request.user,
        'students': students,
        'form': form,
    })


def addstudents(request):
    if request.method == 'POST':
        form = UserForm(
            data=request.POST, request_user=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            link = "http://{0}/users/edit-user/{1}".format(
                request.get_host(), user.pk)
            try:
                send_email(
                    subject=ugettext("[USV] USV statistics"),
                    receiver=user.email,
                    email_template_name='emails/add-user.html',
                    context={'link': link, 'user': user})
            except:
                pass
            return redirect(reverse('users:students'))
        else:
            pass
    else:
        form = UserForm(request_user=request.user)

    return render(request, 'users/add_student.html', {
        'form': form,
    })


@teacher_required
def list_all_students(request):
    return render(request, 'users/list_students.html', {
        'students': User.objects.filter(is_student=True),
    })


def addteacher(request):
    if request.method == 'POST':
        form = UserForm(
            data=request.POST, request_user=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            link = "http://{0}/users/edit-user/{1}".format(
                request.get_host(), user.pk)
            print user.pk
            try:
                send_email(
                    subject=ugettext("[USV] USV statistics"),
                    receiver=user.email,
                    email_template_name='emails/add-user.html',
                    context={'link': link, 'user': user})
            except:
                pass
            return redirect(reverse('users:students'))
        else:
            pass
    else:
        form = UserForm(request_user=request.user)

    return render(request, 'users/add_student.html', {
        'form': form,
    })


def edit_user(request, pk=None):
    instance = None
    if pk:
        try:
            instance = User.objects.get(pk=pk)
        except:
            return redirect(reverse('users:students'))
    if request.method == 'POST':
        form = UserEditForm(
            data=request.POST, instance=instance, request_user=request.user)
        if form.is_valid():
            form.save()
            if request.user.is_anonymous() or request.user.is_student:
                return redirect('users:login')
            return redirect(reverse('users:students'))
        else:
            pass
    else:
        form = UserEditForm(instance=instance, request_user=request.user)
    return render(request, 'users/edit_student.html', {
        'form': form,
    })


def student_absente(request, student_id):
    school_objects = SchoolObject.objects.filter(
        profesor=request.user)
    return render(request, "users/view_absente.html", {
        "student_id": student_id,
        "school_objects": school_objects,
        "student": User.objects.get(pk=student_id)
    })


def add_absente(request, student_id):
    import json
    
    events = json.loads(request.POST["eventsJson"])
    disciplina_details = {
    'curs': 0,
    'laborator': 1,
    'seminar': 2
    }
    for event in events:
        start = None
        end = None
        disc = None
        if "start" in event:
            start = datetime.datetime.strptime(event["start"], "%Y-%m-%d %H:%M:%S")
        if "end" in event:
            end = datetime.datetime.strptime(event["end"], "%Y-%m-%d %H:%M:%S")
        if "title" in event:
            disc = disciplina_details[str(event["title"]).split(' ')[1]]
        try:
            absenta = Absente(student=User.objects.get(pk=student_id), start=start, end=end, materie=SchoolObject.objects.filter(profesor=request.user, disciplina=disc).first())
            absenta.save()
        except:
            pass
    return HttpResponse(status=200)


def get_absente(request, student_id):
    objects_absente = []
    absente = Absente.objects.filter(
        student__id=student_id, materie__profesor=request.user)

    for absent in absente:
        title = "{} {}-{}-{}".format(
            absent.materie.profesor.first_name, absent.materie.profesor.last_name,
            absent.materie.get_disciplina_display(), absent.materie.nume_obiect)
        objects_absente.append(
            {"title": title, "start": absent.start.isoformat(),
            "end": absent.end.isoformat(), "backgroundColor": absent.materie.color,
            "student_pk": absent.student.pk})
    return JsonResponse(objects_absente, safe=False)


def get_absente_student(request, student_id):
    objects_absente = []
    absente = Absente.objects.filter(
        student__id=student_id)

    for absent in absente:
        title = "{} {}-{}-{}".format(
            absent.materie.profesor.first_name, absent.materie.profesor.last_name,
            absent.materie.get_disciplina_display(), absent.materie.nume_obiect)
        objects_absente.append(
            {"title": title, "start": absent.start.isoformat(),
            "end": absent.end.isoformat(), "backgroundColor": absent.materie.color,
            "student_pk": absent.student.pk})
    return JsonResponse(objects_absente, safe=False)


@teacher_required
def students(request):
    return render(request, 'users/about_students.html', {
        'students': User.objects.filter(is_student=True),
    })
