from django.db import models

# Create your models here.
class Author( models.Model ):
    
    author_name = models.CharField( max_length = 30, unique = True )
    
    
class Translator( models.Model ):
    
    translator_name = models.CharField( max_length = 30, unique = True )
    
    
class Publisher( models.Model ):
    publisher_name = models.CharField( max_length = 30, unique = True )
       
       
class User( models.Model ):
    
    userid = models.CharField( max_length = 30, unique = True )
    uid = models.CharField( max_length = 30, unique = True )
    name = models.CharField( max_length = 30 )
    email = models.EmailField( blank = True, null = True, )
    # picture
    avatar = models.URLField( max_length = 200 )
    url = models.URLField( max_length = 200 )
    created = models.DateField()
    desc = models.CharField( max_length = 200 )

class Tags( models.Model ):
    tag_name = models.CharField( max_length = 30, unique = True )
    user = models.ForeignKey( User, blank = True, null = True )
    
class Rating( models.Model ):  
    
    # rating_id=models.CharField(max_length=100,unique=True)
    # rating=models.CharField(max_length=100,unique=True)
    score = models.IntegerField()
    user = models.ForeignKey( User, blank = True, null = True )
    
      
class Review( models.Model ):
    
    reviewid = models.CharField( max_length = 30, unique = True )
    
    title = models.CharField( max_length = 100 )
    url = models.URLField( max_length = 200 )
    
    authorid = models.CharField( max_length = 30 )
    bookid = models.CharField( max_length = 30 )
    
    # author's rating
    rating = models.IntegerField()
    
    # caculate the review's vote number
    votes = models.IntegerField()
    useless = models.IntegerField()
    
    abstract = models.CharField( max_length = 200 )
    content = models.CharField( max_length = 10000 )
    
    published = models.DateField()
    updated = models.DateField()
    
    
class Annotation( models.Model ):
    
    annotationid = models.CharField( max_length = 30, unique = True )
    
    title = models.CharField( max_length = 100 )
    url = models.URLField( max_length = 200 )
    
    authorid = models.CharField( max_length = 100 )
    bookid = models.CharField( max_length = 100 )
    
    abstract = models.CharField( max_length = 200 )
    content = models.CharField( max_length = 10000 )
    
    published = models.DateField()
    updated = models.DateField()
    
class Book( models.Model ):
    # book_id=models.IntegerField(max_length=100,unique=True)
    bookid = models.CharField( max_length = 30 )
    isbn10 = models.CharField( max_length = 30 )
    isbn13 = models.CharField( max_length = 30 )
    title = models.CharField( max_length = 100 )
    url = models.URLField( max_length = 200 )
    small_image_url = models.URLField( max_length = 200 )
    large_image_url = models.URLField( max_length = 200 )
    # price          = models.DecimalField(max_digits=8,decimal_places=2)
    # date_available = models.DateField()
    # #many
    author = models.ManyToManyField( Author )
    translator = models.ManyToManyField( Translator )
    publisher = models.ForeignKey( Publisher )
    
    pubdate = models.DateField()
    
    # rating
    rating = models.ForeignKey( Rating )
    
    tags = models.ManyToManyField( Tags )
    user = models.ManyToManyField( User )
   
    
    binding = models.CharField( max_length = 100 )
    price = models.DecimalField( max_digits = 8, decimal_places = 2 )
    pages = models.IntegerField()
    author_intro = models.CharField( max_length = 10000 )
    summary = models.CharField( max_length = 10000 )
    catalog = models.CharField( max_length = 10000 )
    
    # orders = models.ManyToManyField(Order,through='LineItem')

    
    
    
