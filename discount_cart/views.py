from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
import json


@api_view(['POST'])
def post(request):
    code = DiscountPostSerializer(data=request.data)

    if code.is_valid():
        if DiscountCart.objects.filter(code=code.validated_data['code']).exists():
            discount = DiscountCart.objects.get(code=code.validated_data['code'])
        else:
            return Response(json.dumps({"status": "Code does not exist"}))

        if discount.status and discount.valid_date_end > datetime.now(timezone.utc):
            discount.cart, discount.status = code.validated_data['cart'], False
            discount.save(update_fields=["cart", "status"])

            cart_sum = float(code.validated_data['amount_cart'])
            new_sum_cart = cart_sum - float(discount.nominal)
            if new_sum_cart < 0:
                new_sum_cart = 0
            return Response(json.dumps({"amount_cart": new_sum_cart, "cart": code.validated_data['cart']}))
        else:
            return Response(json.dumps({"status": "Error"}))
    else:
        return Response(json.dumps({"status": "Not Valid"}))


@api_view(['GET'])
def get(request):
    discount_cart_all = DiscountCart.objects.all()
    serializer = DiscountSerializer(discount_cart_all, many=True)
    return Response(serializer.data)

'''
#Another variant
class Discounts(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, BasicAuthentication)

    def get(self, request):
        discount_cart_all = DiscountCart.objects.all()
        serializer = DiscountSerializer(discount_cart_all, many=True)
        return Response(serializer.data)

    def post(self, request):
        code = DiscountPostSerializer(data=request.data)

        if code.is_valid():
            if DiscountCart.objects.filter(code=code.validated_data['code']).exists():
                discount = DiscountCart.objects.get(code=code.validated_data['code'])
            else:
                return Response(json.dumps({"status": "Code does not exist"}))

            if discount.status and discount.valid_date_end > datetime.now(timezone.utc):
                discount.cart, discount.status = code.validated_data['cart'], False
                discount.save(update_fields=["cart", "status"])

                cart_sum = float(code.validated_data['amount_cart'])
                new_sum_cart = cart_sum - float(discount.nominal)
                return Response(json.dumps({"amount_cart": new_sum_cart, "cart": code.validated_data['cart']}))
            else:
                return Response(json.dumps({"status": "Error"}))
        else:
            return Response(json.dumps({"status": "Not Valid"}))
'''