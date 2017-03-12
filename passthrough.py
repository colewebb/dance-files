from subprocess import call
call("pactl load-module module-loopback latency_msec=1",shell=True)
ticker=0
while True:
	stuff=raw_input("passthrough >>> ")
	if ticker%2==0:
		call("pactl unload-module module-loopback", shell=True)
		ticker=ticker+1
		print("Passthrough OFF")
		pass
	elif ticker%2==1:
		call("pactl load-module module-loopback latency_msec=1",shell=True)
		ticker=ticker+1
		print("Passthrough ON")
		pass
	else:
		pass
