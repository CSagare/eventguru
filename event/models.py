from django.db import models
from django.core.validators import FileExtensionValidator
from authuser.models import CustomUser
validate_image_file_extension = FileExtensionValidator(
    allowed_extensions=['jpg', 'jpeg', 'png', 'gif']
)
class Eventplanner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating=models.FloatField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='events')
    logo = models.ImageField(upload_to='event_logos/',  validators=[validate_image_file_extension], null=True, blank=True)



    def __str__(self):
        return self.title
    
class contacts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name
