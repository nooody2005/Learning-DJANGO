# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.forms import UserCreationForm

# # Create your views here.
# # def register(request):
# #     if request.method == "POST":
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('myapp:index')
        
# #     else:   
# #         form = UserCreationForm()
# #         return render(request,'users/register.html',{'form':form})
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('myapp:index')

#         else:
#             form = UserCreationForm()

#     return render(request, 'users/register.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('myapp:index')

    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})