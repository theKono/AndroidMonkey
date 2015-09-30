from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

print "Start test sample"

# Connects to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection()

# check the Kono app is install
apk_path = device.shell('pm path com.kono.reader')

# Kono app's package name
package = 'com.kono.reader'
# Kono app's name of the start Activity
main_activity = 'com.kono.reader.MainActivity'

run_component = package + '/' + main_activity 


device.startActivity(component=run_component)
print "Kono succesed"
MonkeyRunner.sleep(5)
# Click MyKono button
device.touch(650, 1150, "DOWN_AND_UP")
MonkeyRunner.sleep(1)
# Open MyKono 
device.touch(300, 250, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# Open fans
device.touch(290, 205, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# Back
device.touch(45, 110, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# follow
device.touch(453, 223, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# Back
device.touch(45, 110, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# match friends
device.touch(650, 201, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# Back
device.touch(45, 110, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# edit
device.touch(443, 290, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
# edit name
device.touch(381, 541, "DOWN_AND_UP")
MonkeyRunner.sleep(2)

#delete

device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(2)
#input name
device.type("jiarou")
MonkeyRunner.sleep(1)
#space
device.touch(397, 1127, "DOWN_AND_UP")
MonkeyRunner.sleep(1)
#back
device.touch(664, 94, "DOWN_AND_UP")

print "End of script"




