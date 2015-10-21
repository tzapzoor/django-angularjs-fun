from rest_framework import serializers

from authentication.serializers import AccountSerializer
from blog.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True, required=False)

    class Meta:
        model = BlogPost

        fields = ('id', 'author', 'title', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(BlogPostSerializer, self).get_validation_exclusions()

        return exclusions + ['author']