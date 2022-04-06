from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate(self, data):
        author = get_object_or_404(
            User,
            username=data['following'].username
        )
        is_following = Follow.objects.filter(
            user=self.context['request'].user, following=author
        ).exists()
        if is_following:
            raise serializers.ValidationError(
                'Вы уже подписаны на этого автора.'
            )
        if author == self.context['request'].user:
            raise serializers.ValidationError(
                'Вы не можете подписаться на самого себя.'
            )
        return data

    class Meta:
        model = Follow
        read_only_fields = ('user',)
        exclude = ('id',)
