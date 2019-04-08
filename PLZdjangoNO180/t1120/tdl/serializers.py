# coding=utf-8
# from rest_framework import serializers
#
#
# class TodoSerializer(serializers.Serializer):
#     task = serializers.CharField(max_length=1000)
#     is_delete = serializers.BooleanField(default=False)
#     ct = serializers.CharField(max_length=50)
#
#     def create(self, validated_data):
#         pass
#
#     def update(self, instance, validated_data):
#         pass
from django.contrib.auth.models import User
from rest_framework import serializers
from t1120.tdl.models import todoModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class todoItem(serializers.ModelSerializer):
    todoContent = serializers.CharField(allow_null=True, allow_blank=True)
    isDone = serializers.BooleanField()

    def create_item(self, data):  # 需确认修改
        todoContent = todoModel(todoContent=data['todoContent'])
        todoContent.save()
        return todoContent

    def delete_todo(self, instance):  # 需修改
        if instance.title == self.data['title']:
            instance.remove_status = True
            instance.save()
            return "Delete successfully"
        else:
            return "Delete failed"

    class Meta:
        model = todoModel
        fields = ('id', 'todoContent', 'isDone', 'expireDate', 'priority')
