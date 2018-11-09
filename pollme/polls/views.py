from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import choice, video

def polls_list(request):

    polls = video.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/polls_list.html', context)

def poll_detail(request, video_id):

    #poll = video.objects.get(id=video_id)
    poll = get_object_or_404(video, id=video_id)

    if request.method == "POST":
        print(request.POST)
        print("Thanks for your input!")

    if request.method == "GET":
        print(request.GET)
        print("hi im colin and im here to GET my sister from the store")

    context = {'poll': poll}
    return render(request, 'polls/video_detail.html', context)


def SSB64(request):
    return render(request, 'polls/layout_N64.html' )


def video_vote(request, video_id):
    return HttpResponse('Video Id: {}'.format(video_id))


