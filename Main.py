from flask import Flask, render_template_string, request, jsonify, send_file
import csv
import os
from datetime import datetime
import json

app = Flask(__name__)

# CSV file path
CSV_FILE = 'tasks.csv'


# Initialize CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'title', 'description', 'priority', 'status', 'created_at', 'updated_at'])


# Read tasks from CSV
def read_tasks():
    tasks = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            tasks = list(reader)
    return tasks


# Write tasks to CSV
def write_tasks(tasks):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
        if tasks:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'description', 'priority', 'status', 'created_at',
                                                      'updated_at'])
            writer.writeheader()
            writer.writerows(tasks)
        else:
            writer = csv.writer(file)
            writer.writerow(['id', 'title', 'description', 'priority', 'status', 'created_at', 'updated_at'])


# Sort tasks
def sort_tasks(tasks, sort_by='date'):
    if sort_by == 'priority':
        priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
        return sorted(tasks, key=lambda x: priority_order.get(x['priority'], 4))
    elif sort_by == 'status':
        return sorted(tasks, key=lambda x: x['status'])
    elif sort_by == 'title':
        return sorted(tasks, key=lambda x: x['title'].lower())
    else:  # date
        return sorted(tasks, key=lambda x: x['created_at'], reverse=True)


HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager - Python Flask</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            padding: 30px;
        }
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
        }
        .form-section {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .form-section h2 {
            color: #333;
            margin-bottom: 20px;
            font-size: 1.5em;
        }
        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-bottom: 15px;
        }
        input, select, textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s;
        }
        input:focus, select:focus, textarea:focus {
            outline: none;
            border-color: #667eea;
        }
        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        .btn-primary {
            background: #667eea;
            color: white;
        }
        .btn-primary:hover {
            background: #5568d3;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        .btn-success {
            background: #28a745;
            color: white;
        }
        .btn-success:hover {
            background: #218838;
        }
        .btn-danger {
            background: #dc3545;
            color: white;
            padding: 8px 12px;
        }
        .btn-danger:hover {
            background: #c82333;
        }
        .btn-secondary {
            background: #6c757d;
            color: white;
        }
        .btn-secondary:hover {
            background: #5a6268;
        }
        .controls {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        .search-box {
            flex: 1;
            min-width: 250px;
        }
        .task-card {
            background: white;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 15px;
            transition: all 0.3s;
        }
        .task-card:hover {
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }
        .task-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 10px;
        }
        .task-title {
            font-size: 1.3em;
            font-weight: 600;
            color: #333;
            margin-bottom: 8px;
        }
        .task-description {
            color: #666;
            margin-bottom: 15px;
        }
        .task-badges {
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
            flex-wrap: wrap;
        }
        .badge {
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            border: 2px solid;
        }
        .badge-high {
            background: #ffe6e6;
            color: #dc3545;
            border-color: #ffcccc;
        }
        .badge-medium {
            background: #fff3cd;
            color: #856404;
            border-color: #ffeaa7;
        }
        .badge-low {
            background: #d4edda;
            color: #155724;
            border-color: #c3e6cb;
        }
        .badge-completed {
            background: #d4edda;
            color: #155724;
            border-color: #c3e6cb;
        }
        .badge-progress {
            background: #d1ecf1;
            color: #0c5460;
            border-color: #bee5eb;
        }
        .badge-pending {
            background: #e9ecef;
            color: #495057;
            border-color: #dee2e6;
        }
        .task-meta {
            font-size: 12px;
            color: #999;
        }
        .task-actions {
            display: flex;
            gap: 8px;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
            padding-top: 30px;
            border-top: 2px solid #e9ecef;
        }
        .stat-card {
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .stat-card.blue {
            background: #e3f2fd;
        }
        .stat-card.yellow {
            background: #fff9c4;
        }
        .stat-card.purple {
            background: #f3e5f5;
        }
        .stat-card.green {
            background: #e8f5e9;
        }
        .stat-label {
            color: #666;
            font-size: 14px;
            margin-bottom: 5px;
        }
        .stat-value {
            font-size: 32px;
            font-weight: bold;
        }
        .stat-card.blue .stat-value {
            color: #1976d2;
        }
        .stat-card.yellow .stat-value {
            color: #f57f17;
        }
        .stat-card.purple .stat-value {
            color: #7b1fa2;
        }
        .stat-card.green .stat-value {
            color: #388e3c;
        }
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: #999;
        }
        .empty-state svg {
            width: 80px;
            height: 80px;
            margin-bottom: 20px;
            opacity: 0.3;
        }
        #editingMessage {
            background: #fff3cd;
            padding: 10px 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            color: #856404;
            border-left: 4px solid #ffc107;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📋 Task Manager</h1>
        <p class="subtitle">Organize and track your tasks efficiently with Python Flask</p>

        <div class="form-section">
            <h2 id="formTitle">Add New Task</h2>
            <div id="editingMessage" style="display:none;">
                Currently editing a task. Click "Cancel" to add a new task instead.
            </div>
            <form id="taskForm">
                <input type="hidden" id="taskId" value="">
                <div class="form-grid">
                    <input type="text" id="title" placeholder="Task Title *" required>
                    <input type="text" id="description" placeholder="Task Description">
                    <select id="priority">
                        <option value="Low">Low Priority</option>
                        <option value="Medium" selected>Medium Priority</option>
                        <option value="High">High Priority</option>
                    </select>
                    <select id="status">
                        <option value="Pending" selected>Pending</option>
                        <option value="In Progress">In Progress</option>
                        <option value="Completed">Completed</option>
                    </select>
                </div>
                <div style="display: flex; gap: 10px;">
                    <button type="submit" class="btn btn-primary" id="submitBtn">
                        ➕ Add Task
                    </button>
                    <button type="button" class="btn btn-secondary" id="cancelBtn" style="display:none;" onclick="cancelEdit()">
                        ✖️ Cancel
                    </button>
                </div>
            </form>
        </div>

        <div class="controls">
            <input type="text" id="searchBox" class="search-box" placeholder="🔍 Search tasks..." onkeyup="filterTasks()">
            <select id="sortBy" class="btn" onchange="loadTasks()">
                <option value="date">Sort by Date</option>
                <option value="priority">Sort by Priority</option>
                <option value="status">Sort by Status</option>
                <option value="title">Sort by Title</option>
            </select>
            <a href="/download" class="btn btn-success">
                💾 Download CSV
            </a>
        </div>

        <div id="taskList"></div>

        <div class="stats">
            <div class="stat-card blue">
                <div class="stat-label">Total Tasks</div>
                <div class="stat-value" id="totalTasks">0</div>
            </div>
            <div class="stat-card yellow">
                <div class="stat-label">Pending</div>
                <div class="stat-value" id="pendingTasks">0</div>
            </div>
            <div class="stat-card purple">
                <div class="stat-label">In Progress</div>
                <div class="stat-value" id="progressTasks">0</div>
            </div>
            <div class="stat-card green">
                <div class="stat-label">Completed</div>
                <div class="stat-value" id="completedTasks">0</div>
            </div>
        </div>
    </div>

    <script>
        let allTasks = [];

        // Load tasks on page load
        document.addEventListener('DOMContentLoaded', function() {
            loadTasks();
        });

        // Form submission
        document.getElementById('taskForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const taskId = document.getElementById('taskId').value;

            if (taskId) {
                updateTask(taskId);
            } else {
                addTask();
            }
        });

        // Add task
        function addTask() {
            const data = {
                title: document.getElementById('title').value,
                description: document.getElementById('description').value,
                priority: document.getElementById('priority').value,
                status: document.getElementById('status').value
            };

            fetch('/add_task', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                if (result.success) {
                    document.getElementById('taskForm').reset();
                    loadTasks();
                }
            });
        }

        // Load tasks
        function loadTasks() {
            const sortBy = document.getElementById('sortBy').value;
            fetch(`/get_tasks?sort_by=${sortBy}`)
                .then(response => response.json())
                .then(data => {
                    allTasks = data.tasks;
                    displayTasks(allTasks);
                    updateStats(allTasks);
                });
        }

        // Display tasks
        function displayTasks(tasks) {
            const taskList = document.getElementById('taskList');

            if (tasks.length === 0) {
                taskList.innerHTML = `
                    <div class="empty-state">
                        <svg fill="currentColor" viewBox="0 0 20 20">
                            <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z"/>
                            <path fill-rule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clip-rule="evenodd"/>
                        </svg>
                        <h2>No tasks found</h2>
                        <p>Add your first task to get started!</p>
                    </div>
                `;
                return;
            }

            taskList.innerHTML = tasks.map(task => `
                <div class="task-card">
                    <div class="task-header">
                        <div style="flex: 1;">
                            <div class="task-title">${task.title}</div>
                            <div class="task-description">${task.description}</div>
                            <div class="task-badges">
                                <span class="badge badge-${task.priority.toLowerCase()}">${task.priority}</span>
                                <span class="badge badge-${task.status.toLowerCase().replace(' ', '')}">${task.status}</span>
                            </div>
                            <div class="task-meta">Created: ${new Date(task.created_at).toLocaleString()}</div>
                        </div>
                        <div class="task-actions">
                            <button class="btn btn-primary" onclick='editTask(${JSON.stringify(task)})' style="padding: 8px 12px;">✏️</button>
                            <button class="btn btn-danger" onclick="deleteTask('${task.id}')">🗑️</button>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        // Edit task
        function editTask(task) {
            document.getElementById('taskId').value = task.id;
            document.getElementById('title').value = task.title;
            document.getElementById('description').value = task.description;
            document.getElementById('priority').value = task.priority;
            document.getElementById('status').value = task.status;

            document.getElementById('formTitle').textContent = 'Edit Task';
            document.getElementById('submitBtn').innerHTML = '💾 Update Task';
            document.getElementById('submitBtn').className = 'btn btn-success';
            document.getElementById('cancelBtn').style.display = 'inline-flex';
            document.getElementById('editingMessage').style.display = 'block';

            window.scrollTo({top: 0, behavior: 'smooth'});
        }

        // Cancel edit
        function cancelEdit() {
            document.getElementById('taskForm').reset();
            document.getElementById('taskId').value = '';
            document.getElementById('formTitle').textContent = 'Add New Task';
            document.getElementById('submitBtn').innerHTML = '➕ Add Task';
            document.getElementById('submitBtn').className = 'btn btn-primary';
            document.getElementById('cancelBtn').style.display = 'none';
            document.getElementById('editingMessage').style.display = 'none';
        }

        // Update task
        function updateTask(taskId) {
            const data = {
                id: taskId,
                title: document.getElementById('title').value,
                description: document.getElementById('description').value,
                priority: document.getElementById('priority').value,
                status: document.getElementById('status').value
            };

            fetch('/update_task', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                if (result.success) {
                    cancelEdit();
                    loadTasks();
                }
            });
        }

        // Delete task
        function deleteTask(taskId) {
            if (confirm('Are you sure you want to delete this task?')) {
                fetch('/delete_task', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({id: taskId})
                })
                .then(response => response.json())
                .then(result => {
                    if (result.success) {
                        loadTasks();
                    }
                });
            }
        }

        // Filter tasks
        function filterTasks() {
            const searchTerm = document.getElementById('searchBox').value.toLowerCase();
            const filtered = allTasks.filter(task => 
                task.title.toLowerCase().includes(searchTerm) || 
                task.description.toLowerCase().includes(searchTerm)
            );
            displayTasks(filtered);
        }

        // Update statistics
        function updateStats(tasks) {
            document.getElementById('totalTasks').textContent = tasks.length;
            document.getElementById('pendingTasks').textContent = tasks.filter(t => t.status === 'Pending').length;
            document.getElementById('progressTasks').textContent = tasks.filter(t => t.status === 'In Progress').length;
            document.getElementById('completedTasks').textContent = tasks.filter(t => t.status === 'Completed').length;
        }
    </script>
</body>
</html>
'''


@app.route('/')
def index():
    initialize_csv()
    return render_template_string(HTML_TEMPLATE)


@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    tasks = read_tasks()

    new_task = {
        'id': str(int(datetime.now().timestamp() * 1000)),
        'title': data['title'],
        'description': data.get('description', ''),
        'priority': data['priority'],
        'status': data['status'],
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }

    tasks.append(new_task)
    write_tasks(tasks)

    return jsonify({'success': True, 'task': new_task})


@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    sort_by = request.args.get('sort_by', 'date')
    tasks = read_tasks()
    sorted_tasks = sort_tasks(tasks, sort_by)
    return jsonify({'tasks': sorted_tasks})


@app.route('/update_task', methods=['POST'])
def update_task():
    data = request.get_json()
    tasks = read_tasks()

    for i, task in enumerate(tasks):
        if task['id'] == data['id']:
            tasks[i] = {
                'id': data['id'],
                'title': data['title'],
                'description': data.get('description', ''),
                'priority': data['priority'],
                'status': data['status'],
                'created_at': task['created_at'],
                'updated_at': datetime.now().isoformat()
            }
            break

    write_tasks(tasks)
    return jsonify({'success': True})


@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.get_json()
    tasks = read_tasks()
    tasks = [task for task in tasks if task['id'] != data['id']]
    write_tasks(tasks)
    return jsonify({'success': True})


@app.route('/download')
def download():
    if os.path.exists(CSV_FILE):
        return send_file(CSV_FILE, as_attachment=True,
                         download_name=f'tasks_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    return jsonify({'error': 'No file found'}), 404


if __name__ == '__main__':
    print("🚀 Starting Flask Task Manager Application...")
    print("📂 CSV file will be saved as: tasks.csv")
    print("🌐 Open your browser and go to: http://127.0.0.1:5000")
    print("\n✨ Features:")
    print("  • Add, Edit, Delete tasks")
    print("  • Real-time CSV updates")
    print("  • Search and Sort functionality")
    print("  • Download CSV file")
    print("\n Press Ctrl+C to stop the server\n")
    app.run(debug=True, port=5000)