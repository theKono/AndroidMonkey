
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
print "Start test sample"
# Connects to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
# check the Kono app is install
apk_path = device.shell('pm path com.kono.reader')
# Kono app's package name
package = 'com.kono.reader'
print "htc 820 "


def fans():
	# Kono app's name of the start Activity
	main_activity = 'com.kono.reader.MainActivity'
	run_component = package + '/' + main_activity 
	device.startActivity(component=run_component)
	print "test fans"
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
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	device.press('KEYCODE_BACK','DOWN_AND_UP')
def follow():
    # Kono app's name of the start Activity
	main_activity = 'com.kono.reader.MainActivity'
	run_component = package + '/' + main_activity 
	device.startActivity(component=run_component)
	print "test follow" 
	MonkeyRunner.sleep(5)   
	# Click MyKono button
	device.touch(650, 1150, "DOWN_AND_UP")
	MonkeyRunner.sleep(1)
	# Open MyKono 	
	device.touch(300, 250, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# Open follow
	device.touch(440, 205, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	device.press('KEYCODE_BACK','DOWN_AND_UP')
		
def hello():
    # Kono app's name of the start Activity
	main_activity = 'com.kono.reader.MainActivity'
	run_component = package + '/' + main_activity 
	device.startActivity(component=run_component)
	print "test friends" 
	MonkeyRunner.sleep(5)
    # Click MyKono button
	device.touch(650, 1150, "DOWN_AND_UP")
	MonkeyRunner.sleep(1)
	# Open MyKono 	
	device.touch(300, 250, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	# Open follow
	device.touch(620, 212, "DOWN_AND_UP")
	MonkeyRunner.sleep(2)
	device.press('KEYCODE_BACK','DOWN_AND_UP')
	device.press('KEYCODE_BACK','DOWN_AND_UP')

fans()
# 截圖
result = device.takeSnapshot()
result.writeToFile('./fans.png','png')
follow()
# 截圖
result = device.takeSnapshot()
result.writeToFile('./follow.png','png')
hello()
# 截圖
result = device.takeSnapshot()
result.writeToFile('./hello.png','png')











