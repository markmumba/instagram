from django.shortcuts import render,redirect
from .models import Image,Comments,Profile
from .forms import NewCommentForm,NewsStatusForm

# Create your views here.

def timelines(request):
    current_user = request.user
    images = Image.objects.order_by('-date_uploaded')
    profiles = Profile.objects.order_by('-last_update')
    comments = Comments.objects.order_by('-time_comment')

    return render(request,'timelines.html',{'images':images ,'profiles':profiles,'user_profile':user_profile,'comments':comments})

def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user_id = current_user.id)
    images = Image.objects.all().filter(profile_id = current_user.id)
    return render(request,'profile.html',{'images':images,'profile':profile})

def new_status(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = NewStatusForm(request.POST,request.FILES)
        if form.is_valid():
            image =form.save()
            image.user = request.user
            image.save()
        return redirect('allTimelines')
    else:
        form = NewsStatusForm()
    return render (request,'new_status.html',{"form":form})


def user_profile(request,user_id):
    profile = Profile.objects.get(id=user_id)
    images = Image.objects.all().filter(user_id=user_id)
    return render(request, 'profile.html', {'profile':profile, 'images':images})
