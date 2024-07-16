from django.shortcuts import render, redirect
import random

def Index(request): 
    if 'gscore' not in request.session: 
        request.session['gscore'] = 0
        request.session['sscore'] = 0
    if request.method == 'POST': 
        gamer = request.POST['choice']
        system = random.choice(['rock','paper','scissors'])
        result = winner(gamer, system)
        if result == 'Wow, you win!!!': 
            request.session['gscore'] +=1
        elif result == 'you lose!': 
            request.session['sscore'] +=1
        return render(request, 'index.html',{'gamer':gamer, 'system':system, 'result':result, 'gscore': request.session['gscore'],'sscore': request.session['sscore']})
    return render(request, 'index.html', {'gscore': request.session['gscore'], 'sscore': request.session['sscore']})

def winner(gamer, system): 
    if gamer == system: 
        return 'game is tie!!!'
    elif (gamer == 'rock' and system == 'scissors') or  (gamer == 'scissors' and system == 'paper') or  (gamer == 'paper' and system == 'rock'):
        return 'Wow, you win!!!'
    else: 
        return 'you lose!'
    

def Reset(request): 
    request.session['gscore'] = 0
    request.session['sscore'] = 0
    return redirect('index')