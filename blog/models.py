from django.db import models
from django.utils import timezone

#class is a special keyword that indicates that we are defining an object.
#Post is the name of our model. We can give it a different name 
#(but we must avoid special characters and whitespace). 
#Always start a class name with an uppercase letter.
#models.Model means that the Post is a Django Model, 
#so Django knows that it should be saved in the database.
class Post(models.Model):
	#models.ForeignKey – this is a link to another model.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #models.CharField = this is how you define text with a limited number of characters.
    title = models.CharField(max_length=200)
    #models.TextField = this is for long text without a limit. Sounds ideal for blog post content, right?
    text = models.TextField()
    #models.DateTimeField – this is a date and time.
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    #def = means that this is a function/method
    #publish = is the name of the method. 
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # __str__() we will get a text (string) with a Post title.
    def __str__(self):
        return self.title