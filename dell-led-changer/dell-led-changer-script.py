# This file must be run with sudo access, such as:
# sudo xfce4-terminal -x python /bin/dell-led-changer-script.py
from subprocess import call
from time import sleep
choices=open("./central-db.db")
print("Which program would you like to run?\n(If you would like to add a program to this list, edit central-db.db)\n")
ticker=0
options=[]
for line in choices:
	name=line.split(" = ",1)[0]
	options.append(line.split(" = ",1)[1])
	print(" %d. %s") % (ticker,name)
	ticker=ticker+1
selection=raw_input("\nYour choice >>> ")
try:
	int(selection)
except:
	print("That wasn't an option either. Now exiting...")
	exit()
selection=int(selection)
if selection>ticker:
	print("That wasn't an option. Now exiting...")
	exit()
program=open(options[selection].rstrip())
for line in program:
	line=line.rstrip()
	broken_line=line.split(",",4)
	if broken_line[0]=="repeat":
		exit()
	first_call="dellLEDCtl -z1 "+broken_line[0]
	second_call="dellLEDCtl -z2 "+broken_line[1]
	third_call="dellLEDCtl -z3 "+broken_line[2]
	fourth_call="dellLEDCtl -l "+broken_line[3]
	call(first_call,shell=True)
	call(second_call,shell=True)
	call(third_call,shell=True)
	call(fourth_call,shell=True)
	sleep(int(broken_line[4]))
	
	
