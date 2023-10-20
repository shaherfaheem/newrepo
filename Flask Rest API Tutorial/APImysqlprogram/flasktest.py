from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/my-first-api', methods=['POST'])
def hello():
    data = request.get_json()  # Retrieve JSON data from the request
    print(data)
    # Check if the 'name' key exists in the JSON data
    if 'name' in data:
        name = data['name']
        gender = data['gender']
        response = {'message': f'Hello, {name}, your gender is {gender} !', 'debuginfo': data}
    else:
        response = {'message': 'Hello!'}

    return jsonify(response)  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
