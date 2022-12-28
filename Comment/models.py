from django.db import models
# from django.contrib.auth.models import User
from AppUser.models import AppUser
from Anime.models import Anime


# Create your models here.

class Comment(models.Model):
    # 用户对评论一对多
    CommentUser = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='comments')
    # 番剧对评论一对多

    CommentUserName = models.CharField(max_length=50, default='')

    CommentID = models.AutoField(primary_key=True)

    # 对应番剧都名字
    AnimeTitle = models.CharField(max_length=50, default='')
    mediaId = models.CharField(max_length=50, default="")

    # 对应番剧的封面
    AnimeCover = models.CharField(max_length=100, default='')

    # 评分
    Rating = models.FloatField()
    # 评论
    CommentBody = models.CharField(max_length=200)
    # 是否公开
    IsPublic = models.BooleanField()

    Created = models.DateTimeField(auto_now_add=True)

    # 评论对应番剧，一对多
    CommentAnime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    # 点赞
    like = models.IntegerField(default=0)

    # 踩
    nasty = models.IntegerField(default=0)

    class Meta:
        ordering = ('Created',)

    def __srt__(self):
        return self.body
