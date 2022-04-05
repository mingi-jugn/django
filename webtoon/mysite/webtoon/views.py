from django.core.paginator import Paginator
from .forms import commentForm
from django.shortcuts import render
from .models import Webtoon,Photo, Mcomment
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('mainpage')

def mainpage(request):
    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "webtoon": page_obj,
    }
    return render(request, "mainpage.html", context)
def error(request):
    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "webtoon": page_obj,

    }
    return render(request, "error.html", context)
def join(request):

    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "webtoon": page_obj,

    }
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'], )
            auth.login(request, user)
            return redirect('/')
        return render(request, 'join.html', context)

    return render(request, 'join.html',context)

def login(request):
    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "webtoon": page_obj,

    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')
        else:
            return render(request, 'error.html',context)
    else:
        return render(request, 'login.html',context)

def question(request):
    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "webtoon": page_obj,

    }
    return render(request, 'question.html',context)

def bulletin(request):
    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "webtoon": page_obj,

    }
    return render(request, 'bulletin.html', context)

def list(request):
    list = Webtoon.objects.filter(~Q(user_id='')).order_by('-pk')
    paginator1 = Paginator(list, 30)
    page_number1 = request.GET.get('page')
    page_list = paginator1.get_page(page_number1)
    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "webtoon": page_obj,
        "page_list": page_list,

    }
    return render(request, 'list.html', context)

def getlist(request,getuser):
    list = Webtoon.objects.filter(user_id=getuser).order_by('-pk')
    paginator1 = Paginator(list, 30)
    page_number1 = request.GET.get('page')
    page_list = paginator1.get_page(page_number1)
    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 40)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "webtoon": page_obj,
        "page_list": page_list,

    }
    return render(request, 'getlist.html', context)

def write(request):

    if(request.method == 'POST') :
        test = Webtoon()
        test.name = request.POST['name']
        test.support = request.POST['support']
        test.content = request.POST['content']
        test.thumbnail = request.FILES['thumbnail']
        test.user_id = request.POST.get('user_id', None)
        test.save()
        for img in request.FILES.getlist('imgs'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = test
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()

        return redirect('mainpage')
    else:
        webtoon = Webtoon.objects.all().order_by('-id')
        paginator = Paginator(webtoon, 30)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "webtoon": page_obj,

        }
        return render(request, 'write.html',context)

def detail(request,pk):
    webtoon = Webtoon.objects.all().order_by('-id')
    paginator = Paginator(webtoon, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    ip=  ip.split('.')[0] + "."+ ip.split('.')[1]
    product = Webtoon.objects.get(pk=pk)
    imgs = Photo.objects.filter(post=product).order_by('pk')
    pcomments = Mcomment.objects.filter(post=product.id).order_by('-pk')
    recomments = Mcomment.objects.filter(post=product).order_by('pk')
    parent_comment = request.POST.get('parent_comment_id', None)
    paginator = Paginator(pcomments, 40)
    comment_number = request.GET.get('commentnum')
    comment_obj = paginator.get_page(comment_number)
    if request.method == "POST":
        form = commentForm(request.POST)
        if form.is_valid():
            pcomment = Mcomment()
            pcomment.name=request.POST['name']
            pcomment.content=request.POST['content']
            pcomment.ip=ip
            pcomment.post = product
            pcomment.parent_comment_id=parent_comment

            pcomment.save()
            pcomments = Mcomment.objects.filter(post=product).order_by('-pk')
            recomments = Mcomment.objects.filter(post=product).order_by('pk')
            parent_comment = request.POST.get('parent_comment_id', None)
            paginator = Paginator(pcomments, 40)
            comment_number = request.GET.get('commentnum')
            comment_obj = paginator.get_page(comment_number)
            form = commentForm()
            context = {
                "webtoon": page_obj,
                "imgs": imgs,
                "product": product,
               "recomments":recomments,
                "page_obj": comment_obj,
                "form": form,
                       }
            return render(request, "detail.html", context)
    else:
        form=commentForm()
        context={
            "webtoon": page_obj,
            "imgs": imgs,
            "product": product,
            "recomments":recomments,
            "page_obj": comment_obj,
            "form": form,
        }
    return render(request, 'detail.html',context)