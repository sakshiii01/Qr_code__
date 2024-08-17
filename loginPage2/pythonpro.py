from flask import Flask, render_template, send_file
import qrcode
import io

app = Flask(__name__)

def generate_qr(url):
    qr=qrcode.QRCode(version=1, box_size=10, borders=5)
    qr=add_data(url)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black" , back_color="white")
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        URL = request.form['url']
        qr_image = generate_qr(url)
        return send_file(qr_image,mimetype='image/png')
    return render_template('index.html')

if __name__=="__main__":
    app.run()