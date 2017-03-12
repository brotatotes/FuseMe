from flask import Flask, request, redirect, url_for
from flask import render_template
from werkzeug import secure_filename
import os, librosa, numpy as np, scipy as sp
from scipy.fftpack import fft, ifft
from scipy.signal import hamming, boxcar, hilbert

app = Flask(__name__)

def wavwrite(filepath, data, sr, norm=True, dtype='int16',):
    if norm:
        data /= np.max(np.abs(data))
    data = data * np.iinfo(dtype).max
    data = data.astype(dtype)
    sp.io.wavfile.write(filepath, sr, data)

def cross_synthesize(mod, car):
    # takes two 1D np arrays
    # mod - the modulator signal
    # car - the carrier signal
    #
    # returns cross synthesis of the two signals
    # 
    n_fft = 4096
    hop_length = 1024 
    
    smaller_length = min(len(mod), len(car))

    mod = mod[:smaller_length]
    car = car[:smaller_length]

    modstft = librosa.core.stft(mod, n_fft, hop_length)
    carstft = librosa.core.stft(car, n_fft, hop_length)

    car_env = hilbert(np.abs(carstft), axis=0)
    flat_car = carstft/(car_env+1e-20)
    mod_env = np.abs(hilbert(np.abs(modstft), axis=0))
    cross = flat_car * mod_env
    result = librosa.core.istft(cross, hop_length)

    return result

@app.route("/", methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		f = request.files['file']
		f.filename = 'uploaded.mp3'
		f.save(os.path.join('static', secure_filename(f.filename)))
		return '', 204
	else:
		return render_template('test.html')

@app.route("/file/<id>", methods=["POST"])
def file(id):
	if request.method == "POST":
		if id == '1':
			f = request.files['file']
			f.filename = 'carrier.wav'
			f.save(os.path.join('static', secure_filename(f.filename)))
			return '', 204
		else:
			f = request.files['file']
			f.filename = 'modulator.wav'
			f.save(os.path.join('static', secure_filename(f.filename)))
			return '', 204
	else:
		return render_template('test.html')

@app.route("/playback", methods=['GET', 'POST'])
def playback():
    if(os.path.isfile('./static/modulator.wav') == True and os.path.isfile('./static/carrier.wav') == True): 
        modulator, sr = librosa.load('./static/modulator.wav', 22500)
        carrier, sr = librosa.load('./static/carrier.wav', 22500)
        fusion = cross_synthesize(modulator, carrier)
        wavwrite((os.path.join('static', secure_filename('fusion.wav'))), fusion, 22500, norm=True, dtype='int16')
        return render_template('playback.html')
    else:
        return render_template('upload_error.html')

@app.route("/about", methods=['GET','POST'])
def about():
	return render_template('about.html')

if __name__ == "__main__":
    app.run()