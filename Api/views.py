from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import APITodolist
from .serializer import HomeSerializer


# Create your views here.


@api_view(['GET'])
def tasklist(request):
    task = APITodolist.objects.all()
    serializer = HomeSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskdetail(request, id):
    task = APITodolist.objects.get(id=id)
    serializer = HomeSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskupdate(request, id):
    task = APITodolist.objects.get(id=id)
    serializer = HomeSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskdelete(request, id):
    task = APITodolist.objects.get(id=id)
    task.delete()
    return Response('Task deleted successfully')


@api_view(['POST'])
def taskcreate(request):
    serializer = HomeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
