import sys
import dlib
from skimage import io, util
import numpy as np
from PIL import Image
from io import BytesIO
from StringIO import StringIO
import cStringIO
import base64

detector = dlib.get_frontal_face_detector()

def read_image(b64_img):
    enc_data = base64.b64decode(b64_img)
    file_like = cStringIO.StringIO(enc_data)
    im = io.imread(file_like)
    return im


def write_image(img):
    s = StringIO()
    io.imsave(s, img)
    contents = s.getvalue()
    return base64.b64encode(contents)

def detect_face(data):
    img = read_image(data)
    dets, scores, idx = detector.run(img, 1)
    scores = list(scores)
    best = dets[scores.index(max(scores))]
    x,y,c = img.shape
    c_img = util.crop(img, ((best.top(), y - best.bottom()), (best.left(), x - best.right()), (0,0)))
    s = write_image(c_img)
    return s
