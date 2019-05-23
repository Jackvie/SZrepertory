from rest_framework import serializers

from booktest.models import BookInfo, HeroInfo

class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = BookInfo
	# fields = '__all__'
        fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment')
        read_only_fields = ('id',)
        extra_kwargs = {
            'bread': {'min_value': 0, 'required': True},
            'bcomment': {'min_value': 0, 'required': True},
        }
