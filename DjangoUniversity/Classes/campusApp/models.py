from django.db import models

# creating text fields
class UniversityCampus(models.Model):
    campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()
    # displays camps name and state
    def __str__(self):
        display_course = '{0.campus_Name}: {0.State}:'
        return display_course.format(self)
    # set the actual name
    class Meta:
        verbose_name_plural = "University Campus"