# This file must be run with sudo access, such as:
# sudo xfce4-terminal -x python /bin/dell-led-changer.py
from subprocess import call
run_line="dellLEDCtl "
zone_set=False
while zone_set==False:
	zone=int(raw_input("Please select zone:\n  1. Fans\n  2. Speakers\n  3. Lid\n>>> "))
	if zone==1:
		run_line=run_line+"-z1 "
		zone_set=True
	elif zone==2:
		run_line=run_line+"-z2 "
		zone_set=True
	elif zone==3:
		run_line=run_line+"-z3 "
		zone_set=True
	else:
		print("That was not one of your options. Please try again")
	print(run_line)
	color=int(raw_input("Please select a color:\n  0. Off\n  1. Ruby (red)\n  2. Citrine (light yellow-orange)\n  3. Amber (lime-green)\n  4. Peridot (greenish sky-blue)\n  5. Emerald (green)\n  6. Jade (teal)\n  7. Topaz (light blue)\n  8. Tanzanite (blue)\n  9. Aquamarine (light grey-blue)\n  10. Sapphire (Dell blue, same as power adapter)\n  11. Iolite (bluish purple)\n  12. Amethyst (light purple)\n  13. Kunzite (lighter purple)\n  14. Rhodolite (pink)\n  15. Coral (rose)\n  16. Diamond (white-blue)\n>>> "))
	color=str(color)
	run_line=run_line+color
	call(run_line, shell=True)
	zone_set=False
	run_line="dellLEDCtl "
	call("clear",shell=True)
