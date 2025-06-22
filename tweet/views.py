from django.shortcuts import render
from .models import Tweet
from .forms import Tweetform ,UserRegistrationForm  
from django.shortcuts import get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def index(request):
    return render(request, 'tweet/index.html') 

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet/tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = Tweetform(request.POST,request.FILES)
        if form.is_valid():                             #in this point form is being saved
           tweet= form.save(commit=False)
           tweet.user = request.user    
           tweet.save()
           return redirect('tweet_list')

    else:
        form = Tweetform()
    return render(request,'tweet/tweet_form.html',{ 'form': form })

@login_required
def tweet_edit(request,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=request.user)
    if request.method =='POST':
          form = Tweetform(request.POST,request.FILES ,instance=tweet)
          if form.is_valid():                           #in this point form is being saved
               tweet=form.save(commit=False)
               tweet.user=request.user
               tweet.save()
               return redirect('tweet_list')
    else:
        form=Tweetform(instance=tweet)
    return render(request,'tweet/tweet_form.html',{ 'form': form })
 
@login_required
def tweet_delete(request,tweet_id):
    tweet= get_object_or_404(Tweet,pk=tweet_id,user=request.user)     
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')           
    return render(request,'tweet/tweet_delete.html',{'tweet':tweet})


#jab bhi edit ka tweet de rahe hai to instance dena  hoga  by the we get to knoe that we are editing that same tweet 


def register(request):
         if request.method == 'POST':
              form = UserRegistrationForm(request.POST)
              if form.is_valid():
                   user=form.save(commit=False)
                   user.set_password(form.cleaned_data['password1'])
                   form.save()
                   login(request,user)
                   return redirect('tweet_list')
         else:
              form=UserRegistrationForm()
         return render(request,'registration/registration.html',{'form':form})
