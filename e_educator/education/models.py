from django.db import models


# Create your models here.

class author(models.Model):
    author_fname = models.CharField(max_length=20)
    author_lname = models.CharField(max_length=20)
    author_address = models.CharField(max_length=200)
    city_id = models.ForeignKey('city', on_delete=models.CASCADE)
    author_contactno = models.CharField(max_length=10)
    author_emailid = models.CharField(max_length=50)
    author_gender = models.CharField(max_length=10)
    author_loginid = models.CharField(max_length=50)
    author_password = models.CharField(max_length=30)
    author_photo = models.CharField(max_length=200)
    author_aboutus = models.CharField(max_length=1000)
    author_rdate = models.DateField()
    author_isActive = models.IntegerField()


class city(models.Model):
    name = models.CharField(max_length=20)
    stateid = models.ForeignKey('state', on_delete=models.CASCADE)
    cit_isActive = models.IntegerField()


class state(models.Model):
    name = models.CharField(max_length=20)
    countryid = models.ForeignKey('country', on_delete=models.CASCADE)
    sta_isActive = models.IntegerField()


class country(models.Model):
    name = models.CharField(max_length=20)
    con_isActive = models.IntegerField()


class course(models.Model):
    course_name = models.CharField(max_length=20)
    course_shortdesc = models.CharField(max_length=2000)
    course_longdesc = models.CharField(max_length=5000)
    course_price = models.CharField(max_length=10)
    course_image = models.CharField(max_length=200)
    author_id = models.ForeignKey('author', on_delete=models.CASCADE)
    course_language = models.CharField(max_length=10)
    course_createddate = models.DateField()
    course_isActive = models.IntegerField()


class course_order(models.Model):
    course_id = models.ForeignKey('course', on_delete=models.CASCADE)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    order_date = models.DateField()
    order_paymentmode = models.CharField(max_length=10)


class exam(models.Model):
    order_id = models.ForeignKey('course_order', on_delete=models.CASCADE)
    exam_totalmark = models.CharField(max_length=5)
    exam_givendate = models.DateField()


class feedback(models.Model):
    feedback_text = models.CharField(max_length=500)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    course_id = models.ForeignKey('course', on_delete=models.CASCADE)
    feedback_givendate = models.DateField()


class lecture(models.Model):
    lecture_title = models.CharField(max_length=200)
    lecture_desc = models.CharField(max_length=2000)
    course_id = models.ForeignKey('course', on_delete=models.CASCADE)
    lecture_video = models.CharField(max_length=200)
    lecture_uploaddate = models.DateField()


class question(models.Model):
    course_id = models.ForeignKey('course', on_delete=models.CASCADE)
    question_name = models.CharField(max_length=400)
    question_optiona = models.CharField(max_length=100)
    question_optionb = models.CharField(max_length=100)
    question_optionc = models.CharField(max_length=100)
    question_optiond = models.CharField(max_length=100)
    question_correct = models.CharField(max_length=100)


class subject_category(models.Model):
    category_name = models.CharField(max_length=30)
    cat_isActive = models.IntegerField()


class subject_subcategory(models.Model):
    subcategory_name = models.CharField(max_length=30)
    categoryid = models.ForeignKey('subject_category', on_delete=models.CASCADE)
    subcategory_photo = models.CharField(max_length=200)
    subcategory_isActive = models.IntegerField()


class user(models.Model):
    user_fname = models.CharField(max_length=20)
    user_lname = models.CharField(max_length=20)
    user_address = models.CharField(max_length=200)
    city_id = models.ForeignKey('city', on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=10)
    user_gender = models.CharField(max_length=10)
    user_emailid = models.CharField(max_length=50)
    user_loginid = models.CharField(max_length=50)
    user_password = models.CharField(max_length=40)
    user_photo = models.CharField(max_length=200)
    user_rdate = models.DateField()
    user_isActive = models.IntegerField()

class admin(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_phone = models.CharField(max_length=10)
    admin_emailid = models.CharField(max_length=100)
    admin_password= models.CharField(max_length=50)
    admin_isActive = models.IntegerField()

class rating(models.Model):
    course_id = models.ForeignKey('course', on_delete=models.CASCADE)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    rate = models.CharField(max_length=5)
    givendate = models.DateField()
