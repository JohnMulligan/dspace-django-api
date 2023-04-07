from django.db import models

# Create your models here.

class Collection(models.Model):
	uid=models.CharField(max_length=50,null=True,blank=True)
	def __str__(self):
		return self.uid
		
class Place(models.Model):
	name_EN=models.CharField(max_length=50,null=True,blank=True)
	name_CN=models.CharField(max_length=50,null=True,blank=True)
	latitude=models.DecimalField("Latitude",
		max_digits=10,
		decimal_places=7,
		null=True
	)
	longitude=models.DecimalField("Longitude",
		max_digits=10,
		decimal_places=7,
		null=True
	)
	def __str__(self):
		return self.name_EN

class Subject(models.Model):
	name_EN=models.CharField(max_length=50,null=True,blank=True)
	name_CN=models.CharField(max_length=50,null=True,blank=True)
	def __str__(self):
		return self.name_EN

class MediaType(models.Model):
	name_EN=models.CharField(max_length=50,null=True,blank=True)
	name_CN=models.CharField(max_length=50,null=True,blank=True)
	def __str__(self):
		return self.name_EN
	
class ProductCategory(models.Model):
	name_EN=models.CharField(max_length=50,null=True,blank=True)
	name_CN=models.CharField(max_length=50,null=True,blank=True)
	def __str__(self):
		return self.name_EN

class ProductType(models.Model):
	name_EN=models.CharField(max_length=50,null=True,blank=True)
	name_CN=models.CharField(max_length=50,null=True,blank=True)
	def __str__(self):
		return self.name_EN

class Advertisement(models.Model):
	title=models.CharField(max_length=200,null=True,blank=True)
	dspace_uri=models.URLField(max_length=250,null=True,blank=True)
	dspace_iiif_uri=models.URLField(max_length=250,null=True,blank=True)
	uid=models.CharField(max_length=50,null=True,blank=True,unique=True)
	pub_year=models.IntegerField(null=True,blank=True)
	subtitle_EN=models.CharField(max_length=500,null=True,blank=True)
	subtitle_CN=models.CharField(max_length=500,null=True,blank=True)
	prod_type=models.ManyToManyField(ProductType)
	prod_cat=models.ManyToManyField(ProductCategory)
	genre=models.ManyToManyField(MediaType)
	subject=models.ManyToManyField(Subject)
	spatial_coverage=models.ManyToManyField(Place)
	owning_collection=models.ForeignKey(Collection,null=True,on_delete=models.CASCADE)
	def __str__(self):
		return self.title