from flask import Flask, request, make_response, redirect

app = Flask(__name__)
users = {'admin': 'password'}  # Simple user database

@app.route('/')
def index():
    if 'username' in request.cookies:
        return f'Welcome: {request.cookies.get("username")}'
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if users.get(username) == password:
            resp = make_response(redirect('/'))
            resp.set_cookie('username', username)  # Set the cookie
            return resp
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="password" name="password">
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)  # Run the server in debug mode
