from flask import render_template, request, jsonify, redirect, url_for
from models import db, Task

class TaskRoutes:

    # Home route, renders the index.html template
    @staticmethod
    def home():
        return render_template("index.html")

    # Get all tasks route, returns all tasks in the database
    @staticmethod
    def get_tasks():
        tasks = Task.query.all()
        task_list = [{"task": t.task, "done": t.done, "id": t.id} for t in tasks]
        return jsonify(task_list)

    # Add task route, adds a new task to the database
    @staticmethod
    def add_task():
        data = request.json
        new_task = Task(task=data["task"])
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"message": "Task added!"})

    # Complete task route, marks a task as done
    

    # Delete task route, deletes a task from the database
    