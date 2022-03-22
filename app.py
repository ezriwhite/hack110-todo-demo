from flask import Flask, render_template, request
from helpers import todo

app: Flask = Flask(__name__)


todo_list: list[todo] = []
todo_count: int = 0


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/view-todo-list', methods=["GET", "POST"])
def view_todo_list():
    if request.method == "POST" and len(todo_list) > 0:
        # an item was checked/unchecked - len > 0 ensures refreshes don't potentially crash the site.
        id: int = int(request.form['check-button'])
        todo_list[id].visible = not todo_list[id].visible
    return render_template('view-list.html', todo_list=todo_list)
    


@app.route('/edit-todo<todo_number>')
def edit_todo(todo_number: str):
    return render_template('edit-todo.html', user=todo_list[int(todo_number)])


@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global todo_list
        global todo_count
        print(request.form)
        title: str = request.form['title']
        description: str = request.form['description']
        color: str = request.form['color']

        if title == '':
            return render_template("create-todo.html")

        new_todo: todo = todo(todo_count, title, description, color)
        todo_list.append(new_todo)

        todo_count += 1

        return render_template("success.html", todo=todo)
    return render_template("create-todo.html")


if __name__ == '__main__':
    app.run(debug=True)
