from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   #need to require log in for classes, allows testfunc method
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)




class PostListView(ListView):
    model = Post        #tells list view what model to query (in this case, it is all of our posts)
    template_name = 'blog/home.html'        #tells django where to look for template instead of default
    context_object_name = 'posts'    #set this variable for posts
    # ordering = ['date_posted']    #newest posts show first
    ordering = ['date_posted']     #oldest posts show first
    paginate_by = 4

class UserPostListView(ListView):
    model = Post        #tells list view what model to query (in this case, it is all of our posts)
    template_name = 'blog/user_posts.html'        #tells django where to look for template instead of default
    context_object_name = 'posts'    #set this variable for posts
    # ordering = ['date_posted']    #newest posts show first
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #will get an object from database if exists...or will return 404 error
        return Post.objects.filter(author=user).order_by('-date_posted')    #filter will limit to user and sort by reverse date order

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()    #get post
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()    #get post
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def family(request):
    return render(request, 'blog/family.html', {'title': 'Family'})

