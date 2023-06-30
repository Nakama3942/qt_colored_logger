"""
Copyright © 2023 Kalynovsky Valentin. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# todo разбить в пакет

class ColorException(BaseException):
	"""
	The exception that is thrown when there is no color in any palette.

	.. versionadded:: 0.0.0
	"""

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message

class ReCreationException(BaseException):
	"""
	The exception that is thrown when an object of the Singleton category is re-created.

	.. versionadded:: 0.0.0
	"""

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message

class EnvironmentException(BaseException):
	"""
	The exception that is thrown when on environmental errors.

	.. versionadded:: 0.0.0
	"""

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message

class InitException(BaseException):
	"""
	The exception thrown on errors during initialization.

	.. versionadded:: 0.0.0
	"""

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message

class MessageException(BaseException):
	"""
	The exception that is thrown when a write message is too short.

	.. versionadded:: 0.0.0
	"""

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message
