from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

  # Sample data
 tasks = [
      {'name': 'Task 1', 'type': 'Work'},
      {'name': 'Task 2', 'type': 'Personal'}
  ]

@app.route('/')
def home():
      return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
      task_name = request.form.get('task_name')
      task_type = request.form.get('task_type')
      if task_name and task_type:
          tasks.append({'name': task_name, 'type': task_type})
      return redirect(url_for('home'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
      if 0 <= task_id < len(tasks):
          del tasks[task_id]
      return redirect(url_for('home'))
if __name__ == '__main__':
      app.run(debug=True)
