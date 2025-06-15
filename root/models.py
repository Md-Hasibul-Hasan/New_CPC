# from django.db import models

# # Create your models here.

# class Notice(models.Model):
#     title=models.CharField(max_length=200)
#     date=models.DateField(auto_now_add=False)
#     file = models.FileField(upload_to='attachments')

# class Course(models.Model):
#     title=models.CharField(max_length=200)
#     description=models.CharField(max_length=300)
#     image = models.ImageField(upload_to='course_img')


# Event_Type=[
#     ('PROGRAMMING','PROGRAMMING'),
#     ('HACKATHON','HACKATHON'),
#     ('WEB','WEB'),
#     ('FEST','FEST'),
#     ('OTHERS','OTHERS')
# ]

# class Event(models.Model):
#     title=models.CharField(max_length=200)
#     date=models.DateField(auto_now_add=False)
#     type=models.CharField(max_length=20, choices=Event_Type)
#     image=models.ImageField(upload_to='event_img')





from django.db import models

# ---------- Notice Model ----------
class Notice(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False)
    file = models.FileField(upload_to='notices',blank=True,null=True)

    def __str__(self):
        return self.title
    


# ---------- Course Model ----------
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    details = models.TextField(blank=True, null=True)  
    image = models.ImageField(upload_to='course_img')

    def __str__(self):
        return self.title



# ---------- Event Types ----------
Event_Type = [
    ('PROGRAMMING', 'PROGRAMMING'),
    ('HACKATHON', 'HACKATHON'),
    ('WEB', 'WEB'),
    ('FEST', 'FEST'),
    ('OTHERS', 'OTHERS')
]

# ---------- Event Model ----------
class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False)
    type = models.CharField(max_length=20, choices=Event_Type)
    details = models.TextField(blank=True, null=True)  # if you want to allow empty details

    def __str__(self):
        return f"{self.title} - {self.date}"

# ---------- EventImage Model ----------
class EventImage(models.Model):
    event = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_img', blank=False, null=False)

    def __str__(self):
        return f"Image for {self.event.title}"




Executive = [
    ('Admin Panel', 'Admin Panel'),
    ('Mentor Wing', 'Mentor Wing'),
    ('IT Wing', 'IT Wing'),
    ('Executive Wing', 'Executive Wing'),
    ('Advertising & Finance Management Wing', 'Advertising & Finance Management Wing'),
    ('Public Relations Wing', 'Public Relations Wing')
]

class CurrentExecutiveMember(models.Model):
    panel = models.CharField(max_length=100, choices=Executive)
    name = models.CharField(max_length=100) 
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    is_leader = models.BooleanField(default=False)
    page_title = models.CharField(max_length=200, blank=True)
    page_subtitle = models.CharField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if self.is_leader:
            # এক প্যানেলে এক লিডার রাখবে
            CurrentExecutiveMember.objects.filter(panel=self.panel, is_leader=True).exclude(id=self.id).update(is_leader=False)

        # যদি নতুন instance হয়
        if not self.id:
            latest = CurrentExecutiveMember.objects.order_by('-id').first()
            if latest:
                self.page_title = latest.page_title
                self.page_subtitle = latest.page_subtitle
            else:
                # যদি কিছুই না থাকে, fallback value
                self.page_title = 'EXECUTIVE BODY'
                self.page_subtitle = 'Acting Panel (Effective from ..)'

        super().save(*args, **kwargs)

        # সব মেম্বারের page_title, page_subtitle আপডেট করে দেওয়া
        CurrentExecutiveMember.objects.exclude(id=self.id).update(
            page_title=self.page_title,
            page_subtitle=self.page_subtitle
        )

    def __str__(self):
        return self.name



class FormerExecutiveMember(models.Model):
    panel = models.CharField(max_length=100, choices=Executive)
    name = models.CharField(max_length=100) 
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    is_leader = models.BooleanField(default=False)
    page_title = models.CharField(max_length=200, blank=True)
    page_subtitle = models.CharField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
        if self.is_leader:
            # এক প্যানেলে এক লিডার রাখবে
            FormerExecutiveMember.objects.filter(panel=self.panel, is_leader=True).exclude(id=self.id).update(is_leader=False)

        # যদি নতুন instance হয়
        if not self.id:
            latest = FormerExecutiveMember.objects.order_by('-id').first()
            if latest:
                self.page_title = latest.page_title
                self.page_subtitle = latest.page_subtitle
            else:
                # যদি কিছুই না থাকে, fallback value
                self.page_title = 'EXECUTIVE BODY'
                self.page_subtitle = 'Acting Panel (Effective from ..)'

        super().save(*args, **kwargs)

        # সব মেম্বারের page_title, page_subtitle আপডেট করে দেওয়া
        FormerExecutiveMember.objects.exclude(id=self.id).update(
            page_title=self.page_title,
            page_subtitle=self.page_subtitle
        )

    def __str__(self):
        return self.name







Panel_Choice = [
    ('Cheif Advisor', 'Cheif Advisor'),
    ('Cheif Patron', 'Cheif Patron'),
]

class CurrentFacultyMember(models.Model):
    panel = models.CharField(max_length=100, choices=Panel_Choice)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150, default='Lecturer, Dept of CSE, KiU')
    image = models.ImageField(upload_to='faculty/')
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    page_title = models.CharField(max_length=200, blank=True)
    page_subtitle = models.CharField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
        # নতুন instance তৈরি হলে
        if not self.id:
            latest = CurrentFacultyMember.objects.order_by('-id').first()
            if latest:
                self.page_title = latest.page_title
                self.page_subtitle = latest.page_subtitle
            else:
                # যদি কিছুই না থাকে, fallback value
                self.page_title = 'Faculty Panel'
                self.page_subtitle = 'Acting Panel (Effective from ..)'

        super().save(*args, **kwargs)

        # সব instance এর page_title, page_subtitle আপডেট করে দেওয়া
        CurrentFacultyMember.objects.exclude(id=self.id).update(
            page_title=self.page_title,
            page_subtitle=self.page_subtitle
        )

    def __str__(self):
        return self.name



class FormerFacultyMember(models.Model):
    panel = models.CharField(max_length=100, choices=Panel_Choice)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150, default='Lecturer, Dept of CSE, KiU')
    image = models.ImageField(upload_to='faculty/')
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    page_title = models.CharField(max_length=200, blank=True)
    page_subtitle = models.CharField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
        # নতুন instance তৈরি হলে
        if not self.id:
            latest = FormerFacultyMember.objects.order_by('-id').first()
            if latest:
                self.page_title = latest.page_title
                self.page_subtitle = latest.page_subtitle
            else:
                # যদি কিছুই না থাকে, fallback value
                self.page_title = 'Faculty Panel'
                self.page_subtitle = 'Acting Panel (Effective from ..)'

        super().save(*args, **kwargs)

        # সব instance এর page_title, page_subtitle আপডেট করে দেওয়া
        FormerFacultyMember.objects.exclude(id=self.id).update(
            page_title=self.page_title,
            page_subtitle=self.page_subtitle
        )

    def __str__(self):
        return self.name


class ShowCase(models.Model):
    image = models.ImageField(upload_to='showcase/')

  