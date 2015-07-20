## The Monkey Runner `EXAMPLE` for Kono app 
## This example is base on the Nexus 6, which means that 
## the touch events may fail due to the different resolution of screen.

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

print "Start test sample"

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
device.touch(160, 2300, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# Click feed button
device.touch(450, 2300, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# Click konogram button
device.touch(710, 2300, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# Click notification button
device.touch(1000, 2300, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# Click MyKono button
device.touch(1270, 2300, "DOWN_AND_UP")
MonkeyRunner.sleep(2)

print "End of script"
