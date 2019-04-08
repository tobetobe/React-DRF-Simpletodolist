# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.shortcuts import render

# class TodoList(APIView):
#     def get(self, request, format=None):
#         todos = Todo.todo.filter(is_delete=False)
#         ser = TodoSerializer(todos, many=True)
#         return Response(ser.data)

# !/usr/bin/env python

from __future__ import print_function
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import todoModel
from serializers import todoItem


@csrf_exempt
def todo_list(request):
    print('todolist')
    if request.method == 'GET':
        todoitems = todoModel.objects.all()
        # print(todoitems)
        serializer = todoItem(todoitems, many=True)
        # print(serializer)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        print(request)
        data = JSONParser().parse(request)
        print(data)
        serializer = todoItem(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print('save success')
            return JsonResponse(serializer.data, status=201)
        print("create Errors:")
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo_detail(request, pk):
    print("tododetail")
    try:
        print("pk=" + pk)
        todoitems = todoModel.objects.get(id=pk)
        # print(todoitems)
        if request.method == 'GET':
            print('GET')
            serializer = todoItem(todoitems)
            return JsonResponse(serializer.data)

        elif request.method == 'POST':
            print('GOT IT!')
            data = JSONParser().parse(request)
            # print(data)
            serializer = todoItem(todoitems, data=data)
            if serializer.is_valid():
                serializer.save()
                print('Update success')
                return JsonResponse(serializer.data)
            print("Now Errors:")
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'PUT':
            print('COMPLETE!')
            todoitems.isDone = True
            todoitems.save()
            print('COMPLETE SUCCESS')
            return HttpResponse(status=204)

        elif request.method == 'DELETE':
            todoitems.delete()
            print('deleteSuccess')
            return HttpResponse(status=204)

    except todoModel.DoesNotExist:
        print('404')
        return HttpResponse(status=404)
