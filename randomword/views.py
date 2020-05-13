from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def main(request):
    request.session['randword'] = get_random_string(length=14)
    
    if 'counter' in request.session:
        request.session['counter']= request.session['counter']+1
    else:
        request.session['counter']=0
    print('session counter'+ str(request.session['counter']))
    print('random: '+ request.session['randword'])
    

    
    # context={
    #     'counter': request.session['counter'],
    #     'randword': get_random_string(length = 14)
    # }
    
    return render(request, 'index.html')

def randomword(request):
    request.session['counter']= request.session['counter']+1
    request.session['randword'] = get_random_string(length=14)
    return redirect()