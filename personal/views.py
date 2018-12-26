from django.shortcuts import render


def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    content = {'content': ['Checkout my github handle','github.com/besarism']}
    return render(request, 'personal/contact.html', content)

