from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from root.models import Notice,Course,Event,CurrentExecutiveMember,CurrentFacultyMember,FormerExecutiveMember,FormerFacultyMember,ShowCase

# Create your views here.

def home(request):
    showcase = ShowCase.objects.all()
    notice=Notice.objects.all().order_by('-date')
    course=Course.objects.all().order_by('-id')
    event=Event.objects.all()
    dic={
        'notice':notice,
        'course':course,
        'event':event,
        'showcase':showcase
    }
    return render(request,"root/index.html",dic)




def current_panel(request):
    fields = CurrentExecutiveMember.objects.all()

    # Unique প্যানেল নাম বের করা
    panel_names = fields.values_list('panel', flat=True).distinct()
    
    # প্যানেল অনুযায়ী মেম্বার গ্রুপ করা
    panels = []
    for panel in panel_names:
        leader = CurrentExecutiveMember.objects.filter(panel=panel, is_leader=True).first()
        print(leader)
        members = CurrentExecutiveMember.objects.filter(panel=panel, is_leader=False)
        print(members)
        panels.append({
            'panel': panel,
            'leader': leader,
            'members': members
        })


    context = {
        'panels': panels,
        'page_title': fields[0].page_title if fields else 'EXECUTIVE PANEL',
        'page_subtitle': fields[0].page_subtitle if fields else 'Current Panel (Effective from...)'
    }

    return render(request, 'root/current_panel.html', context)


def former_panel(request):
    fields = FormerExecutiveMember.objects.all()

    # Unique প্যানেল নাম বের করা
    panel_names = fields.values_list('panel', flat=True).distinct()
    
    # প্যানেল অনুযায়ী মেম্বার গ্রুপ করা
    panels = []
    for panel in panel_names:
        leader = FormerExecutiveMember.objects.filter(panel=panel, is_leader=True).first()
        print(leader)
        members = FormerExecutiveMember.objects.filter(panel=panel, is_leader=False)
        print(members)
        panels.append({
            'panel': panel,
            'leader': leader,
            'members': members
        })


    context = {
        'panels': panels,
        'page_title': fields[0].page_title if fields else 'EXECUTIVE PANEL',
        'page_subtitle': fields[0].page_subtitle if fields else 'Former Panel (Effective from...)'
    }

    return render(request, 'root/former_panel.html', context)


# def former_panel_1(request):
#     return render(request, 'root/former_panel_1.html')

# def former_panel_2(request):
#     return render(request, 'root/former_panel_2.html')









def current_faculty(request):
    fields = CurrentFacultyMember.objects.all()

    # Unique প্যানেল নাম বের করা
    panel_names = fields.values_list('panel', flat=True).distinct()

    # প্যানেল অনুযায়ী মেম্বার গ্রুপ করা
    panels = []
    for panel in panel_names:
        members = CurrentFacultyMember.objects.filter(panel=panel)
        panels.append({
            'panel': panel,
            'members': members
        })

    context = {
        'panels': panels,
        'page_title': fields[0].page_title if fields else 'FACULTY PANEL',
        'page_subtitle': fields[0].page_subtitle if fields else 'Current Panel (Effective from...)'
    }
    return render(request, 'root/current_faculty.html', context)


def former_faculty(request):
    fields = FormerFacultyMember.objects.all()

    # Unique প্যানেল নাম বের করা
    panel_names = fields.values_list('panel', flat=True).distinct()

    # প্যানেল অনুযায়ী মেম্বার গ্রুপ করা
    panels = []
    for panel in panel_names:
        members = FormerFacultyMember.objects.filter(panel=panel)
        panels.append({
            'panel': panel,
            'members': members
        })

    context = {
        'panels': panels,
        'page_title': fields[0].page_title if fields else 'FACULTY PANEL',
        'page_subtitle': fields[0].page_subtitle if fields else 'Former Panel (Effective from...)'
    }
    return render(request, 'root/former_faculty.html', context)




def event_details(request,id):
    event=Event.objects.get(pk=id)
    return render(request, 'root/event_details.html', {'event':event})

def course_details(request,id):
    course=Course.objects.get(pk=id)
    return render(request, 'root/course_details.html', {'course':course})








@csrf_exempt  # optional (if csrf token missing in ajax)
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        subject = request.POST.get('Subject')
        message = request.POST.get('Message')

        full_message = f"From: {name}\nEmail: {email}\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['hasibsorker01@gmail.com'],
            fail_silently=False,
        )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)

