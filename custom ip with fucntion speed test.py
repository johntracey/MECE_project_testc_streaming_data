01	from scipy.signal import lfilter
02
03	import time
04	start_time = time.time()
05	sw_fir_output = 5*samples+50000
06	stop_time = time.time()
07	sw_exec_time = stop_time - start_time
08	print('Software execution time: ',sw_exec_time)
09
10	# Plot the result to notebook
11	plot_to_notebook(t,samples,1000,out_signal=sw_fir_output)
12
13
14	from pynq import Xlnk
15	import numpy as np
16
17	# Allocate buffers for the input and output signals
18	xlnk = Xlnk()
19	in_buffer = xlnk.cma_array(shape=(n,), dtype=np.int32)
20	out_buffer = xlnk.cma_array(shape=(n,), dtype=np.int32)
21
22	# Copy the samples to the in_buffer
23	np.copyto(in_buffer,samples)
24
25	# Trigger the DMA transfer and wait for the result
26	import time	
27	start_time = time.time()
28	dma.sendchannel.transfer(in_buffer)
29	dma.recvchannel.transfer(out_buffer)
30	dma.sendchannel.wait()
31	dma.recvchannel.wait()
32	stop_time = time.time()
33	hw_exec_time = stop_time-start_time
34	print('Hardware execution time: ',hw_exec_time)
35	print('Hardware acceleration factor: ',sw_exec_time / hw_exec_time)
36	# Plot to the notebook
37	plot_to_notebook(t,samples,1000,out_signal=out_buffer)
38
39	# Free the buffers
40	in_buffer.close()
41	out_buffer.close()