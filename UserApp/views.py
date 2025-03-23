from rest_framework import viewsets
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from UserApp.models import User, Category, Product, SalesHistory
from UserApp.serializers import UserSerializer, CategorySerializer, ProductSerializer, SaleHistorySerializer

# Create your views here.
### No es necesario pues puedo hacer override a los métodos de viewset de ser necesaria una configuracion especial ###
# @api_view(['GET'])
# def get_users(request, id=None):
#     if id:
#         try:
#             user = User.objects.get(id=id)
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         except User.DoesNotExist:
#             return Response({'Error': 'No hay registros de ese usuario en la base de datos'}, status=404)
#     else:
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

# @api_view(['POST'])
# def add_user(request):
#     if User.objects.filter(username=request.data.get('username')).exists():
#         return Response({'Error': 'Ese usuario ya esta registrado'}, status=400)
    
#     serializer = UserSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
    
#     return Response(serializer.errors, status=400)

class USerViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer