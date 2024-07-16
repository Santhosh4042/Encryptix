from django.shortcuts import render

def Calculate(request): 
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')
        if operation == 'add': 
            result = num1 + num2
        elif operation == 'sub': 
            result = num1 - num2
        elif operation == 'mul': 
            result = num1 * num2
        elif operation == 'div': 
            result = num1 / num2 if num2 != 0 else 'Error! please enter valid number'
        elif operation == 'mod': 
            result = num1 % num2
    return render(request, 'index.html', {'result' : result})
