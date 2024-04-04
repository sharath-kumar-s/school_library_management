from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from common.helpers.string_validation import is_valid_email_id
from users.controllers.user_details import UserDetailsController

from service_users.controllers.users_controllers import ServiceUserDetailsController


class ServiceUsersDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        controller = ServiceUserDetailsController(request.data, request.user, *args, **kwargs)
        result = controller.service_user_details()
        if result['status'] is True:
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
