import sys
from PIL import Image
from StringIO import StringIO
import requests
import urllib2
import base64
import json
import NumpyEncoder as np_enc
import cStringIO
from skimage import io

class FaceClient:
    def __init__(self, url):
        self.url = url

    def getBase64(self, filename):
        with open(filename, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string

    def request(self, endpoint, data):
        url = self.url + '/' + endpoint
        headers = {'Content-Type': 'application/json'}
        req = requests.post(url=url, data=json.dumps(data), headers=headers)
        return req.content

    def recognize(self, filename):
        base64Image = self.getBase64(filename)
        json_data = { "image" : base64Image }
        api_result = self.request("facedetect", json_data)
        face = json.loads(api_result)
        return base64.b64decode(face['face'])

f = sys.argv[1]
url = sys.argv[2]
client = FaceClient(url)
image = client.recognize(f)


with open('return.jpg', 'wb') as fd:
    fd.write(image)

