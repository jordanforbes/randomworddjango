from django.shortcuts import render
from django.utils.crypto import get_random_string

def main(request):
    if 'counter' in request.session:
        request.session['counter']= request.session['counter']+1
    else:
        request.session['counter']=0
    print('session counter'+ str(request.session['counter']))
    print('random: '+get_random_string(length=14))
    
    context={
        'counter': request.session['counter'],
        'randword': get_random_string(length = 14)
    }
    return render(request, 'index.html', context)