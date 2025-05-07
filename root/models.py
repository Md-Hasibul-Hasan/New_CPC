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
    details = models.TextField(blank=True, null=True)  # if you want to allow empty details
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






class ExecutivePanel(models.Model):
    name = models.CharField(max_length=100)
    page_title = models.CharField(max_length=200, default='EXECUTIVE BODY 20..')
    page_subtitle = models.CharField(max_length=300, default='Acting Panel (Effective from..)')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # save this instance first
        # update all other panels to match this one's title & subtitle
        ExecutivePanel.objects.exclude(id=self.id).update(
            page_title=self.page_title,
            page_subtitle=self.page_subtitle
        )

    def __str__(self):
        return self.name


class ExecutiveMember(models.Model):
    panel = models.ForeignKey(ExecutivePanel, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    is_leader = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_leader:
            # set all other members of this panel to is_leader=False
            ExecutiveMember.objects.filter(panel=self.panel, is_leader=True).exclude(id=self.id).update(is_leader=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name







class FacultyPanel(models.Model):
    name = models.CharField(max_length=100)
    page_title = models.CharField(max_length=200, default='FACULTY PANEL')
    page_subtitle = models.CharField(max_length=300, default='Acting Panel (Effective from...)')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update all other panels to sync title & subtitle
        FacultyPanel.objects.exclude(id=self.id).update(
            page_title=self.page_title,
            page_subtitle=self.page_subtitle
        )

    def __str__(self):
        return self.name


class FacultyMember(models.Model):
    panel = models.ForeignKey(FacultyPanel, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150, default='Lecturer, Dept of CSE, KiU')
    image = models.ImageField(upload_to='faculty/')
    facebook_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
