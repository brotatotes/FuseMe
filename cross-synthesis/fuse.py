import numpy as np, librosa, scipy as sp
from scipy.fftpack import fft, ifft
from scipy.signal import hamming, boxcar


def fuse(modulator, carrier):
	"""
	Takes in modulator and carrier signals and returns a fused signal. 
	Typically, a modulator is a voice, and the carrier is any spectrally rich sound.

	- inpu
	modulator: np array
	carrier: np array

	- output -
	fusion: np array

	"""
	modulator_stft = librosa.core.stft(modulator)
	carrier_stft = librosa.core.stft(carrier)


def get_spectral_envelope(frame):
	frame = np.log(np.abs(frame))
	fs = len(frame)
	real_cepstrum = np.real(ifft(frame))
	nw = 20
	high_low_window = hamming(fs)[fs - nw:]
	low_high_window = hamming(fs)[:nw]
	wzp = np.concatenate((high_low_window, np.zeros(fs - (2 * nw)), low_high_window))
	wrcep = wzp * real_cepstrum
	rcepenv = fft(wrcep)
	rcepenvp = np.real(rcepenv)
	rcepenvp = rcepenvp - np.mean(rcepenvp)


	# Direct translation of code from textbook

	# fs = len(sample)
	# w = hamming(fs)
	# winspeech = w * sample
	# Nfft = 4*fs
	# sspec = fft(winspeech, Nfft)
	# dbsspecfull = 20*np.log(np.abs(sspec))
	# rcep = ifft(dbsspecfull)
	# rcep = np.real(rcep)
	# period = 41 # what is period ??
	# nspec = Nfft/2+1
	# nw = 2*period - 4
	# if nw % 2 == 0:
	# 	nw -= 1
	# w = boxcar(nw)
	# wzp = np.concatenate((w[(nw+1)/2:], np.zeros(Nfft - nw), w[:(nw+1)/2]))
	# wrcep = wzp * rcep
	# rcepenv = fft(wrcep)
	# rcepenvp = np.real(rcepenvp[:nspec])
	# rcepenvp -= np.mean(rcepenvp)

