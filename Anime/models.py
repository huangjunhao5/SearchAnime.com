from django.db import models


# Create your models here.

class Anime(models.Model):
    # area = models.CharField(default='', max_length=50, blank=True, null=True)
    # arealimit = models.IntegerField(default=0)
    # attention = models.IntegerField(default=0)
    # bangumi_id = models.CharField(default='', max_length=50, blank=True, null=True)
    # bgmcount = models.CharField(default='', max_length=50, blank=True, null=True)
    cover = models.CharField(default='', max_length=100, blank=True, null=True)
    first_ep_cover = models.CharField(default='', max_length=100, blank=True, null=True)
    # first_ep_id = models.IntegerField(default=0)
    index_show = models.CharField(default='', max_length=100, blank=True, null=True)
    # danmaku_count = models.IntegerField(default=0)
    ep_id = models.IntegerField(default=0)
    # favorites = models.IntegerField(default=0)
    is_finish = models.IntegerField(default=0)
    media_id = models.IntegerField(default=0)
    link = models.CharField(default='', max_length=100, blank=True, null=True)
    # lastupdate = models.IntegerField(default=0)
    # lastupdate_at = models.CharField(default='', max_length=100, blank=True, null=True)
    # new = models.BooleanField(default=0)
    # play_count = models.IntegerField(default=0)
    # pub_time = models.CharField(default='', max_length=100, blank=True, null=True)
    season_id = models.IntegerField(default=0)
    season_status = models.IntegerField(default=0)
    season_type = models.IntegerField(default=0)
    order = models.CharField(default='', max_length=100, blank=True, null=True)
    order_type = models.CharField(default='', max_length=100, blank=True, null=True)
    score = models.CharField(default='', max_length=100, blank=True, null=True)
    subTitle = models.CharField(default='', max_length=100, blank=True, null=True)
    user_sumScore = models.FloatField(default=0)
    # user_cnt = models.IntegerField(default=0)
    # spid = models.IntegerField(default=0)
    # square_cover = models.CharField(default='', max_length=100, blank=True, null=True)
    title = models.CharField(default='', max_length=100, blank=True, null=True)
    title_icon = models.CharField(default='', max_length=100, blank=True, null=True)
    media_tag = models.CharField(default='', max_length=200, blank=True, null=True)
    # viewRank = models.IntegerField(default=0)
    # weekday = models.IntegerField(default=0)


# 站内评分
class AnimeScore(models.Model):
    anime = models.OneToOneField(Anime, related_name='anime', on_delete=models.CASCADE)
    sumScore = models.FloatField(default=0)
    cnt = models.FloatField(default=0)



class AnimeTag(models.Model):
    tag_name = models.CharField(max_length=20, default='')
