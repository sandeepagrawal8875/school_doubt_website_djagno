from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView ,DeleteView
from django.views.generic.edit import FormMixin

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from .models import Question, Answer
from users.models import Profile
from .forms import AnswerForm

class QuestionListView(LoginRequiredMixin,ListView):
    model = Question
    template_name = 'core/home.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        recent_que = Question.objects.all().order_by("-id")
        most_viewed_que = Question.objects.all().order_by("-views")

        data['recent_que'] = recent_que
        data['most_viewed_que'] = most_viewed_que
        return data


class QuestionCreateView(LoginRequiredMixin,CreateView):
    model = Question
    fields = ['question_title','description','tags']
    template_name = 'core/post-question.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.user = profile
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        data = super(QuestionCreateView, self).get_context_data(**kwargs)
        hot_que = Question.objects.all().order_by('-id')[:7]

        data['hot_que'] = hot_que
        return data 


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'core/question-detial.html'
    context_object_name = 'question'
    form_class = AnswerForm
    

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        data = super(QuestionDetailView, self).get_context_data(**kwargs)
        question = Question.objects.get(pk=self.kwargs.get('pk'))
        profile = Profile.objects.get(user=question.user.user)
        answer = Answer.objects.filter(question=self.kwargs.get('pk'))
        hot_que = Question.objects.all().order_by('-id')[:5]
        
        tag_list = question.tags.split("#")
        
        data['profile'] = profile
        data['answer'] = answer
        data['hot_que'] = hot_que
        data['tag_list'] = tag_list[1:]
        data['form'] = AnswerForm(instance=self.request.user)
        return data 

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        answer = Answer(question = self.get_object(),
                        answer_by = profile,
                        answer=request.POST.get('text'))
        answer.save()
        return self.get(self, request, *args, **kwargs)
    

    def get_object(self, queryset=None):
        item = super().get_object(queryset)
        item.incrementViewCount()
        return item

class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    template_name = "core/question_delete.html"
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.get_object().user.user == self.request.user
    

class QuestionUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Question
    fields = ['question_title','description','tags']
    template_name = "core/question_update.html"
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs['pk']})
    
    def test_func(self):
        return self.get_object().user.user == self.request.user

    def get_context_data(self, **kwargs):
        data = super(QuestionUpdateView, self).get_context_data(**kwargs)
        hot_que = Question.objects.all().order_by('-id')[:7]

        data['hot_que'] = hot_que
        return data 



class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    template_name = "core/answer_delete.html"
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.get_object().answer_by.user == self.request.user

class AnswerUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Answer
    fields = ['answer',]
    template_name = "core/answer_update.html"
    success_url = reverse_lazy('home')
    
    def test_func(self):
        return self.get_object().answer_by.user == self.request.user

    def get_context_data(self, **kwargs):
        data = super(AnswerUpdateView, self).get_context_data(**kwargs)
        hot_que = Question.objects.all().order_by('-id')[:5]

        data['hot_que'] = hot_que
        return data 
