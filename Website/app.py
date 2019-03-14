from flask import Flask, request, render_template, send_file
from PIL import Image
from io import BytesIO
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    if request.method == 'GET':
        description = request.args.get('description')
        model = request.args.get('model')
        print(f'Generate image for : {description} with {model}')
        pil_img = Image.new('RGB', (32,32), (0,255,255))
        return serve_pil_image(pil_img)
    

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


