from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippetList'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippetDetail'),
    path("users/", views.UserList.as_view()), 
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("snippets/<int:pk>/highlight/", views.SnippetHighlight.as_view(), name="snippet-highlight",),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)