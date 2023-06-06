from flask import Flask, request, jsonify
from dotenv import load_dotenv

import os 
load_dotenv()
#print(f"0.0.0.0:{$PORT}")
print(f"{os.getenv('PORT')}")
saved_port = os.getenv('PORT')

app = Flask(__name__)

@app.route("/", methods = ['POST'])
def print_req():
    
    user_as_json = request.get_json(silent=True, force=True)
    print(user_as_json)
    data = {'data': user_as_json}
    return jsonify(data, 200)

#host='0.0.0.0'
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=saved_port)