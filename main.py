from flask import Flask, request, jsonify
from flask_cors import CORS

#initialize flask app
app = Flask(__name__)

#allow cross-origin requests to recieve data from the extension
CORS(app)


@app.route('/update_data', methods=['POST'])
def update_data():
    #recieve posted data and print to screen
    data = request.json

    type_of_update = request.headers.get('Type')
    print(f"Type of update: {type_of_update}")
    if data:
        print(f"Recieved data: {data}")
        return jsonify({"message": "Data recieved successfully"}), 200
    else:
        return jsonify({"error": "No data recieved"}), 400

if __name__ == "__main__":
    app.run(debug=True)
