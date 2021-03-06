from django.conf import settings
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = \
    [
        path('', views.index, name='index'),
        path('NewUser/', views.createNewUser, name='NewUser'),
        path('SaveNewUser/', views.SaveNewUser, name='SaveNewUser'),
        path('NewArticle/', views.createNewArticle, name='NewArticle'),
        path('EditArticle/<int:articleID>/', views.editArticle, name='EditArticle'),
        path('DeleteArticle/<int:articleID>/', views.deleteArticle, name='DeleteArticle'),
        path('ReadArticle/<int:articleID>', views.renderArticle, name='ReadArticle'),
        path('ListUserArticles/',views.userArticleList,name='ListUserArticles'),
        path('SearchArticles/', views.SearchWiki, name = 'SearchArticles'),
        path('EditSideContent/<int:sideContentID>/', views.EditSideContent, name='EditSideContent'),
        path('deleteSideContent/<int:sideContentID>/', views.deleteSideContent, name='deleteSideContent'),
        path('NewSideContent/<int:articleID>/', views.NewSideContent, name='NewSideContent'),
        path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
    ]

# <str:SearchItem>/