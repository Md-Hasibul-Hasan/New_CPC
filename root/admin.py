# from django.contrib import admin
# from root.models import Notice,Course,Event

# # Register your models here.

# @admin.register(Notice)
# class NoticeAdmin(admin.ModelAdmin):
#     list_display=('id','title','date','file')


# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display=('id','title','description','image')

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display=('id','title','date','type','image')



from django.contrib import admin
from django.utils.html import format_html
from .models import Notice, Course, Event, EventImage , CurrentExecutiveMember, FormerExecutiveMember,  CurrentFacultyMember, FormerFacultyMember, ShowCase



# ---------- Notice Admin ----------
@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'file')
    list_display_links = ('id', 'title')


# ---------- Course Admin ----------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'image')
    list_display_links = ('id', 'title')


# ---------- Inline for Event Images ----------
class EventImageInline(admin.TabularInline):  # or admin.StackedInline if you prefer
    model = EventImage
    extra = 1



# ---------- Event Admin ----------
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'type', 'first_image')
    list_display_links = ('id', 'title')
    inlines = [EventImageInline]

    def first_image(self, obj):
        first_img = obj.images.first()
        if first_img and first_img.image:
            return format_html('<img src="{}" width="50" />', first_img.image.url)
        return "No image"
    first_image.short_description = 'Image Preview'







@admin.register(CurrentExecutiveMember)
class CurrentExecutiveMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'panel', 'is_leader', 'image_preview')
    list_display_links = ('id', 'name')
    list_filter = ('panel', 'is_leader')
    search_fields = ('name', 'role')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="border-radius: 4px;" />', obj.image.url)
        return "(No image)"
    image_preview.short_description = 'Image'


@admin.register(FormerExecutiveMember)
class FormerExecutiveMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'panel', 'is_leader', 'image_preview')
    list_display_links = ('id', 'name')
    list_filter = ('panel', 'is_leader')
    search_fields = ('name', 'role')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="border-radius: 4px;" />', obj.image.url)
        return "(No image)"
    image_preview.short_description = 'Image'






@admin.register(CurrentFacultyMember)
class CurrentFacultyMemberAdmin(admin.ModelAdmin):
    list_display = ('id',  'name', 'designation', 'panel', 'image_preview')
    list_display_links = ('id', 'name')
    list_filter = ('panel',)
    search_fields = ('name', 'designation')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="border-radius: 4px;" />', obj.image.url)
        return "(No image)"
    image_preview.short_description = 'Image'


@admin.register(FormerFacultyMember)
class FormerFacultyMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'panel', 'image_preview')
    list_display_links = ('id', 'name')
    list_filter = ('panel',)
    search_fields = ('name', 'designation')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="border-radius: 4px;" />', obj.image.url)
        return "(No image)"
    image_preview.short_description = 'Image'



@admin.register(ShowCase)
class ShowCaseAdmin(admin.ModelAdmin):
    list_display = ( 'id','image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="border-radius: 4px;" />', obj.image.url)
        return "(No image)"
    image_preview.short_description = 'Image'