from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GenderOption(models.TextChoices):
    male=('m','مرد')
    female=('f','زن')
    none=('n','نمی خواهم مشخص کنم')



class MyUser(models.Model):
    username=models.CharField(max_length=50 , verbose_name='نام کاربری')
    password=models.CharField(max_length=20,verbose_name='رمزعبور')
    name=models.CharField(max_length=40,verbose_name='نام')
    birthdate=models.DateField(verbose_name='تاریخ تولد')
    phone=models.CharField(max_length=11,verbose_name='شماره نلفن')
    email=models.EmailField(verbose_name='ایمیل',null=True,blank=True)
    gender=models.CharField(max_length=10, choices=GenderOption.choices,verbose_name='جنسیت')

    class Meta:
        verbose_name='کاربر '
        verbose_name_plural='کاربر'


class Post(models.Model):
    title=models.CharField(max_length=50,verbose_name='عنوان')
    content=models.TextField(verbose_name='محتوا')
    user=models.ForeignKey(to=MyUser , on_delete=models.CASCADE,verbose_name='منتشرکننده')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='زمان بروزرسانی')
    published=models.BooleanField(default=False,verbose_name= 'منتشرشده')
    published_at=models.DateTimeField(verbose_name='زمان انتشار')
    rate=models.PositiveSmallIntegerField(verbose_name='امتیاز')
    archived=models.BooleanField(default=False,verbose_name='آرشیو')
    image=models.ImageField(upload_to='post_images/',null=True,blank=True,verbose_name='بارگذاری عکس')
    class Meta:
        verbose_name='پست'
        verbose_name_plural='پست'

class Comments(models.Model):
    user=models.ForeignKey(to=MyUser , on_delete=models.CASCADE,verbose_name='کامنت توسط')
    Post=models.ForeignKey(to=Post , on_delete=models.CASCADE,verbose_name='کامنت برای پست')
    content=models.TextField(verbose_name='محتوای کامنت')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    Updated_at=models.DateTimeField(auto_now=True,verbose_name='زمان بروزرسانی')
    Is_visible=models.BooleanField(default=True,verbose_name='قابل رویت')
    parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE,related_name='replied',verbose_name='پاسخ به کامنت')
    class Meta:
        verbose_name='کامنت'
        verbose_name_plural='کامنت'


class Like(models.Model):
    user=models.ForeignKey(to=MyUser , on_delete=models.CASCADE,verbose_name='پسندیده شده توسط')
    post=models.ForeignKey(to=Post , on_delete=models.CASCADE,related_name='liked',verbose_name='پست مربوطه')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    class Meta:
        verbose_name='لایک'
        verbose_name_plural='لایک'


class Modes(models.TextChoices):
    pending=('p','در انتظار')
    accepted=('a','درخواست دوستی را قبول کرد')
    rejected=('r','درخواست دوستی را قبول نکرد')




class FriendRequest(models.Model):
    from_user=models.ForeignKey(to=MyUser,related_name='request',on_delete=models.CASCADE,verbose_name='درخواست دوستی از')
    to_user=models.ForeignKey(to=MyUser,related_name='receive_request',on_delete=models.CASCADE,verbose_name='درخواست دوستی به')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    status=models.CharField(max_length=15,choices=Modes,default='pending',verbose_name='وضعیت')
    class Meta:
        verbose_name='درخواست دوستی'
        verbose_name_plural='درخواست دوستی'

class Message(models.Model):
    sender=models.ForeignKey(to=MyUser,related_name='sender',on_delete=models.CASCADE,verbose_name='فرستنده پیام')
    receiver=models.ForeignKey(to=MyUser,related_name='receiver',on_delete=models.CASCADE,verbose_name='گیرنده پیام')
    content=models.TextField(verbose_name='محتوای پیام',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='زمان ایجاد')
    is_read=models.BooleanField(default=False,verbose_name='خوانده شده')
    class Meta:
        verbose_name='پیام'
        verbose_name_plural='پیام'
    
        

