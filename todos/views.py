from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Todo
from .serializers import TodoSerializer, CreateTodoSerializer


@api_view(['GET'])
def health_check(request):
    """Health check endpoint."""
    return Response({'data': {'status': 'ok'}})


@csrf_exempt
@api_view(['GET', 'POST'])
def todo_list(request):
    """List all todos or create a new todo."""
    if request.method == 'GET':
        status_filter = request.GET.get('status', 'all')
        search_query = request.GET.get('q', '')
        sort_param = request.GET.get('sort', 'created_at_desc')

        queryset = Todo.objects.all()

        # Filter by status
        if status_filter == 'open':
            queryset = queryset.filter(completed=False)
        elif status_filter == 'done':
            queryset = queryset.filter(completed=True)

        # Search
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )

        # Sort
        if sort_param == 'created_at_desc':
            queryset = queryset.order_by('-created_at')
        elif sort_param == 'created_at_asc':
            queryset = queryset.order_by('created_at')
        elif sort_param == 'priority_desc':
            queryset = queryset.order_by('-priority')
        elif sort_param == 'priority_asc':
            queryset = queryset.order_by('priority')

        serializer = TodoSerializer(queryset, many=True)
        return Response({
            'data': serializer.data,
            'meta': {
                'total': len(serializer.data),
                'status': status_filter,
                'sort': sort_param,
            }
        })

    elif request.method == 'POST':
        serializer = CreateTodoSerializer(data=request.data)
        if serializer.is_valid():
            todo = serializer.save()
            return Response({'data': TodoSerializer(todo).data}, status=status.HTTP_201_CREATED)
        return Response({
            'error': {
                'code': 'VALIDATION_ERROR',
                'message': 'Invalid input data',
                'details': serializer.errors,
            }
        }, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):
    """Retrieve, update or delete a todo."""
    # id from URL is uuid; DB column is TEXT, so pass string
    pk = str(id) if id else None
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({
            'error': {
                'code': 'NOT_FOUND',
                'message': 'Todo not found',
            }
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response({'data': serializer.data})

    elif request.method == 'PUT':
        # Only pass fields that are allowed to be updated (exclude read_only)
        data = {k: v for k, v in (request.data or {}).items()
                if k in ('title', 'description', 'completed', 'priority')}
        serializer = TodoSerializer(todo, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})
        return Response({
            'error': {
                'code': 'VALIDATION_ERROR',
                'message': 'Invalid input data',
                'details': serializer.errors,
            }
        }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
