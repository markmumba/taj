from django.db import models

# Create your models here.
class Usermails(models.Model):
    subject= models.TextField(null=False)
    message =  models.CharField( max_length=20)
    from_email = models.EmailField(null=False)
    destinations = models.CharField(null=True, max_length=20)

    class Meta:
        ordering = ('-id',)
                                       
    def __str__(self):
        return f'{self.message} from_email'
