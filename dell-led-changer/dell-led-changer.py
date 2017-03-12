# This file must be run with sudo access, such as:
# sudo xfce4-terminal -x python /bin/dell-led-changer.py
from subprocess import call
def set_color(selected_zone):
	run_line_starter="dellLEDCtl "
	color=int(raw_input("Please select a color:\n  0. Off\n  1. Ruby (red)\n  2. Citrine (light yellow-orange)\n  3. Amber (lime-green)\n  4. Peridot (greenish sky-blue)\n  5. Emerald (green)\n  6. Jade (teal)\n  7. Topaz (light blue)\n  8. Tanzanite (blue)\n  9. Aquamarine (light grey-blue)\n  10. Sapphire (Dell blue, same as power adapter)\n  11. Iolite (bluish purple)\n  12. Amethyst (light purple)\n  13. Kunzite (lighter purple)\n  14. Rhodolite (pink)\n  15. Coral (rose)\n  16. Diamond (white-blue)\n>>> "))
	color=str(color)
	if selected_zone==0:
		run_line=run_line_starter+"-z1 "+color
		call(run_line,shell=True)
		run_line=run_line_starter+"-z2 "+color
		call(run_line,shell=True)
		run_line=run_line_starter+"-z3 "+color
		call(run_line,shell=True)
	elif selected_zone==1:
		run_line=run_line_starter+"-z1 "+color
		call(run_line,shell=True)
	elif selected_zone==2:
		run_line=run_line_starter+"-z2 "+color
		call(run_line,shell=True)
	elif selected_zone==3:
		run_line=run_line_starter+"-z3 "+color
		call(run_line,shell=True)
	else:
		print("That's not an option. Sorry.")
while True:
	zone=int(raw_input("Please select zone:\n  0. All\n  1. Fans\n  2. Speakers\n  3. Lid\n>>> "))
	set_color(zone)
