from abc import ABC, abstractmethod

class TextBufferType(ABC):
	def __init__(self):
		self._text_buffer: list[str] = []

	def __lshift__(self, other) -> None:
		"""
		Used to add a string to the end of the buffer.

		:param other: The line to be added
		"""
		self.append(f"{other}")

	def __rshift__(self, other) -> None:
		"""
		Used to save a buffer to the file.

		:param other: The name of the file where you want to save the buffer
		"""
		self.save(other)

	def get_data(self) -> list:
		"""
		Returns a list of strings from a text buffer.

		:return: a list of text buffer lines
		"""
		return self._text_buffer

	@abstractmethod
	def append(self, message: str) -> None:
		"""
		Adds a string to the end of the text buffer.

		:param message: The string to be added to the buffer
		"""
		raise NotImplementedError("Method append() is not implemented in the base class.")

	@abstractmethod
	def insert(self, number_string: int, message: str) -> None:
		"""
		Adds a string to the middle of the text buffer at the specified position.

		:param number_string: Position (number) of the line to which you need to add a string
		:param message: The string to be placed on the position
		"""
		raise NotImplementedError("Method insert() is not implemented in the base class.")

	@abstractmethod
	def replace(self, number_string: int, message: str) -> None:
		"""
		Replaces a specific string in a text buffer. If there is no such string, the method
		fills the list with empty strings up to the required position and *adds* the string.

		:param number_string: Position (number) of the string to be replaced (added)
		:param message: A string that will replace the previous one by position
		"""
		raise NotImplementedError("Method replace() is not implemented in the base class.")

	@abstractmethod
	def save(self, name_file: str = "buffer") -> None:
		"""
		Saves the text of the buffer to a file.

		:param name_file: The name of the file where the buffer will be saved
		"""
		raise NotImplementedError("Method save() is not implemented in the base class.")

	@abstractmethod
	def update_console(self) -> None:
		"""
		Refreshes the console, erasing output text and outputting an updated buffer.
		"""
		raise NotImplementedError("Method update_console() is not implemented in the base class.")
