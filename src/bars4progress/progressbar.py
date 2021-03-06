from math import ceil
from time import sleep
from threading import Thread

class ProgressBar:
	"""
	Represents the progress of the given values into an ascii-based animation.

	Args
	animated_bar : AnimatedBarBuilder
		Object that represents the animation.
	on_finish : function
		Function to execute when the process finishes.
	max_value : float
		Represents the max progress value, on_finish will be executed once the progress reaches this value. Recommended to leave default value (1.0)
	frame_interval : float
		Time between each frame of the animation.
	"""
	
	def __init__(self, animated_bar, on_finish, max_value=1.0, frame_interval=0.1):
		self.max_value = max_value
		self.current_value = 0
		self.on_finish = on_finish
		self.animated_bar = animated_bar
		self.animation_thread = Thread(target=self.__animation_loop)
		self.frame_interval = frame_interval

	def start(self, run_process):
		"""
		Starts the animation of the progress bar and runs another process.
		"""
		self.animation_thread.start()
		run_process()

	def display_progress(self, progress: float, formatting="Loading... {0}%"):
		"""Displays the progress of the given value.
		Args:
		progress : float
			A value between 0 and max_value (default 1).
		formatting : str
			Describe how you want the progress to be shown.
		"""
		self.current_value = progress
		self.animated_bar.set_progress(formatting.format(self.__progress()))

	def __animation_loop(self):
		"""
		Displays the animation untill the progress bar reaches its max value.
		"""
		while self.current_value < self.max_value:
			sleep(self.frame_interval)
			self.animated_bar.next_frame()
		self.on_finish()

	def __progress(self, multiplier=100) -> int:
		"""
		Returns the progress as an integer.
		
		Args:
		multiplier : int
			The value to multiply the progress by.
		"""
		return ceil(self.current_value/self.max_value * multiplier)