from django.db import models

# create text fields
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    object = models.Manager()
    # displays title and instructor name
    def __str__(self):
        display_course = '{0.title}: {0.instructor_name}:'
        return display_course.format(self)
    # sets actual name
    class Meta:
        verbose_name_plural = "University Classes"

