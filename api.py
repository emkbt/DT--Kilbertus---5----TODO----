from json import load, dump
from datetime import datetime
from flask import Flask, jsonify, request

db_file = "users.json"
todo_file = "todo.json"
app = Flask(__name__)

@app.route("/auth", methods=['GET'])
def auth():
    """Authenticate with api key
    CURL example:
    curl --location 'http://127.0.0.1:8000/auth?api_key=83a426cd48bdbae86c217bf2217bd038'
    """
    db = load(open(db_file, 'r'))
    success = False
    
    if 'api_key' in request.args:
        for i in db:
            if i['api_key'] == request.args['api_key']:
                success = True
                return jsonify({"success": success, "username": i['username'], "status": 200}), 200
    else:
        return jsonify({"success": success, "status": 400, "message": "Missing API key parameter"}), 400
    if not success:
        return jsonify({"success": success, "status": 401, "message": "Invalid API key"}), 401
    
@app.route("/add", methods=['PUT'])
def add_task():
    """Add task
    CURL example:
    curl --location --request PUT 'http://127.0.0.1:8000/add' --header 'description: Study'
    """
    if request.method == 'PUT':
        success = False
        db = load(open(db_file, 'r'))
        if 'api_key' in request.args:
            for i in db:
                if i['api_key'] == request.args['api_key']:
                    success = True
                    break
        else:
            return jsonify({"success": False, "status": 400, "message": "Missing API key parameter"}), 400
        if success:
            todo = load(open(todo_file, 'r'))
            description = request.headers.get("description")
            due_date = request.headers.get("due_date")
            due_date = datetime.strptime(due_date, "%Y-%m-%d") if due_date else None
            new_task = {"description": description, "due_date": due_date, "completed": False}
            if description:
                todo.append(new_task)
                dump(todo, open(todo_file, 'w'))
                new_task['success'] = True
                new_task['status'] = 200
            return jsonify(new_task), new_task['status']
        else:
            return jsonify({"success": False, "status": 401, "message": "Invalid API key"}), 401
    else:
        return jsonify({"success": False, "status": 405, "message": "Method not allowed"}), 405
    
@app.route("/tasks", methods=['GET'])
def get_tasks():
    """Get list of tasks
    CURL example:
    curl --location 'http://127.0.0.1:8000/tasks?api_key=83a426cd48bdbae86c217bf2217bd038'
    """
    if request.method == 'GET':
        success = False
        todo = load(open(todo_file, 'r'))
        db = load(open(db_file, 'r'))
        if 'api_key' in request.args:
            for i in db:
                if i['api_key'] == request.args['api_key']:
                    success = True
                    break
                    
            if success:
                return jsonify({"success": True, "status": 200, "tasks": todo})
            else:
                return jsonify({"success": False, "status": 401, "message": "Invalid API key"}), 401
        else:
            return jsonify({"success": False, "status": 400, "message": "Missing API key parameter"}), 400
    else:
        return jsonify({"success": False, "status": 405, "message": "Method not allowed"}), 405
    
@app.route("/delete", methods=['DELETE'])
def delete_task():
    """Delete task
    CURL example:
    curl --location --request DELETE 'http://127.0.0.1:8000/delete?api_key=83a426cd48bdbae86c217bf2217bd038' --header 'description: Study'
    """
    if request.method == 'DELETE':
        success = False
        found = False
        todo = load(open(todo_file, 'r'))
        db = load(open(db_file, 'r'))
        
        if 'api_key' in request.args:
            if 'description' in request.headers:
                for i in db:
                    if i['api_key'] == request.args['api_key']:
                        success = True
                        break
                if success:
                    for index, task in enumerate(todo):
                        if task['description'] == request.headers['description']:
                            found = True
                            todo.pop(index)
                            dump(todo, open(todo_file, 'w'))
                            break
                    if found:
                        return jsonify({"success": True, "status": 200}), 200
                    else:
                        return jsonify({"success": False, "status": 400, "message": "Task not found"}), 400
                else:
                    return jsonify({"success": False, "status": 401, "message": "Invalid API key"}), 401
            else:
                return jsonify({"success": False, "status": 400, "message": "Missing description header"}), 400
        else:
            return jsonify({"success": False, "status": 400, "mesage": "Missing API key parameter"}), 400
        
@app.route("/complete", methods=['POST'])
def complete_task():
    """Mark task as completed
    CURL example:
    curl --location --request POST 'http://127.0.0.1:8000/complete?api_key=83a426cd48bdbae86c217bf2217bd038' --header 'description: Study'
    """
    if request.method == 'POST':
        success = False
        found = False
        todo = load(open(todo_file, 'r'))
        db = load(open(db_file, 'r'))
        
        if 'api_key' in request.args:
            if 'description' in request.headers:
                for i in db:
                    if i['api_key'] == request.args['api_key']:
                        success = True
                        break
                if success:
                    for index, task in enumerate(todo):
                        if task['description'] == request.headers['description']:
                            found = True
                            todo[index]['completed'] = True
                            dump(todo, open(todo_file, 'w'))
                            break
                    if found:
                        return jsonify({"success": True, "status": 200}), 200
                    else:
                        return jsonify({"success": False, "status": 400, "message": "Task not found"}), 400
                else:
                    return jsonify({"success": False, "status": 401, "message": "Invalid API key"}), 401
            else:
                return jsonify({"success": False, "status": 400, "message": "Missing description header"}), 400
        else:
            return jsonify({"success": False, "status": 400, "mesage": "Missing API key parameter"}), 400

if __name__ == '__main__':
    app.run(port=8000, debug=True)