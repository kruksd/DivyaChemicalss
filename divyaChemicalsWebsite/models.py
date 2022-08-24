
from django.db import models




class divyaProducts(models.Model):
    productName=models.CharField(max_length=200,null=False,blank=False)
    productHeroImage=models.ImageField(upload_to='static/assets/img')
    productType=models.CharField(max_length=200,blank=False,null=False)
  
    productImage=models.ImageField(upload_to='static/assets/img')
    productDescription=models.CharField(max_length=2000,null=False,blank=False)
    productPoints=models.CharField(max_length=2000,null=False,blank=False)
    productFile=models.FileField(upload_to='static/assets')

    def __str__(self):
        return self.productName    


class blogPage(models.Model):
    blogTitle=models.TextField(max_length=2000,blank=False,null=False)
    blogAuthor=models.TextField(max_length=200,blank=False,null=False)
    blogId=models.TextField(default=0,blank=False,null=False)
    blogDate=models.TextField(max_length=200,blank=False,null=False)
    blogContent=models.TextField(max_length=20000,blank=False,null=False)
    blogImage=models.ImageField(upload_to='static/assets/img')
    blogAuthorInstaLink=models.TextField(max_length=2000,blank=False,null=False)
    blogAuthorFacebookLink=models.TextField(max_length=2000,blank=False,null=False)
    blogAuthorInfo=models.TextField(max_length=2000,blank=False,null=False)

    def __str__(self):
         return self.blogTitle

class downloadModel(models.Model):
    fileName=models.CharField(blank=False,null=False,max_length=200)
    downloadFile=models.FileField(blank=False)
    modelDescription=models.TextField(max_length=4000,blank=False,null=False)
    def __str__(self):
         return self.fileName

class contactQuery(models.Model):
    name = models.CharField(blank=False,null=False,max_length=200)
    mobilenumber = models.CharField(blank=False,null=False,max_length=1000)
    email = models.CharField(blank=False,null=False,max_length=200)
    message = models.CharField(blank=False,null=False,max_length=2000)
    def __str__(self):
        return self.name + ' Query'



