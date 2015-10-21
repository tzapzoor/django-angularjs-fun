from rest_framework import permissions, viewsets
from rest_framework.response import Response
from blog.serializer import BlogPostSerializer

from blog.models import BlogPost


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.order_by('-created_at')
    serializer_class = BlogPostSerializer

    # def get_permissions(self):
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return (permissions.AllowAny(),)
    #     return (permissions.IsAuthenticated(), IsAuthorOfPost())

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)

        return super(BlogPostViewSet, self).perform_create(serializer)

# class AccountPostsViewSet(viewsets.ViewSet):
#     queryset = Post.objects.select_related('author').all()
#     serializer_class = PostSerializer
#
#     def list(self, request, account_username=None):
#         queryset = self.queryset.filter(author__username=account_username)
#         serializer = self.serializer_class(queryset, many=True)
#
#         return Response(serializer.data)