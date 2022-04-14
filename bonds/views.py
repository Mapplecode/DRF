from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from .models import Bonds
from .serializers import BondSerializer,BondCreateSerializer

class BondsList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        titles = [{"name":bond.name,"symbol":bond.symbol,"price":bond.price} for bond in Bonds.objects.all() if bond.status =="p"]
        return Response({"data": titles})

class BondCreateAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = BondCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'success':'True'})


# dc14e5021a3e6f4804bc8b3bf719a7b581d18a01e6404a54533e38b0f84ea9c9