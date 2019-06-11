import logging
from rest_framework.views import APIView

from apps.common.result import ResultResponse
from apps.movies_api.main_serializers import *
from apps.movies_api.models import *


class FilmView(APIView):
    # 不同请求方式不同处理

    def get(self, request):
        # 把数据库里都film表转化成json数据返回
        try:
            films = Film.objects.all()
            # 转json，多个对象many=True 默认单个
            serializer = FilmSerializer(films, many=True)
            # 生成json数据serializer.data 并返回
            # JsonResponse默认只能传字典,serializer.data不是字典需要加 safe=False
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class CateView(APIView):
    # 不同请求方式不同处理

    def get(self, request):
        # 把数据库里都film表转化成json数据返回
        try:
            cate = CateLog.objects.all()
            # 转json，多个对象many=True 默认单个
            serializer = CateSerializer(cate, many=True)
            # 生成json数据serializer.data 并返回
            # JsonResponse默认只能传字典,serializer.data不是字典需要加 safe=False
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DecadeView(APIView):
    # 不同请求方式不同处理

    def get(self, request):
        # 把数据库里都film表转化成json数据返回
        try:
            decade = Decade.objects.all()
            # 转json，多个对象many=True 默认单个
            serializer = DecadeSerializer(decade, many=True)
            # 生成json数据serializer.data 并返回
            # JsonResponse默认只能传字典,serializer.data不是字典需要加 safe=False
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class LocView(APIView):
    # 不同请求方式不同处理

    def get(self, request):
        # 把数据库里都film表转化成json数据返回
        try:
            loc = Loc.objects.all()
            # 转json，多个对象many=True 默认单个
            serializer = LocSerializer(loc, many=True)
            # 生成json数据serializer.data 并返回
            # JsonResponse默认只能传字典,serializer.data不是字典需要加 safe=False
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class SubView(APIView):
    # 不同请求方式不同处理

    def get(self, request):
        # 把数据库里都film表转化成json数据返回
        try:
            sub = Subclass.objects.all()
            # 转json，多个对象many=True 默认单个
            serializer = SubSerializer(sub, many=True)
            # 生成json数据serializer.data 并返回
            # JsonResponse默认只能传字典,serializer.data不是字典需要加 safe=False
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class TypeView(APIView):
    # 不同请求方式不同处理

    def get(self, request):
        # 把数据库里都film表转化成json数据返回
        try:
            types = Type.objects.all()
            # 转json，多个对象many=True 默认单个
            serializer = TypeSerializer(types, many=True)
            # 生成json数据serializer.data 并返回
            # JsonResponse默认只能传字典,serializer.data不是字典需要加 safe=False
            return ResultResponse.success_to_response(serializer.data)
        except Exception as e:
            logging.error(e)
            return ResultResponse.error_to_response()

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass