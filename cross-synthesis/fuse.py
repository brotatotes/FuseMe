import numpy as np, librosa, scipy as sp
from scipy.fftpack import fft, ifft
from scipy.signal import hamming, boxcar


def fuse(modulator, carrier):
	"""
	Takes in modulator and carrier signals and returns a fused signal. 
	Typically, a modulator is a voice, and the carrier is any spectrally rich sound.

	- input -
	modulator: np array
	carrier: np array

	- output -
	fusion: np array

	"""
	modulator_stft = librosa.core.stft(modulator)
	carrier_stft = librosa.core.stft(carrier)


def get_spectral_envelope(signal, sr):

