from pathlib import Path
import random

class MaterializeMood:

	
	def __init__(self):
		self._newMood = ''
		
	def makeMood(self):
		"""
		
		Write code to open a file and get a mood by random. Return the retrieved mood back to the caller.
		
		"""
		
		moodList = []
		moodroll = 0
		filePath = Path('moodbank.txt')
		if filePath.exists():
			with open('moodbank.txt') as moodFile:
				for currentMood in moodFile:
					moodList.append(currentMood)
			moodFile.close()
		else:
			self._newMood = '\n\n\n\nCannot open moodbank.txt file.'
		print("List contents\n")
		print(moodList)
		
		#self._newMood = "A test mood."
		
		moodroll = random.randint(0, len(moodList) - 1)
		#print(moodroll)
		self._newMood = "\n\n\n\n\n\n" + moodList[moodroll]
		
		return self._newMood
