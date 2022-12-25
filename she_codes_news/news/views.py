from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Category
from .forms import StoryForm
from django.shortcuts import render
from django.views.generic.edit import DeleteView, UpdateView


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('?')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(UpdateView):
    model = NewsStory
    template_name = 'news/editStory.html'
    fields = ['title', 'pub_date', 'content','image','newsCategory']
    success_url = reverse_lazy('news:index')

class DeleteStoryView(DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')


class CategoryView(generic.ListView):
    template_name = 'news/categoryView.html'

    def get_queryset(self):
        '''Return category'''
        return Category.objects.all()
    
    def get_context_data(self, **kwargs):
        cont = super().get_context_data(**kwargs)
        cont['selected_category'] = Category.objects.order_by('-pub_date')[:4]
        return cont

