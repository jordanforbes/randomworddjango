from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def main(request):
    
    if 'counter' not in request.session:
        request.session['counter']=0
    
    context={
        'randword': get_random_string(length = 14)
    }
        
    print('session counter'+ str(request.session['counter']))
    print('random: '+ request.session['randword'])
    
    
    return render(request, 'index.html', context)

def randomword(request):
    request.session['counter']+=1
    request.session['randword']=get_random_string(length=14)
    print(request.POST)
    
    return redirect('/')