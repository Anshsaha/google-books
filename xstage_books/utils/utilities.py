from django.http import JsonResponse


def custom_response(
    success=False, message="something went wrong", data=None, status=400
):
    response = {"success": success, "message": message, "data": data}
    return JsonResponse(response, status=status)
