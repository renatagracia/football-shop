from django.shortcuts import render

def show_main(request):
    context = {
        'app_name': 'Football Shop',
        'name': 'Renata Gracia Adli',
        'npm': '2406399705',
        'class': 'PBP D',
    }

    return render(request, "main.html", context)

