from flask import Flask, send_file, request
from flask_restful import Resource, Api, reqparse
import plus_one
import Faces
from io import BytesIO
import json
import numpy as np
import base64
import NumpyEncoder as np_enc

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('image')

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/')

class Image(Resource):
    def get(self):
        return send_file('../lydia.JPG', mimetype='image/jpg')
api.add_resource(Image, '/image')

class EchoImage(Resource):
    def get(self):
        return send_file(BytesIO(request.files['image'].read()))
api.add_resource(EchoImage, '/echoimage')

class FaceDetect(Resource):
    def post(self):
        face = Faces.detect_face(request.get_json(force=True)['image'])
        return {'face': face}
api.add_resource(FaceDetect, '/facedetect')

class Plus1(Resource):
    def get(self, num):
        return {'plus_one': str(plus_one.plus_one(num))}
api.add_resource(Plus1, '/plusone/<string:num>')




if __name__ == '__main__':
    app.run(debug=True)

