from flask import Flask, render_template, send_file, request, abort
import qrcode
import io

app = Flask(__name__)

def generate_qr(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)  # Fix the parameter name
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    return img_io

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            return "URL parameter is missing", 400
        
        qr_image = generate_qr(url)
        return send_file(
            qr_image,
            mimetype='image/png',
            as_attachment=True,
            download_name='qrcode.png'  # Suggest a filename for download
        )
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
