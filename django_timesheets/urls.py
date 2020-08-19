"""boot4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler400, handler403, handler404, handler500
from django.contrib import admin
from django.urls import path, include, reverse
from django.conf.urls.static import static
from django.conf import settings
from django.apps import apps
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation
from django import http
import json
from customuser.views import CustomUserUpdateView
from customuser.decorators import check_lang
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime


@login_required
@check_lang
def home(request):
    c = {}
    c['tasks'] = request.user.tasks.filter(done=False)
    c['tasks_done'] = request.user.tasks.filter(done=True,close_date=datetime.now())
    c['timesheets'] = request.user.timesheets.filter(date=datetime.now())
    return render(request, "today.html", c)


def test(request):
    return render(request, "test.html")


def set_language(request):
    if 'lang' in request.GET and 'next' in request.GET:
        if translation.LANGUAGE_SESSION_KEY in request.session:
            del request.session[translation.LANGUAGE_SESSION_KEY]
        translation.activate(request.GET.get('lang'))
        request.session[translation.LANGUAGE_SESSION_KEY] = request.GET.get('lang')
        return HttpResponseRedirect(request.GET.get('next'))
    else:
        return reverse('home')


urlpatterns = [
    path('', home, name='home'),
    path('test/', test, name='test'),
    path('timesheet/', include('timesheet.urls', namespace='timesheet')),
    path('client/', include('client.urls', namespace='client')),
    path('tag/', include('tag.urls', namespace='tag')),
    path('user/', include('user.urls', namespace='user')),
    path('task/', include('task.urls', namespace='task')),
    path('project/', include('project.urls', namespace='project')),
    path('lang/', set_language, name='lang'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/update/', check_lang(CustomUserUpdateView.as_view()), name='update_user'),
    path('hijack/', include('hijack.urls', namespace='hijack')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))]

if not settings.DEBUG:
    handler400 = '.urls.bad_request'
    handler403 = '.urls.permission_denied'
    handler404 = '.urls.page_not_found'
    handler500 = '.urls.server_error'


def bad_request(request, exception):
    context = {}
    return render(request, '400.html', context, status=400)


def permission_denied(request, exception):
    context = {}
    return render(request, '403.html', context, status=403)


def page_not_found(request, exception):
    context = {}
    return render(request, '404.html', context, status=404)


def server_error(request, exception):
    context = {}
    return render(request, '500.html', context, status=500)
