from flask import Flask, jsonify, request, render_template
import os
import mysql.connector
import time

app = Flask(__name__)

# MySQL 연결 설정
def get_db_connection():
    # 초기 연결 시도 시 약간의 지연을 추가하여 DB가 준비될 때까지 대기
    retries = 5
    while retries > 0:
        try:
            connection = mysql.connector.connect(
                host=os.environ.get('DB_HOST', 'db'),
                user=os.environ.get('DB_USER', 'user'),
                password=os.environ.get('DB_PASSWORD', 'password'),
                database=os.environ.get('DB_NAME', 'flaskdb')
            )
            return connection
        except mysql.connector.Error as err:
            print(f"데이터베이스 연결 오류: {err}")
            retries -= 1
            time.sleep(3)  # 3초 대기 후 재시도
    
    # 최대 재시도 횟수를 초과한 경우
    print("데이터베이스 연결 실패: 최대 재시도 횟수 초과")
    return None

# 데이터베이스 초기화 함수
def init_db():
    connection = get_db_connection()
    if connection is None:
        print("데이터베이스 초기화 실패")
        return
    
    cursor = connection.cursor()
    
    # 테이블이 없으면 생성
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            completed BOOLEAN DEFAULT FALSE
        )
    ''')
    
    # 샘플 데이터 확인 후 없으면 추가
    cursor.execute('SELECT COUNT(*) FROM tasks')
    count = cursor.fetchone()[0]
    
    if count == 0:
        # 샘플 데이터 추가
        cursor.execute('INSERT INTO tasks (title, completed) VALUES (%s, %s)', ('도커 학습하기', False))
        cursor.execute('INSERT INTO tasks (title, completed) VALUES (%s, %s)', ('Flask 앱 만들기', True))
        cursor.execute('INSERT INTO tasks (title, completed) VALUES (%s, %s)', ('MySQL 연동하기', False))
    
    connection.commit()
    cursor.close()
    connection.close()

# 앱 시작 시 DB 초기화
@app.before_first_request
def before_first_request():
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "데이터베이스 연결 실패"}), 500
    
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    cursor.close()
    connection.close()
    
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        return jsonify({"error": "제목이 필요합니다"}), 400
    
    title = request.json['title']
    completed = request.json.get('completed', False)
    
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "데이터베이스 연결 실패"}), 500
    
    cursor = connection.cursor()
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (%s, %s)', (title, completed))
    connection.commit()
    
    new_id = cursor.lastrowid
    cursor.close()
    connection.close()
    
    return jsonify({
        'id': new_id,
        'title': title,
        'completed': completed
    }), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if not request.json:
        return jsonify({"error": "데이터가 필요합니다"}), 400
    
    title = request.json.get('title')
    completed = request.json.get('completed')
    
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "데이터베이스 연결 실패"}), 500
    
    cursor = connection.cursor()
    
    update_fields = []
    params = []
    
    if title is not None:
        update_fields.append("title = %s")
        params.append(title)
    
    if completed is not None:
        update_fields.append("completed = %s")
        params.append(completed)
    
    if not update_fields:
        cursor.close()
        connection.close()
        return jsonify({"error": "업데이트할 필드가 없습니다"}), 400
    
    params.append(task_id)
    cursor.execute(f'UPDATE tasks SET {", ".join(update_fields)} WHERE id = %s', params)
    connection.commit()
    
    # 업데이트된 작업 가져오기
    cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
    task = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if task:
        return jsonify({
            'id': task_id,
            'title': title if title is not None else task[1],
            'completed': completed if completed is not None else task[2]
        })
    else:
        return jsonify({"error": "작업을 찾을 수 없습니다"}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "데이터베이스 연결 실패"}), 500
    
    cursor = connection.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return jsonify({'result': True})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    # HTML 템플릿 디렉토리 생성
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # 간단한 HTML 템플릿 파일 생성
    with open('templates/index.html', 'w') as f:
        f.write('''
<!DOCTYPE html>
<html>
<head>
    <title>Flask + Docker + MySQL 데모</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        .task-list {
            margin-top: 20px;
        }
        .task {
            padding: 10px;
            border-bottom: 1px solid #ddd;
            display: flex;
            align-items: center;
        }
        .task.completed {
            background-color: #f8f8f8;
        }
        .task-checkbox {
            margin-right: 10px;
        }
        .task-title {
            flex-grow: 1;
        }
        .completed .task-title {
            text-decoration: line-through;
            color: #888;
        }
        .task-actions {
            margin-left: 10px;
        }
        .new-task {
            margin-top: 20px;
            display: flex;
        }
        .new-task input {
            flex-grow: 1;
            padding: 8px;
            margin-right: 10px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 8px 15px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .delete-btn {
            background-color: #f44336;
        }
        .delete-btn:hover {
            background-color: #d32f2f;
        }
    </style>
</head>
<body>
    <h1>할 일 관리 애플리케이션</h1>
    <p>Flask + Docker + MySQL 데모 애플리케이션입니다.</p>
    
    <div class="new-task">
        <input type="text" id="new-task-input" placeholder="새 할 일 입력...">
        <button onclick="addTask()">추가</button>
    </div>
    
    <div class="task-list" id="task-list">
        <!-- 태스크가 여기에 동적으로 로드됩니다 -->
    </div>

    <script>
        // 페이지 로드 시 할 일 목록 가져오기
        document.addEventListener('DOMContentLoaded', fetchTasks);

        // 할 일 목록 가져오기
        function fetchTasks() {
            fetch('/api/tasks')
                .then(response => response.json())
                .then(tasks => {
                    const taskList = document.getElementById('task-list');
                    taskList.innerHTML = '';
                    
                    tasks.forEach(task => {
                        const taskElement = document.createElement('div');
                        taskElement.className = `task ${task.completed ? 'completed' : ''}`;
                        taskElement.innerHTML = `
                            <input type="checkbox" class="task-checkbox" ${task.completed ? 'checked' : ''} 
                                   onchange="updateTask(${task.id}, {completed: this.checked})">
                            <span class="task-title">${task.title}</span>
                            <div class="task-actions">
                                <button class="delete-btn" onclick="deleteTask(${task.id})">삭제</button>
                            </div>
                        `;
                        taskList.appendChild(taskElement);
                    });
                })
                .catch(error => console.error('할 일 목록을 가져오는 중 오류 발생:', error));
        }

        // 새 할 일 추가
        function addTask() {
            const input = document.getElementById('new-task-input');
            const title = input.value.trim();
            
            if (!title) return;
            
            fetch('/api/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title: title, completed: false }),
            })
            .then(response => response.json())
            .then(data => {
                input.value = '';
                fetchTasks();
            })
            .catch(error => console.error('할 일 추가 중 오류 발생:', error));
        }

        // 할 일 업데이트
        function updateTask(id, data) {
            fetch(`/api/tasks/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => fetchTasks())
            .catch(error => console.error('할 일 업데이트 중 오류 발생:', error));
        }

        // 할 일 삭제
        function deleteTask(id) {
            fetch(`/api/tasks/${id}`, {
                method: 'DELETE',
            })
            .then(response => response.json())
            .then(data => fetchTasks())
            .catch(error => console.error('할 일 삭제 중 오류 발생:', error));
        }
    </script>
</body>
</html>
        ''')
    
    app.run(host='0.0.0.0', debug=True)
