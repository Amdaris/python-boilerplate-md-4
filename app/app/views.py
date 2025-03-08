from app.challenges import challenge1, challenge2, challenge3

from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class PingApiView(APIView):
    def get(self, request):
        return Response({"result": "pong"})

class Challenge1APIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_INTEGER),
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_BOOLEAN,
            )
        }
    )
    def post(self, request):
        array = request.data

        result = challenge1(array)
        
        return Response(result)

class Challenge2APIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_INTEGER),
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Items(type=openapi.TYPE_INTEGER),
            )
        }
    )
    def post(self, request):
        array = request.data

        result = challenge2(array)
        
        return Response(result)

class Challenge3APIView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Items(type=openapi.TYPE_INTEGER),
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_INTEGER,
            )
        }
    )
    def post(self, request):
        array = request.data

        result = challenge3(array)
        
        return Response(result)
