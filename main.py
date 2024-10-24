from flask import Flask, request, jsonify

app = Flask(__name__)



@app.route('/update_data', methods=['POST'])
def update_data():
    data = request.json
    if data:
        print(f"Recieved data: {data}")
        return jsonify({"message": "Data recieved successfully"}), 200
    else:
        return jsonify({"error": "No data recieved"}), 400

if __name__ == "__main__":
    app.run(debug=True)
