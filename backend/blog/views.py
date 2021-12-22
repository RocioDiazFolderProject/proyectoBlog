from django.db.models.fields import SlugField
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import PostForm, UserRegisterForm, ComentarioForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {'posts':posts}

    return render(request, 'index.html', context)

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} ha sido creado correctamente')
            return redirect('index')
    else:
        form = UserRegisterForm()


    context = { 'form': form}
    return render(request, 'register.html', context)

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Publicación creada')
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})

def edit_post(request,content):
    post = get_object_or_404(Post,content=content)
    
    contexto = {
        'form':PostForm(instance=post)
    }
    
    if request.method=='POST':
        formulario = PostForm(data=request.POST, instance=post)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        contexto['form'] = formulario

    return render(request,'edit.html', contexto)

def eliminar_post(request,content):
    post = get_object_or_404(Post,content=content)
    post.delete()
    return redirect('index')

def detalle_post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    post = Post.objects.get(
        slug = slug
    )
    
    contexto = {'detalle_post':post,           
            }

    return render(request,'detalle_post.html',contexto)

def comentario(request,slug):
    post = get_object_or_404(Post, slug=slug)
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.user = current_user
            com.post = post
            com.save()
            messages.success(request, 'Comentario publicado')
            return redirect('index')
    else:
        form = ComentarioForm()
        return render(request, 'comentario.html', {'form': form})