from django.http import JsonResponse
from rest_framework import status

# rest框架定义状态码
# status.HTTP_200_OK


# 自定义状态码
# 请求成功
STATUS_SUCCESS_CODE = 200
# 账号密码错误
STATUS_LOGIN_ERROR_CODE = 1
# 用户已存在
STATUS_USER_EXIST_CODE = 2
MESSAGE_SUCCESS_STR = 'success'
STATUS_ERROR_CODE = 404
MESSAGE_ERROR_STR = 'error'


class ResultResponse:
    @staticmethod
    def success_to_response(data, status=status.HTTP_200_OK, msg=MESSAGE_SUCCESS_STR):
        result = {
            'status': status,
            'msg': msg,
            'data': data,
        }
        return JsonResponse(result)

    @staticmethod
    def error_to_response(status=STATUS_ERROR_CODE, msg=MESSAGE_ERROR_STR):
        result = {
            'status': status,
            'msg': msg,
        }
        return JsonResponse(result)
