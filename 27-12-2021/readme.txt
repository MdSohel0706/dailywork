python -m venv virenv - create virtual environment

virenv\Scripts\activate.bat - start virtual environment

django-admin start project projectname

python manage.py runserver <port number>

python manage.py startapp playground

INSIDE APP FOLDER
-----------------
admin.py - where we define how the admin interface looks like
apps.py - configure the apps
models.py - where we define models class of the apps
tests.py - where we do unit tests
views.py - where we define the view functions.
A view function takes a request and create a response. It can be called as a request handler.

DEBUG TOOLBAR 
-------------

python -m pip install django-debug-toolbar - install debug toolbar package

Add "debug_toolbar" to your INSTALLED_APPS setting

MIGRATIONS
----------
python manage.py makemigrations - create migrations

python manage.py migrate - apply migrations
 
python manage.py sqlmigrate <appname> <indexofmigrationfile> - check the real sql queries used in a migration

python manage.py migrate <appname> <indexofmigrationfile>

DATABASE
--------
pip install mysqlclient

INSIDE MYSQL WORKBENCH : create database <databasename>

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DB_name',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'USER': 'DB_user',
            'PASSWORD': 'DB_password',
        }
    }

#then make migrations 

SET MYSQL PATH 
--------------
set path=%PATH%;C:\Program Files\MySQL\MySQL Server 8.0\bin;

CONNECT
-------
mysql -u root -package

CREATE EMPTY MIGRATION 
----------------------
python manage.py makemigrations store --empty

RUN A SQL QUERY IN A EMPTY MIGRATION FILE 
-----------------------------------------
operations = [
        migrations.RunSQL("""
            INSERT INTO STORE_COLLECTION (title)
            values ("mycollection")
        ""","""
            DELETE FROM STORE_COLLECTION WHERE title = "mycollection"
        """)
    ]

DJANGO ORMS
-----------
query_set = Product.objects.all() - returns queryset
get(pk = 1) - returns object with primary key value 1, throws exception if pk value not found
filter(pk = 1) - returns a query set after filtering the query set and returns a matching object
filter(pk = 1).first() - returns the first row of the queryset
filter(pk = 0).exists() - returns a boolean value depending on the existence of the queryset
filter(unit_price__gt=20) - returns a queryset of values greater than 20
filter(unit_price__gte=20) - greater than equal to
filter(unit_price__lt=20) - less than
filter(unit_price__lte=20) - less than equal to

from django.db.models import Q,F
Q object - to add multiple conditions. eg. filter(Q(unit_price__lt = 10) | Q(inventory__lt = 20))
F object - to compare among different field of same or different table

only('field1', 'field2') - to get specific columns of the table
defer('field') - to get all columns except the specified ones

select_related('collection') - to preload different table(whose name is present in the current 
table as a field) than the one whose object we are using
select_related is used when there is many to one relationship. 
like many products belong to one collection

prefetch_related('promotions') - to preload different table(whose name is present in the 
current table as a field), used in case of many to many relationship

select_related('table2').prefetch_related('table3') - nesting select and prefetch, 
order does'nt matter

aggregate(count = Count('field'), min_price = Min('price_field'))

annotate(field = Value/F('filed_name'))
EXPRESSION CLASS IN DJANGO
--------------------------
derivatives of this class are :
1. Value
2. F
3. Func
4. Aggregate
5. ExpressionWrapper

CONTENTTYPE MODELS FUNCTIONS
----------------------------
#store/models.py
class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, object_id):
        content_type_object = ContentType.objects.get_for_model(obj_type)
        queryset = TaggedItem.objects.select_related('tag').filter(content_type = content_type_object,object_id = object_id)
        return queryset

class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

#views.py
queryset = TaggedItem.objects.get_tags_for(Product, 3)

QUERY CACHE
-----------
First time we select the full table by using a queryset it is stored in cache. 
Now if we access a subset of the table it is retrieved from the Query Cache. 
We must optimize our code to facilitate using of Query Cache and not write redundant
queries because it is a costly operation to retrieve data from the memory instead of cache.

CREATING OBJECTS
---------------
collection = Collection()
    collection.title = 'Video Games'
    collection.featured_product = Product(pk = 1)
    collection.save()

or

collection = Collection.objects.create(title = "Video Games", featured_product_id = 1)

UPDATING OBJECTS
----------------
collection = Collection.objects.get(pk = 11)
collection.featured_product = Product(pk = 5)
collection.save()

or

collection = Collection.objects.filter(pk = 11).update(featured_product = Product(pk = 5))

DELETING OBJECTS
----------------
collection = Collection(pk = 11)
collection.delete()

or 

collection = Collection.objects.filter(id__gt = 5).delete()

DECLARING TRANSATIONS
---------------------
method 1 = Using decorator:
@transaction.atomic
def method(request):
    pass

method2 = Using context manager, it is better because we get the choice as to which code block
should be inside the transaction and which code block should be outside, in the same function.

def method(request):
    ... code outside transaction

    with transaction.atomic():
        code block inside transaction1
        code block inside transaction2
        code block inside transaction3

EXECUTING RAW SQL QUERIES
-------------------------
1. When the model matches the query
queryset2 = Product.objects.raw("SELECT * FROM store_product") 

2. When the model doesn't match the query and we need to bypass the model layer.
try:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM store_product')
finally:
    cursor.close()

or

with connection.cursor as cursor:
    cursor.execute("SELECT * FROM store_product")

or

#rather than using execute function use stored procedures. 
with connection.cursor as cursor:
    cursor.callproc('get_customers', [1,2,'a'])

DJANGO-ADMIN
------------
python manage.py createsuperuser

username : sohel
password : tiger 

python manage.py migrate

python manage.py changepassword sohel

CUSTOMIZING VIEW OF ADMIN PAGE 
------------------------------
------------------------------
CUSTOMIZING THE LIST VIEW OF A PRODUCT 
--------------------------------------
Method1:
1. Create class to define the view 
2. admin.site.register(models.Modelname, ClassName)
eg.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price']

admin.site.register(models.Product, ProductAdmin)

Method2:
1. Create class to define the view
2. Wrap it around the @admin.register decorator
eg. 
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price']

ORDERING OF CALCULATED ITEMS 
----------------------------
1. Write the calculating function and return the calculated value
2. Include the function name in the list_display attribute of ModelView class 
3. Wrap the function in @admin.display decorator and pass the required field 
on which to base your sorting to the ordering parameter

FINDING RELATED FIELDS
----------------------
Method1:
1. Create function to return the related field 
2. Add the related field in list_display
eg.
def collection_title(self, product):
        return product.collection.title

list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
#note : list_display[4] must not be a manytomany field

Method2:
1. 




