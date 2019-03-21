from flask import Flask, request, render_template, send_file
from PIL import Image
from io import BytesIO
from tester import Tester
import yaml
import random


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    if request.method == 'GET':
        description = request.args.get('description')
        model_type = request.args.get('model') # gan or wgan
        model_type = model_type if model_type in ['gan', 'wgan'] else 'gan'

        object_type = request.args.get('object') # birds or flowers
        object_type = object_type if object_type in ['birds', 'flowers'] else 'flowers'

        cls_option = request.args.get('cls') # true or false
        cls_option = False if cls_option == 'false' else True

        tester = Tester(
            type=model_type,
            dataset=object_type,
            cls_option=cls_option
            )
        pil_img = tester.predict(txt=[description]*2) # Problem of batchNorm if size 1
        return serve_pil_image(pil_img)
    
@app.route('/random-description', methods=['GET'])
def get_random_description():
    with open('config.yaml', 'r') as f:
	    config = yaml.load(f)
    object_type = request.args.get('object')
    random_descriptions_path = config[f'{object_type}_random_descriptions_path']       
    with open(random_descriptions_path) as f:
        lines = f.read().splitlines()
    return random.choice(lines)
    

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


