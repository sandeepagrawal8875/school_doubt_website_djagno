from django.urls import path

from .views import QuestionListView, QuestionDetailView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView

urlpatterns = [
    path("", QuestionListView.as_view(), name='home'),
    path("question/<int:pk>/", QuestionDetailView.as_view(), name='detail'),
    path("question/create/", QuestionCreateView.as_view(), name="create"),
    path("question/update/<int:pk>/", QuestionUpdateView.as_view(), name="update"),
    path("question/delete/<int:pk>/", QuestionDeleteView.as_view(), name="delete"),
    
]