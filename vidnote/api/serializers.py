from rest_framework import serializers
from core.models import Video


class coreSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = "__all__"


