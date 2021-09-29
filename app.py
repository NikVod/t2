from flask import Flask

from database import TasksDataBase

app = Flask(__name__)
db = TasksDataBase()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return db.get_tasks()


@app.route("/tasks", methods=["POST"])
def add_new_task():
    return db.add_new_task()


@app.route("/tasks/<int:task_id>/take", methods=["POST"])
def take_task(task_id):
    return db.take_task(task_id, driver_id)


@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    db.complete_task(task_id, driver_id)
    return "ok"


if __name__ == "__main__":
    app.run()
