from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def print_req():
    print(f"0.0.0.0:{$PORT}")
    user_as_json = request.get_json(silent=True, force=True)
    print(user_as_json)
    data = {'data': user_as_json}
    return jsonify(data, 200)


if __name__ == '__main__':
    app.run(debug=True)