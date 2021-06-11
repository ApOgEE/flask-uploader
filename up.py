from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import uuid

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

# nak spoof jenis server supaya tak kena scan
SERVER_NAME = 'Fakap Server v0.1.0'

class wtfFlask(Flask):
    def process_response(self, response):
        response.headers['server'] = SERVER_NAME
        return(response)

#from OpenSSL import SSL
#context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
#context.use_privatekey_file('cert/app_cert.key')
#context.use_certificate_file('cert/app_cert.crt')

token_selamat = 'g33k_79ec7a8f62844688b64898bfb26c176a'

app = wtfFlask(__name__)

@app.route('/')
def home():
    app.logger.info('Ada request mai...')

    token = check_token_bakhang()

    if token and (token_selamat == token):
        app.logger.info('yeay!!... token sukses')
        return render_template('home.tpl')
    else:
        return render_template('go_meninggal.tpl'),404


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    token = check_token_bakhang()

    if token and (token_selamat == token):
        app.logger.info('yeay!!... token sukses')

        if request.method == 'POST':
            f = request.files['file']
            namafail = 'gotfile/' + uuid.uuid4().hex + '_' + secure_filename(f.filename)
            f.save(namafail)
            app.logger.info('Fail baru upload: {}'.format(namafail))
            return 'file uploaded successfully'
        else:
            return 'wazaaaap...', 404

    else:
        return render_template('go_meninggal.tpl'),404

@app.errorhandler(404)
def page_not_found(error):
    return render_template('go_meninggal.tpl'), 404
    
def check_token_bakhang():
    token = None
    if 'x-apogeek-tokens' in request.headers:
        token = request.headers['x-apogeek-tokens']
        app.logger.info('jumpa token: {}'.format(token))
    return token


if __name__ == '__main__':
   app.run(debug = True)
