from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class Articles(models.Model):
    img = models.ImageField(upload_to="images/")
    title = models.CharField("Название", max_length=84)
    description = models.CharField("Опесание", max_length=250)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_text = models.TextField('Полный текст')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    moder = models.BooleanField(default=False, verbose_name='Одобрить')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('profile')

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"


class Articles_admin(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField("Название", max_length=122)
    text = models.CharField("Опесание", max_length=250)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    moder = models.BooleanField(default=False, verbose_name='Одобрить')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись админа"
        verbose_name_plural = "Записи админов"


class Comments(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья', blank=True, null=True, related_name='comments_articles')
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Post(models.Model):
    title = models.CharField("Название", max_length=84)
    description = models.CharField("Опесание", max_length=250)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_text = models.TextField('Полный текст')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    moder = models.BooleanField(default=False, verbose_name='Одобрить')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Video(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to="images/", null=False, blank=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='post_files')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    moder = models.BooleanField(default=False, verbose_name='Одобрить')


