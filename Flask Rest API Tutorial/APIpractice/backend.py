from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"Sam": {"age":19, "gender": "male"},
        "Wil":{"age":70,"gender":"male"}}

class HelloWorld(Resource):
    def get(self, name):
       return names[name]
       
def post(self):
    return {"data": "Posted"}

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
    