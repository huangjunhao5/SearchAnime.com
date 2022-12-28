from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from Anime.models import Anime, AnimeScore
from AppUser.models import AppUser
from Comment.models import Comment
from django.http import HttpResponse, JsonResponse


# Create your views here.
@csrf_exempt
def CheckComment(data):
    CommentBody = data.get("Comment", "").strip()
    CommentRating = data.get("Rating", "").strip()
    IsPublic = data.get("IsPublic")
    if CommentBody == "":
        return False
    if CommentRating == "":
        return False
    return True


@csrf_exempt
def GetCommentID():
    CommentObject = Comment.objects.all()
    if len(CommentObject) == 0:
        return 1
    return max(CommentObject)


@csrf_exempt
def PostComment(request):
    data = request.POST
    commentBody = data.get("Comment", "").strip()
    commentRating = data.get("Rating", "").strip()
    isPublic = data.get("IsPublic")
    if isPublic == 'true':
        isPublic = True
    else:
        isPublic = False
    # commentID = GetCommentID()
    media_id = data.get('mediaId', '').strip()
    # print(media_id)
    if not request.user.is_authenticated:
        return JsonResponse({
            'code': 'no',
            'message': '请登录后评论'
        })
    if not CheckComment(data):
        return JsonResponse({
            'code': 'no',
            'message': '请输入完整评论信息'
        })
    commentAnime = Anime.objects.filter(media_id=media_id)[0]
    animeScore = AnimeScore.objects.filter(anime=commentAnime)[0]
    animeTitle = commentAnime.title
    animeCover = commentAnime.cover
    animeScore.sumScore += float(commentRating)
    animeScore.cnt += 1
    animeScore.save()
    commentAnime.user_sumScore = animeScore.sumScore / animeScore.cnt * 2;
    commentAnime.save()
    nowUser = AppUser.objects.filter(user=request.user)[0]
    commentPOST = Comment(
        CommentBody=commentBody,
        Rating=commentRating,
        IsPublic=isPublic,
        CommentUser=nowUser,
        mediaId=media_id,
        AnimeCover=animeCover,
        AnimeTitle=animeTitle,
        CommentAnime=commentAnime,
        CommentUserName=nowUser.open_name
        # CommentID=commentID
    )
    commentPOST.save()
    return JsonResponse({
        'code': 'ok',
        'message': '评论成功'
    })



@csrf_exempt
def UpdateComment(request, CommentID):
    nowUserName = request.user.username
    updateCommentObjectList = Comment.objects.filter(CommentID=CommentID)
    if len(updateCommentObjectList) == 0:
        return JsonResponse({
            'code': 'no',
            'message': '没有找到该评论'
        })
    if not request.user.is_authenticated:
        return JsonResponse({
            'code': 'no',
            'message': '请登录后评论'
        })
    updateCommentObject = updateCommentObjectList[0]
    commentUserName = updateCommentObject.get('username')
    if nowUserName != commentUserName and not nowUserName.is_admin:
        return JsonResponse({
            'code': 'no',
            'message': '没有该评论修改权限'
        })
    nowData = request.POST
    commentBody = nowData.get("Comment", "").strip()
    commentRating = nowData.get("Rating", "").strip()
    isPublic = nowData.get("IsPublic")
    if CheckComment(data=nowData):
        return JsonResponse({
            'code': 'no',
            'message': '请输入完整评论信息'
        })
    updateCommentObject.CommentBody = commentBody
    updateCommentObject.Rating = commentRating
    updateCommentObject.IsPublic = isPublic
    updateCommentObject.save()
    return JsonResponse({
        'code': 'ok',
        'message': '修改成功',
    })


# 从media_id获取评论
@csrf_exempt
def GetCommentByMediaId(request, mid):
    # print(mid)
    anime_list = Anime.objects.filter(media_id=mid)
    comment_list = Comment.objects.filter(CommentAnime=anime_list[0])
    # print(len(comment_list))
    if len(comment_list) == 0:
        # print('nm')
        return JsonResponse({
            'code': 'no',
            'message': 'Comment not found',
        })
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', comment_list)
    })


@csrf_exempt
def GetCommentByUser(request, user_id):
    app_user = AppUser.objects.filter(uid=user_id)[0]
    comments = Comment.objects.filter(CommentUser=app_user)
    if not comments:
        return JsonResponse({
            'code': 'no',
            'message': 'this user has no comment',
        })
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', comments),
    })


@csrf_exempt
def GetNewComment(request):
    comment_list = Comment.objects.all().order_by('-Created')
    if len(comment_list) > 50:
        comment_list = comment_list[0:49]
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', comment_list)
    })