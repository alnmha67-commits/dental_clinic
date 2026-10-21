from django.shortcuts import render
def custom_500(request):
    return render(request,"500.html",status=500)
def custom_400(request,exception=None):
    return render(request,"400.html",status=400)