import random as rng
import time
import subprocess

class item(object):
	type = 'null'
	time = 0
	answer = 0

	def __init__(self,time,type):
		if type == 0:
			self.type = "MEGA"
		else:
			self.type = "ARMOR"
		
		self.time = time
		self.answer = self.get_answer(self.time,self.type)

	def get_answer(self,time,type):
		if type == "MEGA":
			return (time + 35) % 60
		elif type == "ARMOR":
			return (time + 25) % 60



class quake_timer(object):
	"""docstring for quake_timer"""
	def __init__(self):
		super(quake_timer, self).__init__()
		

	def console_run(self):
		subprocess.call("clear")
		while(1):
			start_time = time.time()
			new_item = item(rng.randint(0,60),rng.randint(0,1))
			print str(new_item.type) 
			print "Time: " + str(new_item.time)
			input = raw_input()
			if input == str(new_item.answer):
				elapsed_time = time.time() - start_time
				print "Correct"
				print "Elapsed time:" + str("%.2f" % elapsed_time) + 's\n'
			elif input == "exit":
				
				break

			elif input == "help":
				print "type exit to exit the program"
			
			elif input.isdigit() == False:
				print "Invalid Input" + '\n'
			
			else:
				print "Incorrect answer"
				print "Answer is: " + str(new_item.answer) + '\n'

	def get_new_item(self):
		return item(rng.randint(0,60),rng.randint(0,1))
				




		

def main():
	timer = quake_timer()
	timer.console_run()



if __name__ == '__main__':
	main()


