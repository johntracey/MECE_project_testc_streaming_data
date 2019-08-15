01	from pynq import Overlay
02	import pynq.lib.dma
03
04	%matplotlib notebook
05	import matplotlib.pyplot as plt
06
07	def plot_to_notebook(time_sec,in_signal,n_samples,out_signal=None):
08		plt.figure()	
09		plt.subplot(1, 1, 1)
10		plt.xlabel('Time (usec)')
11		plt.grid()
12		plt.plot(time_sec[:n_samples]*1e6,in_signal[:n_samples],'y-',label='Input signal')
13		if out_signal is not None:
14			plt.plot(time_sec[:n_samples]*1e6,out_signal[:n_samples],'g-',linewidth=2,label='Module output')
15		plt.legend()
16		
17	overlay = Overlay('/home/xilinx/pynq/overlays/custom_streaming_function/custom_function.bit') 
18	print(overlay.ip_dict)
19	dma = overlay.simple_function.custom_dma
20
21
22	import numpy as np
23
24	# Total time
25	T = 0.02
26	# Sampling frequency
27	fs = 100e6
28	# Number of samples
29	n = int(T * fs)
30	# Time vector in seconds
31	t = np.linspace(0, T, n, endpoint=False)
32	# Samples of the signal
33	samples = 10000*np.sin(0.2e6*2*np.pi*t) + 1500*np.cos(46e6*2*np.pi*t) + 2000*np.sin(12e6*2*np.pi*t)
34	# Convert samples to 32-bit integers
35	samples = samples.astype(np.int32)
36	print('Number of samples: ',len(samples))
37
38	# Plot signal to the notebook
39	plot_to_notebook(t,samples,1000)