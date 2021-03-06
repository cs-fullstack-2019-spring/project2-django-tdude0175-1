from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
# for the users this model saves their information and has it linked to articles and user
class WikiEditorModel(models.Model):
    Username = models.CharField(max_length=200)
    Password = models.CharField(max_length=300)
    Email = models.EmailField()
    ProfilePicture = models.ImageField(upload_to='media', null=True,blank=True)
    Description = models.TextField(max_length=500)
    Accountlink = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)

    def __str__(self):
        return self.Username + ' Is the Editor/ '
# the date created and last edited are not managable with is strange but they will display properly
class WikiArticleModel(models.Model):
    Title = models.CharField(max_length=200)
    Body = models.TextField(max_length=1000)
    Image = models.ImageField(upload_to='media' , null=True, blank=True)
    DateCreated = models.DateField(auto_now_add=True)
    LastEdited = models.DateTimeField(auto_now=True)
    User = models.ForeignKey(WikiEditorModel, on_delete=models.PROTECT, null=True , blank=True)

    def __str__(self):
        return self.Title + ' is article / ' + str(self.User)
# Links back to article and it is completely optional.
class ArticleSideContentModel(models.Model):
    SideTitle = models.CharField(max_length=200, null=True, blank=True)
    SideBody = models.TextField(max_length=500,null=True,blank=True)
    SidePicture = models.ImageField(upload_to='media',null=True,blank=True)
    ArticleLink = models.ForeignKey(WikiArticleModel,on_delete=models.CASCADE, null=True , blank=True)

    def __str__(self):
        return self.SideTitle + " is the Side Content / " + str(self.ArticleLink)
