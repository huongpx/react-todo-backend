To run this project locally:
<br>
`cd /path/to/react-todo-backend`
<br>
`pip install -r requirements.txt`
<br>
`export FLASK_ENV=development`
<br>
`flask run`

To test the APIs, you need to signup with username, email and password and then login to get the JWT token.

**SIGNUP**
<br>

- api: http://localhost:5000/api/auth/signup
- JSON body data:
  <br> {"username": "your_username", "email": "your_email", "password": "your_password"}
- Expected response: {"message": "Registration successful with username \"your_username\""}

**LOGIN**
<br>

- api: http://localhost:5000/api/auth/login
- Authorization: Basic auth:
  <br> username: "your_username", password: "your_password"}
- Expected response: {"token": "session_login_token"}

**CALL API RESOURCE**
<br>

#### Get all todos

- api: GET http://localhost:5000/api/todos
- Add token to Request Header:
  <br> x-access-token: session_login_token
- Example response: [{ "id": 1, "title": "test 01", "completed": false }, { "id": 2, "title": "test 01", "completed": false }, ...]

#### Create a new todo

- api: POST http://localhost:5000/api/todos
- Add token to Request Header:
  <br> x-access-token: session_login_token
- JSON body data:
  <br> {"title": "todo title", "completed": true|false}
- Expected response: Create new Todo

#### Get todo with id

- api: GET http://localhost:5000/api/todos/todo_id
- Add token to Request Header:
  <br> x-access-token: session_login_token
- Example response: { "id": todo_id, "title": todo_title, "completed": true|false }

#### Update todo with id

- api: PUT http://localhost:5000/api/todos/todo_id
- Add token to Request Header:
  <br> x-access-token: session_login_token
- JSON body data:
  <br> {"title": "todo title", "completed": true|false}
- Expected response: Updated Todo

#### Delete todo with id

- api: DELETE http://localhost:5000/api/todos/todo_id
- Add token to Request Header:
  <br> x-access-token: session_login_token
- Expected response: Deleted Todo
