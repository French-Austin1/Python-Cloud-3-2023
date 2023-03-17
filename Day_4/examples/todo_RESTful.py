from flask import Flask, jsonify, request

app = Flask(__name__)
todos = [
    {'id': 1, 'task': 'Do laundry'},
    {'id': 2, 'task': 'Walk the dog'},
    {'id': 3, 'task': 'Buy groceries'}
]
next_id = 4

def main():

    @app.route('/todos', methods=['GET'])
    def get_todos():
        return jsonify(todos)

    @app.route('/todos', methods=['POST'])
    def create_todo():
        global next_id
        task = request.json['task']
        todo = {'id': next_id, 'task': task}
        todos.append(todo)
        next_id += 1
        return jsonify(todo), 201

    @app.route('/todos/<int:id>', methods=['GET'])
    def get_todo(id):
        todo = next((t for t in todos if t['id'] == id), None)
        if todo:
            return jsonify(todo)
        else:
            return jsonify({'error': 'Todo not found'}), 404

    @app.route('/todos/<int:id>', methods=['PUT'])
    def update_todo(id):
        todo = next((t for t in todos if t['id'] == id), None)
        if not todo:
            return jsonify({'error': 'Todo not found'}), 404
        task = request.json['task']
        todo['task'] = task
        return jsonify(todo)

    @app.route('/todos/<int:id>', methods=['DELETE'])
    def delete_todo(id):
        global todos
        todos = [t for t in todos if t['id'] != id]
        return '', 204

    return app

if __name__ == "__main__":
    app = main()
    app.run(debug=True)