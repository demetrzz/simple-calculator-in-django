from django.shortcuts import render


def addition(num1, num2):
    result = int(num1) + int(num2)
    return result


def subtract(num1, num2):
    result = int(num1) - int(num2)
    return result


def divide(num1, num2):
    result = int(num1) / int(num2)
    return result


def multiply(num1, num2):
    result = int(num1) * int(num2)
    return result


def home(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        if num1 and num2:
            if 'add' in request.POST:
                result = addition(num1, num2)
                return render(request, 'index.html', {'result': result})

            if 'sub' in request.POST:
                result = subtract(num1, num2)
                return render(request, 'index.html', {'result': result})

            if 'div' in request.POST:
                result = divide(num1, num2)
                return render(request, 'index.html', {'result': result})

            if 'mul' in request.POST:
                result = multiply(num1, num2)
                return render(request, 'index.html', {'result': result})
        else:
            return render(request, 'index.html', {'result': "You are missing one number"})
    return render(request, 'index.html')
