from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions, status


class PostApiView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class CategoryApiView(viewsets.ModelViewSet):
    serializer_class =  CategorySerializer
    queryset = Category.objects.all()

class TagApiView(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

class CommentApiView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class SignUpApiView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)

class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
    })


class ProfileApiView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id) 
