from .serializer import (RawMaterialSerializer, PackingMaterialSerializer,
                        ManPowerSerializer, ProductSerializer,
                        EnergycostSerializer, SuperUserSerializer,
                        LoginViewSerializer)
from rest_framework import generics
from .models import (Product, RawMaterial,
                    ManPower, PackingMaterial, 
                    Energycost)
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated

#Classes for Adding data to database
@method_decorator(login_required, name='dispatch')
class ProductAddView(generics.CreateAPIView):
    serializer_class = ProductSerializer
       
@method_decorator(login_required, name='dispatch')
class RawMaterialAddView(generics.CreateAPIView):
    serializer_class = RawMaterialSerializer

@method_decorator(login_required, name='dispatch')    
class PackingMaterialAddView(generics.CreateAPIView):
    serializer_class = PackingMaterialSerializer

@method_decorator(login_required, name='dispatch')
class ManPowerAddView(generics.CreateAPIView):
    serializer_class = ManPowerSerializer

@method_decorator(login_required, name='dispatch')
class EnergycostAddView(generics.CreateAPIView):
    serializer_class = EnergycostSerializer
    

#classes for viewing data in list
@method_decorator(login_required, name='dispatch')
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@method_decorator(login_required, name='dispatch')       
class RawMaterialListView(generics.ListAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

@method_decorator(login_required, name='dispatch')    
class PackingMaterialListView(generics.ListAPIView):
    queryset = PackingMaterial.objects.all()
    serializer_class = PackingMaterialSerializer

@method_decorator(login_required, name='dispatch')
class ManPowerListView(generics.ListAPIView):
    queryset = ManPower.objects.all()
    serializer_class = ManPowerSerializer

@method_decorator(login_required, name='dispatch')
class EnergycostListView(generics.ListAPIView):
    queryset = Energycost.objects.all()
    serializer_class = EnergycostSerializer

#Classes for UpdateView
@method_decorator(login_required, name='dispatch')
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_name'

@method_decorator(login_required, name='dispatch')
class RawMaterialUpdateView(generics.UpdateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    lookup_field = 'material_name'

@method_decorator(login_required, name='dispatch')   
class PackingMaterialUpdateView(generics.UpdateAPIView):
    queryset = PackingMaterial.objects.all()
    serializer_class = PackingMaterialSerializer
    lookup_field = 'pack_name'

@method_decorator(login_required, name='dispatch')
class ManPowerUpdateView(generics.UpdateAPIView):
    queryset = ManPower.objects.all()
    serializer_class = ManPowerSerializer
    lookup_field = 'category_name'

@method_decorator(login_required, name='dispatch')
class EnergycostUpdateView(generics.UpdateAPIView):
    queryset = Energycost.objects.all()
    serializer_class = EnergycostSerializer
    lookup_field = 'category_name'


#Classes for DeleteView
@method_decorator(login_required, name='dispatch')
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_name'

@method_decorator(login_required, name='dispatch')       
class RawMaterialDeleteView(generics.DestroyAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    lookup_field = 'material_name'

@method_decorator(login_required, name='dispatch')    
class PackingMaterialDeleteView(generics.DestroyAPIView):
    queryset = PackingMaterial.objects.all()
    serializer_class = PackingMaterialSerializer
    lookup_field = 'pack_name'

@method_decorator(login_required, name='dispatch')
class ManPowerDeleteView(generics.DestroyAPIView):
    queryset = ManPower.objects.all()
    serializer_class = ManPowerSerializer
    lookup_field = 'category_name'

@method_decorator(login_required, name='dispatch')
class EnergycostDeleteView(generics.DestroyAPIView):
    queryset = Energycost.objects.all()
    serializer_class = EnergycostSerializer
    lookup_field = 'category_name'


#Classes for DetailView
@method_decorator(login_required, name='dispatch')
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'product_name'

@method_decorator(login_required, name='dispatch')
class RawMaterialDetailView(generics.RetrieveAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    lookup_field = 'material_name'


@method_decorator(login_required, name='dispatch')
class PackingMaterialDetailView(generics.RetrieveAPIView):
    queryset = PackingMaterial.objects.all()
    serializer_class = PackingMaterialSerializer
    lookup_field = 'pack_name'

@method_decorator(login_required, name='dispatch')
class ManPowerDetailView(generics.RetrieveAPIView):
    queryset = ManPower.objects.all()
    serializer_class = ManPowerSerializer
    lookup_field = 'category_name'

@method_decorator(login_required, name='dispatch')
class EnergycostDetailView(generics.RetrieveAPIView):
    queryset = Energycost.objects.all()
    serializer_class = EnergycostSerializer
    lookup_field = 'category_name'


class SuperUserCreateView(generics.CreateAPIView):
    serializer_class = SuperUserSerializer

class LoginView(APIView):
    serializer_class = LoginViewSerializer

    def get_serializer(self,*args, **kwargs):
        return LoginViewSerializer(*args, **kwargs)
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return Response({'message':'Login successfull'})
        else:
            return Response({'message':'Login Unsuccesfull'})

class LogoutView(APIView):
    permission_class = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message':'Logout successful'})
