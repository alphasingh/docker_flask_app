from flask import render_template, request, url_for, redirect, Blueprint
from pymongo import MongoClient
from bson.objectid import ObjectId

bp = Blueprint('todos', __name__)


client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos


def parse_todo_doc(__doc):
    return {
        'id': __doc.get('id', 1),
        'task': __doc.get('task', 'Task'),
        'isCompleted': __doc.get('isCompleted', True)
    }


@bp.route('/ui', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        is_todo_completed = degree == 'Important'
        new_todo = {
            'content': content,
            'degree': degree,
            'task': content,
            'isCompleted': is_todo_completed
        }
        todos.insert_one(new_todo)
        return redirect(url_for('todos.index'))

    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)


@bp.post('/<oid>/delete/')
def delete(oid):
    todos.delete_one({"_id": ObjectId(oid)})
    return redirect(url_for('todos.index'))


@bp.route('/')
def get_all_todos_from_db():
    # all_todo_items = todos.find()
    all_todo_items = [parse_todo_doc(doc) for doc in todos.find()]
    json_response = {'todos': all_todo_items, 'updated': '13 FEB 2024'}
    json_headers = {'Access-Control-Allow-Origin': '*'}
    return json_response, 200, json_headers
