# coding: utf-8
from rest_framework import permissions
from .serializers import TaskSerializer, UserSerializer, Task, User
from .permissions import IsOwner
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    """
    Esta viewset provê automaticamente as ações: 'list', 'create', 'retrieve', 'update' e 'destroy'.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = (permissions.IsAuthenticated,
    #                      IsOwner,)

    def pre_save(self, obj):
        obj.owner = User.objects.get(pk=1) # self.request.user

    '''
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.all()
        return queryset.filter(owner=user)
    '''


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Esta viewset provê automaticamente as ações: 'list' e 'detail'.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

