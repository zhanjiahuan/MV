# 核心功能 将模型转化为json数据
from rest_framework import serializers

from apps.movies_api.models import *


#   film表json数据
class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


#   cate_log表 左侧菜单列表字段/分类字段 json数据
class CateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CateLog
        fields = '__all__'


#   decade表 年代字段 json数据
class DecadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decade
        fields = '__all__'


#   loc表 地区字段 json数据
class LocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loc
        fields = '__all__'


#   subclass表 子类字段 json数据
class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subclass
        fields = '__all__'


#   type表 年代字段 json数据
class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
