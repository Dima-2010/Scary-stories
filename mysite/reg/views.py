from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.views.generic.edit import FormMixin, UpdateView

from reg.forms import ArticlesForm, CommentForm, Articles_adminForm, Post_form, VideoForm, ModerForm
from reg.models import Articles, Articles_admin, Post, Video


# from reg.forms import LoginUserForm, RegisterUserForm


def home(request):
    return render(request, 'reg/home.html')


def articles(request):
    data = {'Articles': Articles.objects.filter(moder=True).order_by('-id')}
    return render(request, 'reg/articles.html', data)


def moder(request):
    data = {'Articles': Articles.objects.filter(moder=False).order_by('-id'),
            'Videos': Video.objects.filter(moder=False).order_by('-id'),
            'Post': Post.objects.filter(moder=False).order_by('-id')}
    return render(request, 'reg/moder.html', data)


def videos(request):
    data = {'Post': Video.objects.filter(moder=True).order_by('-id')}
    return render(request, 'reg/videos.html', data)


@login_required
def profile(request):
    data = {'Articles': Articles.objects.filter(auther=request.user).order_by('-id'),
            'Videos': Video.objects.filter(auther=request.user).order_by('-id'),
            'Post': Post.objects.filter(auther=request.user).order_by('-id')}
    return render(request, 'reg/profile.html', data)


def user(request):
    auther = 'Dima'
    data = {'Articles': Articles.objects.filter(auther__username=auther)}
    return render(request, 'reg/articles.html', data)


class update(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = 'reg/create.html'
    form_class = ArticlesForm
    reise_exceptions = True


class update_video(LoginRequiredMixin, UpdateView):
    model = Video
    template_name = 'reg/create_video.html'
    form_class = VideoForm
    reise_exceptions = True


class update_post(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'reg/create.html'
    form_class = Post_form
    reise_exceptions = True


class moder_up(LoginRequiredMixin, UpdateView):
    model = Articles
    template_name = 'reg/create.html'
    form_class = ModerForm


class create_post(LoginRequiredMixin, CreateView):
    model = Post
    form_class = Post_form
    template_name = 'reg/post.html'
    success_url = 'post'

    def get_context_data(self, **kwargs):
        kwargs['Post'] = Post.objects.filter(moder=True).order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.auther = self.request.user
        self.object.save()
        return super().form_valid(form)


class Search(LoginRequiredMixin, ListView):
    template_name = 'reg/post.html'
    context_object_name = 'Post'

    paginate_by = 9999999999999999999999

    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('q', None)
        return Post.objects.filter(Q(title__iregex=search) | Q(description__iregex=search))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class Search_article(LoginRequiredMixin, ListView):
    template_name = 'reg/articles.html'
    context_object_name = 'Articles'

    paginate_by = 9999999999999999999999

    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('q_2', None)
        return Articles.objects.filter(Q(title__iregex=search) | Q(description__iregex=search))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q_2'] = self.request.GET.get('q_2')
        return context


class del_post(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'reg/del.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post')
    reise_exceptions = True


class del_video(LoginRequiredMixin, DeleteView):
    model = Video
    template_name = 'reg/del_video.html'
    context_object_name = 'video'
    success_url = reverse_lazy('videos')
    reise_exceptions = True


# def post(request):
#    if request.method == 'POST':
#        form = Post_form(request.POST)
#        if form.is_valid:
#            form.save()
#
#    context = {
#        'Post': Post.objects.all(),
#        'form': Post_form()
#    }
#    return render(request, 'reg/post.html', context)


# def create(request):
#    if request.method == 'POST':
#        Articles.objects.create(title=request.POST['title'], description=request.POST['description'],
#                                full_text=request.POST['full_text'], auther=request.POST['auther'],
#                                img=request.POST['img'])
#        return redirect('articles')
#    return render(request, 'reg/create.html')

class create(LoginRequiredMixin, CreateView):
    model = Articles
    form_class = ArticlesForm
    template_name = 'reg/create.html'
    success_url = reverse_lazy('articles')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.auther = self.request.user
        self.object.save()
        return super().form_valid(form)


class create_admin(LoginRequiredMixin, CreateView):
    model = Articles_admin
    form_class = Articles_adminForm
    template_name = 'reg/create_admin.html'
    success_url = reverse_lazy('articles_admin')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.auther = self.request.user
        self.object.save()
        return super().form_valid(form)


class create_video(LoginRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'reg/create_video.html'
    success_url = reverse_lazy('videos')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.auther = self.request.user
        self.object.save()
        return super().form_valid(form)


class search_video(LoginRequiredMixin, ListView):
    template_name = 'reg/videos.html'
    context_object_name = 'Post'

    paginate_by = 9999999999999999999999

    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('q', None)
        return Video.objects.filter(Q(title__iregex=search) | Q(description__iregex=search))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def articles_admin(request):
    data = {'Articles_admin': Articles_admin.objects.all()}
    return render(request, 'reg/articles_admin.html', data)


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'reg/register.html'
    success_url = reverse_lazy('login')


#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        c_def = self.get_user_context(title='Регистрация')
#        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'reg/login.html'

    def get_success_url(self):
        return reverse_lazy('articles')


def Logaut_user(request):
    logout(request)
    return redirect('login')


class details(LoginRequiredMixin, DetailView, FormMixin):
    model = Articles
    template_name = 'reg/details.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('details', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return redirect(request, 'reg/login.html')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.auther = self.request.user
        self.object.save()
        return super().form_valid(form)


class details_video(LoginRequiredMixin, DetailView, FormMixin):
    model = Video
    template_name = 'reg/details_video.html'
    context_object_name = 'Video'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('details_video', kwargs={'pk': self.get_object().id})


class delete(LoginRequiredMixin, DeleteView):
    model = Articles
    success_url = '/articeles'
    template_name = 'reg/delete.html'
    context_object_name = 'article'


class delete_admin(LoginRequiredMixin, DeleteView):
    model = Articles_admin
    success_url = reverse_lazy('articles_admin')
    template_name = 'reg/delete.html'
    context_object_name = 'article'
