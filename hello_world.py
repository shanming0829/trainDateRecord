#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-13 10:10:35
# @Author  : Shanming (shanming0428@163.com)
# @Version : 1.0.0

from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort


app = Flask(__name__)
api = Api(app)


TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}

todoParser = reqparse.RequestParser()
todoParser.add_argument('task')


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class Todo(Resource):
    """docstring for Todo"""

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = todoParser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


class TodoList(Resource):
    """docstring for TodoList"""

    def get(self):
        return TODOS

    def post(self):
        args = todoParser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id

        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


api.add_resource(Todo, '/todos/<todo_id>')
api.add_resource(TodoList, '/todos')

if __name__ == '__main__':
    app.run(debug=True)
