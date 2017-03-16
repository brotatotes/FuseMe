from flask import Flask, request, redirect, url_for, make_response
from flask import render_template
from werkzeug import secure_filename
import os, sys, librosa, numpy as np, scipy as sp
from scipy.fftpack import fft, ifft
from scipy.signal import hamming, boxcar, hilbert
import random
from fuse import *

app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['wav'])

def wavwrite(filepath, data, sr, norm=True, dtype='int16',):
	if norm:
		data /= np.max(np.abs(data))
	data = data * np.iinfo(dtype).max
	data = data.astype(dtype)
	sp.io.wavfile.write(filepath, sr, data)

def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def upload_file():
	resp = make_response(render_template('home.html'))
	if request.method == 'POST':
		f = request.files['file']
		f.filename = 'uploaded.mp3'
		f.save(os.path.join('static/audio', secure_filename(f.filename)))
		return '', 204
	else:
		resp.set_cookie('username', str(int(1000000000*random.random())))
		return resp


@app.route("/file/<id>", methods=["POST"])
def file(id):
	if request.method == "POST":
		username = request.cookies.get('username')
		f = request.files['file']
		f.filename = secure_filename(f.filename)
		if f and allowed_file(f.filename):
			if id == '1':
				f.filename = 'carrier_' + username + '.wav'
			else:
				f.filename = 'modulator_' + username + '.wav'
			f.save(os.path.join('static/audio', secure_filename(f.filename)))
		return '', 204
	else:
		return render_template('home.html')

@app.route("/playback", methods=['GET', 'POST'])
def playback():
	username = request.cookies.get('username')
	if(os.path.isfile('./static/audio/modulator_' + username + '.wav') == True and os.path.isfile('./static/audio/carrier_' + username + '.wav') == True):
		modulator, sr = librosa.load('./static/audio/modulator_' + username + '.wav', 22500)
		carrier, sr = librosa.load('./static/audio/carrier_' + username + '.wav', 22500)
		fusion = fuse(modulator, carrier)
		wavwrite((os.path.join('static/audio', secure_filename('fusion_' + username + '.wav'))), fusion, 22500, norm=True, dtype='int16')
		return render_template('playback.html')
	else:
		return render_template('upload_error.html')

@app.route("/reset", methods=['GET','POST'])
def reset():
	if request.method == "POST":
		username = request.cookies.get('username')
		mfile = './static/audio/modulator_' + username + '.wav'
		cfile = './static/audio/carrier_' + username + '.wav'
		ffile = './static/audio/fusion_' + username + '.wav'
		if os.path.exists(mfile):
			os.remove('./static/audio/modulator_' + username + '.wav')
		if os.path.exists(cfile):
			os.remove('./static/audio/carrier_' + username + '.wav')
		if os.path.exists(ffile):
			os.remove('./static/audio/fusion_' + username + '.wav')
	return render_template('home.html')

@app.route("/about", methods=['GET','POST'])
def about():
	return render_template('about.html')

if __name__ == '__main__':
	# app.debug = True
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
	app.run()
