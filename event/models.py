from django.db import models
# from django.core.validators import FileExtensionValidator
from authuser.models import CustomUser
# validate_image_file_extension = FileExtensionValidator(
#     allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
# )
class Eventplanner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating=models.FloatField()
    # location = models.CharField(max_length=200)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='events')
    # logo = models.ImageField(upload_to='event_logos/',  validators=[validate_image_file_extension], null=True, blank=True)
    logo = models.ImageField(upload_to='media/event_logos/')

    # logo = models.ImageField(upload_to='images/')



    def __str__(self):
        return self.title
    
class contacts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name
    
class category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name
    
class planner_category(models.Model):
    eventplanner = models.ForeignKey(Eventplanner, on_delete=models.CASCADE, related_name='planner_categories')
    category = models.ForeignKey(category, on_delete=models.CASCADE, related_name='planners')
    def __str__(self):
        return self.eventplanner.title + ' - ' + self.category.name


# class Event(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     date = models.DateTimeField()
#     location = models.CharField(max_length=200)
#     eventplanner = models.ForeignKey(Eventplanner, on_delete=models.CASCADE, related_name='events')
#     attendees = models.ManyToManyField(CustomUser, related_name='events')
#     categories = models.ManyToManyField(category, related_name='events')
#     def __str__(self):
#         return self.title
    
