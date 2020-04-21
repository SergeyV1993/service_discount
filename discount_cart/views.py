from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class Discounts(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def post(self, request):
        discount_data = DiscountPostSerializer(data=request.data)

        if discount_data.is_valid():
            if DiscountCart.objects.filter(code=discount_data.validated_data['code']).exists():
                discount = DiscountCart.objects.get(code=discount_data.validated_data['code'])
            else:
                return Response({"message": "Code does not exist"}, status=status.HTTP_404_NOT_FOUND)

            if discount.status and discount.valid_date_end > datetime.now(timezone.utc):
                discount.cart, discount.status = discount_data.validated_data['cart'], False
                discount.save(update_fields=["cart", "status"])

                cart_sum = float(discount_data.validated_data['amount_cart'])
                new_sum_cart = cart_sum - float(discount.nominal)
                return Response({"amount_cart": new_sum_cart, "cart": discount_data.validated_data['cart']}, )
            else:
                return Response({"message": "Expired"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response({"message": "Not Valid"}, status=status.HTTP_400_BAD_REQUEST)


'''
# Вариант с функциями
from rest_framework.decorators import api_view

@api_view(['POST'])
def post(request):
    discount_data = DiscountPostSerializer(data=request.data)

    if discount_data.is_valid():
        if DiscountCart.objects.filter(code=discount_data.validated_data['code']).exists():
            discount = DiscountCart.objects.get(code=discount_data.validated_data['code'])
        else:
            return Response({"message": "Code does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if discount.status and discount.valid_date_end > datetime.now(timezone.utc):
            discount.cart, discount.status = discount_data.validated_data['cart'], False
            discount.save(update_fields=["cart", "status"])

            cart_sum = float(discount_data.validated_data['amount_cart'])
            new_sum_cart = cart_sum - float(discount.nominal)
            if new_sum_cart < 0:
                new_sum_cart = 0
            return Response({"amount_cart": new_sum_cart, "cart": discount_data.validated_data['cart']},)
        else:
            return Response({"message": "Expired"}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({"message": "Not Valid"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get(request):
    discount_cart_all = DiscountCart.objects.all()
    serializer = DiscountSerializer(discount_cart_all, many=True)
    return Response(serializer.data)
'''
