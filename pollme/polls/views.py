from django.shortcuts import render

from .models import video

"""
reders the polls list template which list all the currently avaiable polls 
"""




def polls_list(request):

    polls = video.objects.all()
    context = {'polls': polls}
    return render(request, 'polls/polls_list.html', context)




def SSB64(request):
    return render(request, 'polls/layout_N64.html' )


