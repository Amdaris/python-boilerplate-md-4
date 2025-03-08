from django.http import JsonResponse, HttpResponse
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class PingApiView(APIView):
    def get(self, request):
        return Response({"result": "pong"})

class Challenge1APIView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Items(type=openapi.TYPE_INTEGER),
    ))
    def post(self, request):
        array = request.data

        # Write the code for Challenge 1 here

        n = len(array)
        
        for i in range(n):
            if array[i] <= 0 or array[i] > n:
                array[i] = 0
        
        for i in range(n):
            val = abs(array[i])
            if 0 < val <= n:
                if array[val - 1] > 0:
                    array[val - 1] = -array[val - 1]
                elif array[val - 1] == 0:
                    array[val - 1] = -(n + 1)
        
        for i in range(n):
            if array[i] >= 0:
                return Response(i + 1)
        
        return Response(n + 1)

class Challenge2APIView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Items(type=openapi.TYPE_INTEGER),
    ))
    def post(self, request):
        array = request.data

        # Write the code for Challenge 2 here

        if len(array) == 0:
            return Response([])
        
        count = 1
        for i in range(1, len(array)):
            if array[i] != array[i - 1]:
                count += 1
        
        result = [0] * count
        index = 0
        sum_val = array[0]
        
        for i in range(1, len(array)):
            if array[i] == array[i - 1]:
                sum_val += array[i]
            else:
                result[index] = sum_val
                index += 1
                sum_val = array[i]
        
        result[index] = sum_val
        return Response(result)

class Challenge3APIView(APIView):
    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Items(type=openapi.TYPE_INTEGER),
    ))
    def post(self, request):
        array = request.data

        # Write the code for Challenge 3 here

        if len(array) == 0:
            return Response(False)
        
        min_val = min(array)
        max_val = max(array)
        
        if max_val - min_val + 1 != len(array):
            return Response(False)
        
        seen = set()
        for num in array:
            if num in seen:
                return Response(False)
            seen.add(num)

        return Response(True)
