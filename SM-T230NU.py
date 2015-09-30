## The Monkey Runner `EXAMPLE` for Kono app 
## This example is base on the SM-T230NU, which means that 
## the touch events may fail due to the different resolution of screen.

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time #
print "Start test sample"

def main():
	# Connects to the current device, and return a MonkeyDevice object
	device = MonkeyRunner.waitForConnection()

	# check the Kono app is install
	apk_path = device.shell('pm path com.kono.reader')
	if apk_path.startswith('package:'):
	    print "App already installed."
	else:
	    print "App not install yet."

	# Kono app's package name
	package = 'com.kono.reader'
	# Kono app's name of the start Activity
	main_activity = 'com.kono.reader.MainActivity'

	run_component = package + '/' + main_activity 

	print "Launching Kono"
	device.startActivity(component=run_component)

	# sending an event which simulate a click on the menu button

	# Click library button
	device.touch(85, 1252, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# Click feed button
	device.touch(250, 1252, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# Click konogram button
	device.touch(400, 1252, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# Click notification button
	device.touch(550, 1252, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# Click MyKono button
	device.touch(725, 1252, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	##device.drag((550,500),(100,1000), 0.5, 1)
	# Takes a screenshot
	now = time.strftime("%Y-%m-%d-%H-%M-%S")
	imageShot = device.takeSnapshot()
	# Writes the screenshot to a file
	imageShot.writeToFile("screenShot/"+now+".png", "png")

	print "End of script"

if __name__ == '__main__':
    main()
