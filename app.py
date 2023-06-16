from flask import Flask, jsonify, request, json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def main():
    response = {
        "greeting": "Hola Mundo desde Flask"
    }
    
    return jsonify(response), 200

@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
    
    if request.method == 'GET':
        return jsonify({ "request": f"You are using {request.method} method"}), 200
    
    if request.method == 'POST':
        return jsonify({ "request": f"You are using {request.method} method"}), 200
    
    if request.method == 'PUT':
        return jsonify({ "request": f"You are using {request.method} method"}), 200
    
    if request.method == 'DELETE':
        return jsonify({ "request": f"You are using {request.method} method"}), 200

@app.route('/send-data', methods=['POST', 'PUT'])
def send_data():
    
    if request.method == 'POST':
        """ 
        Convertir a String
        
        response = {
            "message": "Convirtiendo a String"
        }
        
        data = json.dumps(response) 
        
        """
        #data = json.loads(request.data)
        data = request.get_json()
        print(data["name"])
        
    if request.method == 'PUT':
        #data = json.loads(request.data)
        #data = request.get_json()
        lastname = request.json.get("lastname")
        #print(data["lastname"])
        print(lastname)
        
    return jsonify({ "ok": True }), 200

@app.route('/greeting/<name>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def greeting(name):
    return jsonify({ "greeting": f"Hola, {name}"})
        

if __name__ == '__main__':
    app.run()