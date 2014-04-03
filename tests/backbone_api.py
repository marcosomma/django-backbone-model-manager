import backbone
from backbone.views import BackboneAPIView
from models import Course, Lesson, Topic


class CourseBackboneView(BackboneAPIView):
    model = Course
    display_fields = ('identifier', 'name', 'description', 'duration',)
    fields = ('identifier', 'name', 'description', 'duration',)
    def has_add_permission_for_data(self, request, cleaned_data):
        if cleaned_data['name'] == 'NOTALLOWED':
            return False
        else:
            return True

    def has_update_permission_for_data(self, request, cleaned_data):
        if cleaned_data['name'] == 'NOTALLOWED':
            return False
        else:
            return True

    def has_delete_permission(self, request, obj):
        return True

backbone.site.register(CourseBackboneView)


class LessonBackboneView(BackboneAPIView):
    model = Lesson
    display_fields = ['name', 'course']
    fields = ('name', 'course')
    
    def queryset(self, request):
        return Lesson.objects.filter(course=1)

    def has_delete_permission(self, request, obj):
        return True

backbone.site.register(LessonBackboneView)


class TopicBackboneView(BackboneAPIView):
    model = Topic
    display_fields = ['name', 'lesson']
    fields = ('name', 'lesson')

    def has_delete_permission(self, request, obj):
        return True

backbone.site.register(TopicBackboneView)


