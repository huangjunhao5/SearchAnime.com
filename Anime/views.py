import requests
from django.core import serializers
from django.shortcuts import render

# Create your views here.

from django.contrib.auth import login, authenticate, logout
from django.core.serializers import serialize
from django.shortcuts import render
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User  # django封装好的验证功能
from django.contrib import auth

from Comment.models import Comment
from .models import Anime, AnimeScore, AnimeTag
from django.views.decorators.csrf import csrf_exempt
import json


# 爬取b站数据的函数，仅使用一次
def SetAnimeDatabase(request):
    Anime.objects.all().delete()
    mediaTag = {
        '原创': 10010,
        '漫画改': 10011,
        '小说改': 10012,
        # '游戏改': 10013,
        # '特摄': 10102,
        '布袋戏': 10015,
        '热血': 10016,
        '穿越': 10017,
        '奇幻': 10018,
        '战斗': 10020,
        '搞笑': 10021,
        '日常': 10022,
        '科幻': 10023,
        '萌系': 10024,
        '治愈': 10025,
        '校园': 10026,
        '少儿': 10027,
        '泡面': 10028,
        '恋爱': 10029,
        '少女': 10030,
        '魔法': 10031,
        '冒险': 10032,
        '历史': 10033,
        '架空': 10034,
        '机战': 10035,
        '神魔': 10036,
        '声控': 10037,
        '运动': 10038,
        '励志': 10039,
        '音乐': 10040,
        '推理': 10041,
        '社团': 10042,
        '智斗': 10043,
        '催泪': 10044,
        '美食': 10045,
        '偶像': 10046,
        '乙女': 10047,
        # '职场': 10048,
    }
    for tag, key in mediaTag.items():
        for i in range(3):
            if i == 0:
                continue
            url = requests.get(
                f"https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id={key}&order=3&st=1&sort=0&page={i}&season_type=1&pagesize=20&type=1")
            text = url.text
            # print(text)
            data = json.loads(text)
            cnt = 0
            # print(data)
            for AnimeData in data['data']['list']:
                cnt += 1
                # print(AnimeData)
                mid = AnimeData['media_id']
                temp_animeList = Anime.objects.filter(media_id=mid)
                if temp_animeList:
                    temp_anime = temp_animeList[0]
                    if tag in temp_anime.media_tag:
                        continue
                    temp_anime.media_tag = temp_anime.media_tag + ' ' + tag
                    temp_anime.save()
                    continue
                newAnime = Anime()
                # newAnime.area = AnimeData['area']
                # print(AnimeData['area'])
                # print(newAnime.area)
                # newAnime.arealimit = AnimeData['arealimit']
                # newAnime.attention = AnimeData['attention']
                # newAnime.bangumi_id = AnimeData['bangumi_id']
                # newAnime.bgmcount = AnimeData['bgmcount']
                newAnime.cover = AnimeData['cover']
                newAnime.first_ep_cover = AnimeData['first_ep']['cover']
                # newAnime.danmaku_count = AnimeData['danmaku_count']
                newAnime.ep_id = AnimeData["first_ep"]['ep_id']
                # newAnime.favorites = AnimeData["favorites"]
                newAnime.is_finish = AnimeData['is_finish']
                newAnime.link = AnimeData['link']
                newAnime.media_id = AnimeData['media_id']
                newAnime.order = AnimeData['order']
                newAnime.score = AnimeData['score']
                newAnime.index_show = AnimeData['index_show']
                # newAnime.lastupdate = AnimeData['lastupdate']
                # newAnime.lastupdate_at = AnimeData['lastupdate_at']
                # newAnime.new = AnimeData['new']
                # newAnime.play_count = AnimeData['play_count']
                # newAnime.pub_time = AnimeData['pub_time']
                newAnime.season_id = AnimeData['season_id']
                newAnime.season_status = AnimeData['season_status']
                newAnime.season_type = AnimeData['season_type']
                newAnime.subTitle = AnimeData['subTitle']
                newAnime.title_icon = AnimeData['title_icon']
                # newAnime.spid = AnimeData['spid']
                # newAnime.square_cover = AnimeData['square_cover']
                newAnime.title = AnimeData['title']
                newAnime.order_type = AnimeData['order_type']
                # newAnime.viewRank = AnimeData['viewRank']
                # newAnime.weekday = AnimeData['weekday']
                newAnime.media_tag = tag
                newAnime.save()
                # print(newAnime)
            if cnt != 20: break
    return JsonResponse({
        'code': 'ok',
        'result': '1',
    })


# 设置标签,仅使用一次
def SetAnimeTag(request):
    AnimeTag.objects.all().delete()
    animeList = Anime.objects.all()
    for anime in animeList:
        tagList = anime.media_tag.split()
        for tag in tagList:
            allTag = AnimeTag.objects.filter(tag_name=tag)
            if len(allTag):
                continue
            else:
                newTag = AnimeTag()
                newTag.tag_name = tag
                newTag.save()
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
    })


# 获取当前番剧
def GetAnimeByMediaId(request, mid):
    # mid是media_id
    res = Anime.objects.filter(media_id=mid)

    if not res.exists():
        return JsonResponse({
            'code': 'no',
            'message': 'Anime is not found',
            'data': '404',
        })
    score = AnimeScore.objects.filter(anime=res[0])
    if not score:
        new_anime_score = AnimeScore(sumScore=0, cnt=0, anime=res[0])
        new_anime_score.save()
        score = AnimeScore.objects.filter(anime=res[0])
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', res),
        'score': serializers.serialize('python', score)
    })


# 获取所有番剧
def GetAllAnime(request):
    res = Anime.objects.all().order_by('-score')
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', res)
    })


# 获取番剧搜索结果
def SearchAnime(request, keyword):
    anime_list = Anime.objects.all()
    res = []
    keyword = keyword.replace(' ', '')
    for anime in anime_list:
        if keyword in anime.title.replace(' ', ''):
            res.append(anime)
    if not res:
        return JsonResponse({
            'code': 'no',
            'message': 'keyword no found',
        })
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', res),
    })


# 获取全部番剧的名称（仅用于搜索）
def GetAllAnimeTitle(request):
    res = []
    animeList = Anime.objects.all()
    for anime in animeList:
        res.append({'value': anime.title, 'media_id': anime.media_id})
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': res
    })


# 按标签查询结果
def GetAnimeByTag(request, TagName):
    res = []
    animeList = Anime.objects.all()
    for anime in animeList:
        if TagName in anime.media_tag:
            res.append(anime)
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', res)
    })


# 最近更新
def GetUnFinishedAnime(request):
    res = Anime.objects.filter(is_finish=0).order_by('-score')
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', res)
    })


# 最近热门
def GetMostHotAnime(request):
    comment_list = Comment.objects.all().order_by('-Created')
    res = []
    for comment in comment_list:
        if not comment.CommentAnime in res:
            res.append(comment.CommentAnime)
            if len(res) == 5:
                break
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', res)
    })
