from django.shortcuts import render


def index(request):
    template_data = {}
    template_data['title'] = 'Cine Videos'
    return render(request, 'home/index.html', {
        'template_data': template_data
    })

def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html')