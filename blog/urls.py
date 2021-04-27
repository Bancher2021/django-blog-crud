from django.urls import path, include
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, CommentEditView, CommentCreateView, Dashboard, CommentDeleteView
urlpatterns = [
    path('account/', include("django.contrib.auth.urls")),
    path('', Dashboard, name='dashboard'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='postdelete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='postedit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_new'),
    path('lookup/<int:pk>/delete_comment/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'post_detail'),
    path('lookup/<int:pk>/edit_comment/', CommentEditView.as_view(), name = 'commentedit'),
    path('post/', BlogListView.as_view(), name = 'home'),
]
