from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

from discount_cart.application.DiscountService import DiscountService


class Discounts(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def post(self, request) -> Response:
        discount_data = DiscountPostSerializer(data=request.data)

        if not discount_data.is_valid():
            return Response({"message": "Not Valid"}, status=status.HTTP_400_BAD_REQUEST)

        code = str(discount_data.validated_data['code'])
        cart_number = int(discount_data.validated_data['cart'])
        cart_amount = float(discount_data.validated_data['amount_cart'])

        discount = DiscountService()
        return discount.response(code, cart_number, cart_amount)
