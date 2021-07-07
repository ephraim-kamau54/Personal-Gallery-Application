from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
            self.save()    
    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def save_tags(self):
        self.save()

    def delete_tags(self,pk):
        tags.objects.filter(id=pk).delete()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    @classmethod
    def get_category(cls):
        locations = Category.objects.all()
        return Category
        
    def __str__(self):
        return self.name

    @classmethod
    def update_category(cls, pk, value):
        cls.objects.filter(id=pk).update(image=value)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()       

class Location(models.Model):
    name = models.CharField(max_length=30)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations
        
    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, pk, value):
        cls.objects.filter(id=pk).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()



class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE,)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    
    @classmethod
    def todays_photos(cls):
        today = dt.date.today()
        photo = cls.objects.filter(pub_date__date = today)
        return photo

    @classmethod
    def days_photos(cls,date):
        photo = cls.objects.filter(pub_date__date = date)
        return photo
    
    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return photos

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    @classmethod
    def filter_by_location(cls, location):
        image_location = Images.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def update_image(cls, pk, value):
        cls.objects.filter(id=pk).update(image=value)

    @classmethod
    def get_image_by_id(cls, pk):
        image = cls.objects.filter(id=pk).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['date']
