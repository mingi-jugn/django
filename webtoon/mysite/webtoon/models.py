from django.db import models


class Webtoon(models.Model):
    id = models.AutoField(primary_key=True)
    support = models.CharField(max_length=20)
    content=models.TextField(max_length=50,null=True)
    name=models.CharField(max_length=20)
    user_id = models.CharField(max_length=20,blank=True, null=True)
    make_date=models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.name

class Photo(models.Model):
    post = models.ForeignKey(Webtoon, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Mcomment(models.Model):
    name = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)
    content = models.TextField(max_length=300, null=True)
    make_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Webtoon', on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):  # 이 함수 추가
        return self.ip  # User object 대신 나타낼 문자

