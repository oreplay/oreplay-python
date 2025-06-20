from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class NotifyUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        class_id = request.data.get("class_id")
        stage_id = request.data.get("stage_id")
        data = request.data.get("data", {})

        if not class_id or not stage_id:
            return Response(
                {"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST
            )

        group_name = f"class_id_{class_id}_stage_id_{stage_id}"
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "send_update",
                "data": {"class_id": class_id, "stage_id": stage_id, "message": data},
            },
        )

        return Response({"status": "Message sent"}, status=status.HTTP_200_OK)
