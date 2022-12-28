from django.contrib.auth import login, authenticate, logout
from django.core.serializers import serialize
from django.shortcuts import render
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User  # django封装好的验证功能
from django.contrib import auth
from .models import AppUser
from Comment.models import Comment
from Anime.models import Anime
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


# Create your views here.


def check(password):
    ans = 1
    if len(password) < 8:
        return 1
    for c in password:
        if c < '0' or c > '9':
            return 0
    return 1


def create_uid():  # 生成uid
    uid = User.objects.all().count()
    return str(uid)


# 用户登录

@csrf_exempt
def signin(request):
    # x = csrf(request)
    # csrf_token = x['csrf_token']
    data = request.POST  # 获得请求的数据
    # print(data)
    request.session.clear()
    username = data.get("username")
    password = data.get("password")
    user = authenticate(username=username, password=password)  # 找到对应的u
    if not user:  # 用户不存在， 说明用户密码错误
        return JsonResponse({
            'code': 'no',
            'message': '账号或密码错误',
        })

    else:  # 登录成功
        login(request, user)
        print(request.user.is_authenticated)
        res = JsonResponse({
            'code': 'ok',
            'message': '账号密码验证成功',
        })
        request.session['username'] = username
        print(request.session['username'])
        return res


# 用户注册

@csrf_exempt
def Register(request):
    data = request.POST
    username = data.get("username", "").strip()  # strip()移除首位空格 而且如果参数没有提交，返回一个空的字符串
    password = data.get("password", "").strip()  # 密码 而且如果参数没有提交，返回一个空的字符串
    password_confirm = data.get("ConfirmPassword", "").strip()  # 同理 ^
    # print(data)
    if not username or not password:  # 用户名密码， 不嫩为空
        return JsonResponse({
            'code': 'no',
            'message': '验证失败,用户名密码，不能为空',
        })
    if password != password_confirm:  # 确认密码与密码不一致
        return JsonResponse({
            'code': 'no',
            'message': '验证失败,确认密码与密码不一致',
        })
    if User.objects.filter(username=username).exists():  # 用户名已村在
        return JsonResponse({
            'code': 'no',
            'message': '验证失败,用户名已村在',
        })
    if check(password):  # 密码强度不够
        return JsonResponse({
            'code': 'no',
            'message': '验证失败,密码强度不够',
        })
    user = User(username=username)  # 调用构造函数，新建用户
    user.set_password(password)
    user.save()
    uid = create_uid()
    AppUser.objects.create(user=user, uid=uid, open_name=username)
    login(request, user)
    return JsonResponse({
        'code': 'ok',
        'message': '注册成功',
    })


# 退出登录api
@csrf_exempt
def Logout(request):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'code': 'no',
            'message': '用户未登录，无需退出登录',
        })

    logout(request)  # 退出登录

    return JsonResponse({
        'code': 'ok',
        'message': '退出登录成功',
    })


# 获取用户信息api
@csrf_exempt
def GetUserInformation(request, uid=""):
    # user = request.user
    app_users = AppUser.objects.filter(uid=uid)
    if not app_users.exists():
        return JsonResponse({
            'code': 'error',
            "result": "user_is_not_exist",
        })
    # now_login_user = app_users[0]
    # 需要获取的字段
    fields = (
        'username', 'uid', 'open_name', 'is_admin', 'about',
    )

    res = json.loads(serialize('json', app_users, fields=fields))
    # res = list(app_users)
    return JsonResponse({
        'code': 'ok',
        'result': res,
    })


@csrf_exempt
def NowUser(request):
    user = request.user
    if request.session.has_key('username'):
        print('yes')
    else : print('no')
    if not user.is_authenticated:
        return JsonResponse({
            'code': 'no',
            'message': '用户未登录，请先登录',
        })
    app_users = AppUser.objects.filter(user=user)
    # 需要获取的字段
    fields = (
        'username', 'uid', 'open_name', 'is_admin', 'about',
    )
    res = json.loads(serialize('json', app_users, fields=fields))
    return JsonResponse({
        'code': 'ok',
        'result': res,
    })


@csrf_exempt
def ChangeUserPassword(request, uid):
    user = request.user
    if not user.is_authenticated:
        return JsonResponse({
            'code': 'Failed',
            'message': '用户未登陆',
        })
    logUser = AppUser.objects.get(user=user)
    changeUser = AppUser.objects.get(uid=uid)
    if logUser.is_admin or (logUser.uid == changeUser.uid) :
        data = request.POST
        new_password = data.get('newpassword')
        old_password = data.get('oldpassword')
        temp_user = authenticate(username=user.username, password=old_password)  # 找到对应的u
        if not temp_user:
            return JsonResponse({
                'code': 'no',
                'message': '原密码错误',
            })
        changeUser.user.set_password(new_password)
        # print(new_password)
        changeUser.user.save()
        if changeUser.user == user:
            print(changeUser.user)
            print(user)
            login(request, user)
            print(user.is_authenticated)
        return JsonResponse({
            'code': 'ok',
            'message': '修改密码成功,请重新登陆',
        })
    else:
        return JsonResponse({
            'code': 'Failed',
            'message': '用户无操作权限',
        })


@csrf_exempt
def ChangeUserInfo(request, uid):
    user = request.user
    # print(user.username)
    if not user.is_authenticated:
        return JsonResponse({
            'code': 'Failed',
            'message': '用户未登陆',
        })
    logUser = AppUser.objects.get(user=user)
    changeUser = AppUser.objects.get(uid=uid)
    if logUser.is_admin or (logUser.uid == changeUser.uid) :
        data = request.POST
        open_name = data.get('openname')
        changeUser.open_name = open_name
        about = data.get('about')
        print(data.get('openname'))
        changeUser.about = about
        changeUser.save()
        return JsonResponse({
            'code': 'ok',
            'message': '修改用户信息成功',
        })
    else:
        return JsonResponse({
            'code': 'Failed',
            'message': '用户无操作权限',
        })



@csrf_exempt
def GetVisited(request, uid):
    get_user_list = AppUser.objects.filter(uid=uid)
    if not get_user_list:
        return JsonResponse({
            'code': 'no',
            'message': 'no such user',
        })
    get_user = get_user_list[0]
    comment_list = Comment.objects.filter(CommentUser=get_user).order_by('-Created')
    res = []
    for comment in comment_list:
        anime = comment.CommentAnime
        if not anime in res:
            res.append(anime)
    return JsonResponse({
        'code': 'ok',
        'message': 'success',
        'data': serializers.serialize('python', res),
    })
