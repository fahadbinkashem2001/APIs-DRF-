from django.urls import path,include

from rest_framework.routers import DefaultRouter,APIRootView
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.permissions import AllowAny

from .views import task_list,task_details,TaskList,TaskDetails,TaskViewSet,AuthorViewSet,BookViewSet,StudentViewSet,UniversityViewSet

class CustomAPIRootView(APIRootView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = [AllowAny]  # root only lists links, no data

class CustomRouter(DefaultRouter):
    APIRootView = CustomAPIRootView

router = CustomRouter()

router.register("tasks",TaskViewSet,basename="task")
router.register("authors",AuthorViewSet,basename="author")
router.register("books",BookViewSet,basename="book")
router.register("students",StudentViewSet,basename="student")
router.register("universities",UniversityViewSet,basename="university")

urlpatterns = [
    # path("tasks/",task_list),
    # path("tasks/<int:pk>/",task_details),
    # path("tasks/",TaskList.as_view()),
    # path("tasks/<int:pk>/",TaskDetails.as_view()),
    path("",include(router.urls)),
]
