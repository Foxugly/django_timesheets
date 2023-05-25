from datetime import datetime

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, include, reverse
from django.utils import translation
from django.utils.translation import check_for_language

from customuser.views import CustomUserUpdateView


@login_required
def home(request):
    c = {'tasks': request.user.tasks.filter(done=False),
         'tasks_done': request.user.tasks.filter(done=True, close_date=datetime.now()),
         'timesheets': request.user.timesheets.filter(date=datetime.now())}
    return render(request, "today.html", c)


def set_lang(request):
    response = None
    if 'lang' in request.GET and check_for_language(request.GET.get('lang')):
        user_language = request.GET.get('lang')
        translation.activate(user_language)
        if 'next' in request.GET:
            response = HttpResponseRedirect(request.GET.get('next'))
        else:
            response = HttpResponseRedirect(reverse('home'))
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME,
            user_language,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
            secure=settings.LANGUAGE_COOKIE_SECURE,
            httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
            samesite=settings.LANGUAGE_COOKIE_SAMESITE,
        )
    return response


urlpatterns = [
    path('', home, name='home'),
    path('timesheet/', include('timesheet.urls', namespace='timesheet')),
    path('client/', include('client.urls', namespace='client')),
    path('tag/', include('tag.urls', namespace='tag')),
    path('user/', include('user.urls', namespace='user')),
    path('task/', include('task.urls', namespace='task')),
    path('project/', include('project.urls', namespace='project')),
    path('lang/', set_lang, name='lang'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/update/', CustomUserUpdateView.as_view(), name='update_user'),
    path('hijack/', include('hijack.urls', namespace='hijack')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))]

if not settings.DEBUG:
    handler400 = 'tsheets.urls.bad_request'
    handler403 = 'tsheets.urls.permission_denied'
    handler404 = 'tsheets.urls.page_not_found'
    handler500 = 'tsheets.urls.server_error'


def bad_request(request, exception):
    context = {}
    return render(request, '400.html', context, status=400)


def permission_denied(request, exception):
    context = {}
    return render(request, '403.html', context, status=403)


def page_not_found(request, exception):
    context = {}
    return render(request, '404.html', context, status=404)


def server_error(request):
    context = {}
    return render(request, '500.html', context, status=500)
