from django.shortcuts import redirect, render

from .forms import *


def add_model(request):
    if request.method == 'POST':
        form = AddModelForm(request.POST)
        if form.is_valid():
                entry = form.save(commit=False)
                entry.author = request.user
                entry.save()
                return redirect('/')
        else:
            form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddModelForm()
    return render(request, 'blog/create_post.html', {'form':form})