from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from root.models import Notice,Course,Event,ExecutivePanel,FacultyPanel

# Create your views here.

def home(request):
    notice=Notice.objects.all().order_by('-date')
    course=Course.objects.all().order_by('-id')
    event=Event.objects.all()
    dic={
        'notice':notice,
        'course':course,
        'event':event,
    }
    return render(request,"root/index.html",dic)



def current_panel(request):
    panels_data = []
    panels = ExecutivePanel.objects.all()

    for panel in panels:
        leader = panel.members.filter(is_leader=True).first()
        members = panel.members.filter(is_leader=False)
        panels_data.append({
            'panel': panel,
            'leader': leader,
            'members': members
        })

    # ✅ get title & subtitle from the first panel (or any specific logic)
    if panels.exists():
        page_title = panels[0].page_title
        page_subtitle = panels[0].page_subtitle
    else:
        page_title = 'Default Title'
        page_subtitle = 'Default Subtitle'

    return render(request, 'root/current_panel.html', {
        'panels': panels_data,
        'page_title': page_title,
        'page_subtitle': page_subtitle
    })


def former_panel_1(request):
    return render(request, 'root/former_panel_1.html')

def former_panel_2(request):
    return render(request, 'root/former_panel_2.html')

def current_faculty(request):
    panels_data = []
    panels = FacultyPanel.objects.all()

    for panel in panels:
        members = panel.members.all()
        panels_data.append({
            'panel': panel,
            'members': members
        })

    # ✅ get title & subtitle from the first panel
    if panels.exists():
        page_title = panels[0].page_title
        page_subtitle = panels[0].page_subtitle
    else:
        page_title = 'Default Title'
        page_subtitle = 'Default Subtitle'

    return render(request, 'root/current_faculty.html', {
        'panels': panels_data,
        'page_title': page_title,
        'page_subtitle': page_subtitle
    })

def former_faculty(request):
    return render(request, 'root/former_faculty.html')


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

