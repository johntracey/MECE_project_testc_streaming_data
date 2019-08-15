from pynq import Overlay
import pynq.lib.dma

%matplotlib notebook
import matplotlib.pyplot as plt

def plot_to_notebook(time_sec,in_signal,n_samples,out_signal=None):
	plt.figure()	
	plt.subplot(1, 1, 1)
	plt.xlabel('Time (usec)')
	plt.grid()
	plt.plot(time_sec[:n_samples]*1e6,in_signal[:n_samples],'y-',label='Input signal')
	if out_signal is not None:
		plt.plot(time_sec[:n_samples]*1e6,out_signal[:n_samples],'g-',linewidth=2,label='Module output')
		plt.legend()
		
overlay = Overlay('/home/xilinx/pynq/overlays/custom_streaming_function/custom_function.bit') 
#print(overlay.ip_dict)
dma = overlay.simple_function.custom_dma


import numpy as np

# Total time
T = 0.0000025
# Sampling frequency
fs = 100e6
# Number of samples: 0.01 * 100,000,000 = 1,000,000
n = int(T * fs)
# Time vector in seconds
t = np.linspace(0, T, n, endpoint=False)
# Samples of the signal
samples = 10000*np.sin(0.2e6*2*np.pi*t) + 1500*np.cos(46e6*2*np.pi*t) + 2000*np.sin(12e6*2*np.pi*t)
# Convert samples to 32-bit integers
samples = samples.astype(np.int32)
print('Number of samples: ',len(samples))

# Plot signal to the notebook
plot_to_notebook(t,samples,1000)