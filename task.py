###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr2
#Good Luck

import random #library responsible for generatin random number
import time #library responsible for making program sleep for selected time

#I couldn't import msvcrt

class Plane:
	#value between -180 and 180. 0 is when wings are pararrell with the ground
	current_orientation = ""

	def __init__(self, start_orientation):
		self.current_orientation = start_orientation

	def print_cur_orientation(self, time_step):
		print("Plane orientation: " + str( self.current_orientation ) + " angles. In time step: " + str(time_step) )
	
	def tilt_correction(self):
		correction_value = random.randint(0, abs(round(self.current_orientation / 10)) )

		if ( self.current_orientation > 0):
			self.current_orientation -= correction_value
		elif ( self.current_orientation < 0): #don't need to do anything if equals 0\
			self.current_orientation += correction_value

	def turbulations(self):
		self.current_orientation += random.randint(-18, 18)

	def check_crash(self):
		if( abs(self.current_orientation) > 270 ):
			return 1
		else:
			return 0
			


if __name__ == "__main__":
	plane_simulation=Plane( random.randint(-180, 180) ) #make it gaussian!

	time_step = 0

	while (1):
		plane_simulation.print_cur_orientation( time_step )
		plane_simulation.tilt_correction()
		plane_simulation.turbulations()

		if (plane_simulation.check_crash()):
			break

		time_step += 1
		time.sleep(0.2)
		
