from django.shortcuts import render

def base_view(request):
    return render(request, "base.html")  # This will render base.html directly

def index(request):
    return render(request, "pages/portfolio.html")

def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
    ]
    return render(request, 'pages/dashboard.html', {'data': data})