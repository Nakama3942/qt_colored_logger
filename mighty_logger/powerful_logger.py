"""
A module with the implementation of a powerful logger.
\n
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

from mighty_logger.basic.basic_logger import BasicLogger
from mighty_logger.basic.exceptions import ColorException, CombinationException
from mighty_logger.basic.text_buffer_type import TextBufferType
from mighty_logger.src.color_picker import AnsiColor, HexColor, Dec2Ansi, Dec2Hex
from mighty_logger.src.log_environment import LogEnvironments
from mighty_logger.text.text_buffer import BasicTextBuffer, TextBuffer

class Logger(BasicLogger):
	"""
	The Logger class is a class that implements the functionality
	of logging the work of software in different directions.\n
	It has a color output of information, settings for the operation of the log.
	Only one class object can be created!!!\n
	Implements the output of the following information:\n
	1) Record creation time;
	2) Record status;
	3) Recording status message;
	4) Record type;
	5) Write message.
	\nImplements the output of the following types of records:\n
	1)  `DEBUG`
	2)  `DEBUG_PERFORMANCE`
	3)  `PERFORMANCE`
	4)  `EVENT`
	5)  `AUDIT`
	6)  `METRICS`
	7)  `USER`
	8)  `MESSAGE`
	9)  `INFO`
	10) `NOTICE`
	11) `WARNING`
	12) `ERROR`
	13) `CRITICAL`
	14) `PROGRESS`
	15) `SUCCESS`
	16) `FAIL`
	"""

	def __init__(
			self,
			*,
			program_name: str = "Unknown",
			log_environment: str = LogEnvironments.CONSOLE,
			console_width: int = 60,
			global_background: bool = False,
			time: bool = True,
			status: bool = True,
			status_message: bool = True,
			status_type: bool = True,
			message: bool = True
	):
		super().__init__(program_name, time, status, status_message, status_type, message)
		self._ColorScheme: dict = {}
		if log_environment == LogEnvironments.CONSOLE:
			self._buffer = TextBuffer(console_width)
		else:
			self._buffer = BasicTextBuffer()
		self._environment = log_environment
		self.global_background = global_background
		self._color_scheme_init()
		self._initial_log()

	def _color_scheme_init(self):
		"""
		Sets the colors of the logger.
		"""
		match self._environment:
			case LogEnvironments.CONSOLE:
				self._ColorScheme['INITIAL_COLOR'] = [AnsiColor('GOLD', "foreground"), AnsiColor('INDIGO', "foreground")]
				self._ColorScheme['INITIAL_BACKGROUND'] = ["", AnsiColor('GOLD', "background")]
				# DEBUG colors
				self._ColorScheme['DEBUG_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['DEBUG_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['DEBUG_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_DEBUG'] = [AnsiColor('BURLYWOOD', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['DEBUG_MESSAGE'] = [AnsiColor('TAN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['DEBUG_BACKGROUND'] = ["", AnsiColor('TAN', "background")]
				# DEBUG_PERFORMANCE colors
				self._ColorScheme['DEBUG_PERFORMANCE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_DEBUG_PERFORMANCE'] = [AnsiColor('NAVAJOWHITE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['DEBUG_PERFORMANCE_MESSAGE'] = [AnsiColor('WHEAT', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['DEBUG_PERFORMANCE_BACKGROUND'] = ["", AnsiColor('WHEAT', "background")]
				# PERFORMANCE colors
				self._ColorScheme['PERFORMANCE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['PERFORMANCE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['PERFORMANCE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_PERFORMANCE'] = [AnsiColor('BLANCHEDALMOND', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['PERFORMANCE_MESSAGE'] = [AnsiColor('BISQUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['PERFORMANCE_BACKGROUND'] = ["", AnsiColor('BISQUE', "background")]
				# EVENT colors
				self._ColorScheme['EVENT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['EVENT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['EVENT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_EVENT'] = [AnsiColor('GREENYELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['EVENT_MESSAGE'] = [AnsiColor('YELLOWGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['EVENT_BACKGROUND'] = ["", AnsiColor('YELLOWGREEN', "background")]
				# AUDIT colors
				self._ColorScheme['AUDIT_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['AUDIT_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['AUDIT_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_AUDIT'] = [AnsiColor('MEDIUMSPRINGGREEN', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['AUDIT_MESSAGE'] = [AnsiColor('SPRINGGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['AUDIT_BACKGROUND'] = ["", AnsiColor('SPRINGGREEN', "background")]
				# METRICS colors
				self._ColorScheme['METRICS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['METRICS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['METRICS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_METRICS'] = [AnsiColor('PALEGREEN', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['METRICS_MESSAGE'] = [AnsiColor('LIGHTGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['METRICS_BACKGROUND'] = ["", AnsiColor('LIGHTGREEN', "background")]
				# USER colors
				self._ColorScheme['USER_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['USER_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['USER_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_USER'] = [AnsiColor('CHARTREUSE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['USER_MESSAGE'] = [AnsiColor('LAWNGREEN', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['USER_BACKGROUND'] = ["", AnsiColor('LAWNGREEN', "background")]
				# MESSAGE colors
				self._ColorScheme['MESSAGE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['MESSAGE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['MESSAGE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_MESSAGE'] = [AnsiColor('PALETURQUOISE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['MESSAGE_MESSAGE'] = [AnsiColor('POWDERBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['MESSAGE_BACKGROUND'] = ["", AnsiColor('POWDERBLUE', "background")]
				# INFO colors
				self._ColorScheme['INFO_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['INFO_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['INFO_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_INFO'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['INFO_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['INFO_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
				# NOTICE colors
				self._ColorScheme['NOTICE_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['NOTICE_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['NOTICE_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_NOTICE'] = [AnsiColor('LIGHTBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['NOTICE_MESSAGE'] = [AnsiColor('LIGHTSTEELBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['NOTICE_BACKGROUND'] = ["", AnsiColor('LIGHTSTEELBLUE', "background")]
				# WARNING colors
				self._ColorScheme['WARNING_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('DARKMAGENTA', "foreground")]
				self._ColorScheme['WARNING_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['WARNING_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_WARNING'] = [AnsiColor('YELLOW', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['WARNING_MESSAGE'] = [AnsiColor('DARKYELLOW', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['WARNING_BACKGROUND'] = ["", AnsiColor('DARKYELLOW', "background")]
				# ERROR colors
				self._ColorScheme['ERROR_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")]
				self._ColorScheme['ERROR_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
				self._ColorScheme['ERROR_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
				self._ColorScheme['TYPE_ERROR'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('GAINSBORO', "foreground")]
				self._ColorScheme['ERROR_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTGRAY', "foreground")]
				self._ColorScheme['ERROR_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]
				# CRITICAL colors
				self._ColorScheme['CRITICAL_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PLUM', "foreground")]
				self._ColorScheme['CRITICAL_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
				self._ColorScheme['CRITICAL_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
				self._ColorScheme['TYPE_CRITICAL'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('DARKSALMON', "foreground")]
				self._ColorScheme['CRITICAL_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('LIGHTSALMON', "foreground")]
				self._ColorScheme['CRITICAL_BACKGROUND'] = ["", AnsiColor('MAROON', "background")]
				# PROGRESS colors
				self._ColorScheme['PROGRESS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('PURPLE', "foreground")]
				self._ColorScheme['PROGRESS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('DARKRED', "foreground")]
				self._ColorScheme['PROGRESS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('MAROON', "foreground")]
				self._ColorScheme['TYPE_PROGRESS'] = [AnsiColor('LIGHTSKYBLUE', "foreground"), AnsiColor('NAVY', "foreground")]
				self._ColorScheme['PROGRESS_MESSAGE'] = [AnsiColor('SKYBLUE', "foreground"), AnsiColor('MIDNIGHTBLUE', "foreground")]
				self._ColorScheme['PROGRESS_BACKGROUND'] = ["", AnsiColor('SKYBLUE', "background")]
				# SUCCESS colors
				self._ColorScheme['SUCCESS_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['SUCCESS_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('CHARTREUSE', "foreground")]
				self._ColorScheme['SUCCESS_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('LAWNGREEN', "foreground")]
				self._ColorScheme['TYPE_SUCCESS'] = [AnsiColor('GREEN', "foreground"), AnsiColor('PALEGREEN', "foreground")]
				self._ColorScheme['SUCCESS_MESSAGE'] = [AnsiColor('DARKGREEN', "foreground"), AnsiColor('LIGHTGREEN', "foreground")]
				self._ColorScheme['SUCCESS_BACKGROUND'] = ["", AnsiColor('DARKGREEN', "background")]
				# FAIL colors
				self._ColorScheme['FAIL_TIME'] = [AnsiColor('ORCHID', "foreground"), AnsiColor('LAVENDERBLUSH', "foreground")]
				self._ColorScheme['FAIL_STATUS'] = [AnsiColor('ORANGE', "foreground"), AnsiColor('ORANGE', "foreground")]
				self._ColorScheme['FAIL_STATUS_MESSAGE'] = [AnsiColor('DARKORANGE', "foreground"), AnsiColor('DARKORANGE', "foreground")]
				self._ColorScheme['TYPE_FAIL'] = [AnsiColor('FIREBRICK', "foreground"), AnsiColor('YELLOW', "foreground")]
				self._ColorScheme['FAIL_MESSAGE'] = [AnsiColor('DARKRED', "foreground"), AnsiColor('DARKYELLOW', "foreground")]
				self._ColorScheme['FAIL_BACKGROUND'] = ["", AnsiColor('DARKRED', "background")]
			case LogEnvironments.HTML:
				self._ColorScheme['INITIAL_COLOR'] = [HexColor('GOLD'), HexColor('INDIGO')]
				self._ColorScheme['INITIAL_BACKGROUND'] = ["", HexColor('GOLD')]
				# DEBUG colors
				self._ColorScheme['DEBUG_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['DEBUG_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['DEBUG_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_DEBUG'] = [HexColor('BURLYWOOD'), HexColor('NAVY')]
				self._ColorScheme['DEBUG_MESSAGE'] = [HexColor('TAN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['DEBUG_BACKGROUND'] = ["", HexColor('TAN')]
				# DEBUG_PERFORMANCE colors
				self._ColorScheme['DEBUG_PERFORMANCE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_DEBUG_PERFORMANCE'] = [HexColor('NAVAJOWHITE'), HexColor('NAVY')]
				self._ColorScheme['DEBUG_PERFORMANCE_MESSAGE'] = [HexColor('WHEAT'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['DEBUG_PERFORMANCE_BACKGROUND'] = ["", HexColor('WHEAT')]
				# PERFORMANCE colors
				self._ColorScheme['PERFORMANCE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['PERFORMANCE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['PERFORMANCE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_PERFORMANCE'] = [HexColor('BLANCHEDALMOND'), HexColor('NAVY')]
				self._ColorScheme['PERFORMANCE_MESSAGE'] = [HexColor('BISQUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['PERFORMANCE_BACKGROUND'] = ["", HexColor('BISQUE')]
				# EVENT colors
				self._ColorScheme['EVENT_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['EVENT_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['EVENT_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_EVENT'] = [HexColor('GREENYELLOW'), HexColor('NAVY')]
				self._ColorScheme['EVENT_MESSAGE'] = [HexColor('YELLOWGREEN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['EVENT_BACKGROUND'] = ["", HexColor('YELLOWGREEN')]
				# AUDIT colors
				self._ColorScheme['AUDIT_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['AUDIT_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['AUDIT_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_AUDIT'] = [HexColor('MEDIUMSPRINGGREEN'), HexColor('NAVY')]
				self._ColorScheme['AUDIT_MESSAGE'] = [HexColor('SPRINGGREEN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['AUDIT_BACKGROUND'] = ["", HexColor('SPRINGGREEN')]
				# METRICS colors
				self._ColorScheme['METRICS_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['METRICS_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['METRICS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_METRICS'] = [HexColor('PALEGREEN'), HexColor('NAVY')]
				self._ColorScheme['METRICS_MESSAGE'] = [HexColor('LIGHTGREEN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['METRICS_BACKGROUND'] = ["", HexColor('LIGHTGREEN')]
				# USER colors
				self._ColorScheme['USER_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['USER_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['USER_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_USER'] = [HexColor('CHARTREUSE'), HexColor('NAVY')]
				self._ColorScheme['USER_MESSAGE'] = [HexColor('LAWNGREEN'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['USER_BACKGROUND'] = ["", HexColor('LAWNGREEN')]
				# MESSAGE colors
				self._ColorScheme['MESSAGE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['MESSAGE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['MESSAGE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_MESSAGE'] = [HexColor('PALETURQUOISE'), HexColor('NAVY')]
				self._ColorScheme['MESSAGE_MESSAGE'] = [HexColor('POWDERBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['MESSAGE_BACKGROUND'] = ["", HexColor('POWDERBLUE')]
				# INFO colors
				self._ColorScheme['INFO_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['INFO_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['INFO_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_INFO'] = [HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
				self._ColorScheme['INFO_MESSAGE'] = [HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['INFO_BACKGROUND'] = ["", HexColor('SKYBLUE')]
				# NOTICE colors
				self._ColorScheme['NOTICE_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['NOTICE_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['NOTICE_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_NOTICE'] = [HexColor('LIGHTBLUE'), HexColor('NAVY')]
				self._ColorScheme['NOTICE_MESSAGE'] = [HexColor('LIGHTSTEELBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['NOTICE_BACKGROUND'] = ["", HexColor('LIGHTSTEELBLUE')]
				# WARNING colors
				self._ColorScheme['WARNING_TIME'] = [HexColor('ORCHID'), HexColor('DARKMAGENTA')]
				self._ColorScheme['WARNING_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['WARNING_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_WARNING'] = [HexColor('YELLOW'), HexColor('NAVY')]
				self._ColorScheme['WARNING_MESSAGE'] = [HexColor('DARKYELLOW'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['WARNING_BACKGROUND'] = ["", HexColor('DARKYELLOW')]
				# ERROR colors
				self._ColorScheme['ERROR_TIME'] = [HexColor('ORCHID'), HexColor('PLUM')]
				self._ColorScheme['ERROR_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
				self._ColorScheme['ERROR_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
				self._ColorScheme['TYPE_ERROR'] = [HexColor('FIREBRICK'), HexColor('GAINSBORO')]
				self._ColorScheme['ERROR_MESSAGE'] = [HexColor('DARKRED'), HexColor('LIGHTGRAY')]
				self._ColorScheme['ERROR_BACKGROUND'] = ["", HexColor('DARKRED')]
				# CRITICAL colors
				self._ColorScheme['CRITICAL_TIME'] = [HexColor('ORCHID'), HexColor('PLUM')]
				self._ColorScheme['CRITICAL_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
				self._ColorScheme['CRITICAL_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
				self._ColorScheme['TYPE_CRITICAL'] = [HexColor('FIREBRICK'), HexColor('DARKSALMON')]
				self._ColorScheme['CRITICAL_MESSAGE'] = [HexColor('DARKRED'), HexColor('LIGHTSALMON')]
				self._ColorScheme['CRITICAL_BACKGROUND'] = ["", HexColor('MAROON')]
				# PROGRESS colors
				self._ColorScheme['PROGRESS_TIME'] = [HexColor('ORCHID'), HexColor('PURPLE')]
				self._ColorScheme['PROGRESS_STATUS'] = [HexColor('ORANGE'), HexColor('DARKRED')]
				self._ColorScheme['PROGRESS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('MAROON')]
				self._ColorScheme['TYPE_PROGRESS'] = [HexColor('LIGHTSKYBLUE'), HexColor('NAVY')]
				self._ColorScheme['PROGRESS_MESSAGE'] = [HexColor('SKYBLUE'), HexColor('MIDNIGHTBLUE')]
				self._ColorScheme['PROGRESS_BACKGROUND'] = ["", HexColor('SKYBLUE')]
				# SUCCESS colors
				self._ColorScheme['SUCCESS_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['SUCCESS_STATUS'] = [HexColor('ORANGE'), HexColor('CHARTREUSE')]
				self._ColorScheme['SUCCESS_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('LAWNGREEN')]
				self._ColorScheme['TYPE_SUCCESS'] = [HexColor('GREEN'), HexColor('PALEGREEN')]
				self._ColorScheme['SUCCESS_MESSAGE'] = [HexColor('DARKGREEN'), HexColor('LIGHTGREEN')]
				self._ColorScheme['SUCCESS_BACKGROUND'] = ["", HexColor('DARKGREEN')]
				# FAIL colors
				self._ColorScheme['FAIL_TIME'] = [HexColor('ORCHID'), HexColor('LAVENDERBLUSH')]
				self._ColorScheme['FAIL_STATUS'] = [HexColor('ORANGE'), HexColor('ORANGE')]
				self._ColorScheme['FAIL_STATUS_MESSAGE'] = [HexColor('DARKORANGE'), HexColor('DARKORANGE')]
				self._ColorScheme['TYPE_FAIL'] = [HexColor('FIREBRICK'), HexColor('YELLOW')]
				self._ColorScheme['FAIL_MESSAGE'] = [HexColor('DARKRED'), HexColor('DARKYELLOW')]
				self._ColorScheme['FAIL_BACKGROUND'] = ["", HexColor('DARKRED')]

	def _initial_log(self):
		"""
		Displays initialized information.
		"""
		if self._environment == LogEnvironments.HTML:
			self._buffer << "<body style='background-color: #000000; color: #ffffff;'>"
		self._buffer << self._initialized_data(
			[
				self._ColorScheme['INITIAL_COLOR'][self.global_background],
				self._ColorScheme['INITIAL_BACKGROUND'][self.global_background]
			], self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def set_color(self, *, logger_color_name: str, color_value: list[int, int, int], foreground: bool = True, background: bool = False):
		"""
		A method that sets the ANSI escape code color code in the color table of the logger.
		May throw a ColorException if the given color is not in the table.
		The logger color table stores the following keys: see README.md/Data/"Logger Color Chart".\n
		Boolean flags: If foreground is set to True, then the color of the foreground text will change
		with/without a background (it all depends on the background flag). If in this case background
		is set to False (the standard combination of arguments) - then the color of the specifically
		front text that is displayed without a background changes, otherwise it changes the color
		of the specifically front text that is displayed with a background. If the foreground is set
		to False with background set to True, the background itself will change. The last combination,
		when both arguments are False, is an impossible combination that throws a CombinationException.

		:param logger_color_name: Color name in logger color table
		:param color_value: Color value in RGB
		:param foreground: Change foreground text color with/without background?
		:param background: Change background color?
		"""
		if logger_color_name in self._ColorScheme:
			if background and not foreground:
				self._ColorScheme[logger_color_name][1] = Dec2Ansi(color_value, "background") if self._environment == LogEnvironments.CONSOLE else Dec2Hex(color_value)
			elif background and foreground:
				self._ColorScheme[logger_color_name][1] = Dec2Ansi(color_value, "foreground") if self._environment == LogEnvironments.CONSOLE else Dec2Hex(color_value)
			elif not background and foreground:
				self._ColorScheme[logger_color_name][0] = Dec2Ansi(color_value, "foreground") if self._environment == LogEnvironments.CONSOLE else Dec2Hex(color_value)
			else:
				raise CombinationException("False-False combination of foreground-background flags not possible")
		else:
			raise ColorException("This color is not in the dictionary")

	def get_buffer(self) -> TextBufferType:
		"""
		Usually, before creating a logger, you need to create a text buffer
		and pass it to the constructor. But if this has not been done, the buffer
		is created directly in the logger. And to get it (for example, to save
		the buffer to a file), this method was implemented. It returns a buffer.

		:return: a text buffer object
		"""
		return self._buffer

	def DEBUG(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Debugging information logging:
		Can be used to log entry any information while debugging an application.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['DEBUG_TIME'][background],
				self._ColorScheme['DEBUG_STATUS'][background],
				self._ColorScheme['DEBUG_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_DEBUG'][background],
				self._ColorScheme['DEBUG_MESSAGE'][background],
				self._ColorScheme['DEBUG_BACKGROUND'][background],
			], status_message_text, "%DEBUG", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def DEBUG_PERFORMANCE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Performance debugging information logging:
		Can be used to log entry the execution time of operations or other
		performance information while the application is being debugged.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['DEBUG_PERFORMANCE_TIME'][background],
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS'][background],
				self._ColorScheme['DEBUG_PERFORMANCE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_DEBUG_PERFORMANCE'][background],
				self._ColorScheme['DEBUG_PERFORMANCE_MESSAGE'][background],
				self._ColorScheme['DEBUG_PERFORMANCE_BACKGROUND'][background],
			], status_message_text, "%DEBUG PERFORMANCE", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def PERFORMANCE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Performance information logging:
		Can be used to log entry the execution time of operations or
		other application performance information.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['PERFORMANCE_TIME'][background],
				self._ColorScheme['PERFORMANCE_STATUS'][background],
				self._ColorScheme['PERFORMANCE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_PERFORMANCE'][background],
				self._ColorScheme['PERFORMANCE_MESSAGE'][background],
				self._ColorScheme['PERFORMANCE_BACKGROUND'][background],
			], status_message_text, "%PERFORMANCE", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def EVENT(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Event information logging:
		Can be used to log entry specific events in the application,
		such as button presses or mouse cursor movements.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['EVENT_TIME'][background],
				self._ColorScheme['EVENT_STATUS'][background],
				self._ColorScheme['EVENT_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_EVENT'][background],
				self._ColorScheme['EVENT_MESSAGE'][background],
				self._ColorScheme['EVENT_BACKGROUND'][background],
			], status_message_text, "~EVENT", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def AUDIT(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Audit information logging:
		Can be used to log entry changes in the system, such as creating or
		deleting users, as well as changes in security settings.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['AUDIT_TIME'][background],
				self._ColorScheme['AUDIT_STATUS'][background],
				self._ColorScheme['AUDIT_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_AUDIT'][background],
				self._ColorScheme['AUDIT_MESSAGE'][background],
				self._ColorScheme['AUDIT_BACKGROUND'][background],
			], status_message_text, "~AUDIT", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def METRICS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Metrics information logging:
		Can be used to log entry metrics to track application performance and identify issues.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['METRICS_TIME'][background],
				self._ColorScheme['METRICS_STATUS'][background],
				self._ColorScheme['METRICS_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_METRICS'][background],
				self._ColorScheme['METRICS_MESSAGE'][background],
				self._ColorScheme['METRICS_BACKGROUND'][background],
			], status_message_text, "~METRICS", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def USER(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		User information logging:
		Can be used to log entry custom logs to store additional information
		that may be useful for diagnosing problems.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['USER_TIME'][background],
				self._ColorScheme['USER_STATUS'][background],
				self._ColorScheme['USER_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_USER'][background],
				self._ColorScheme['USER_MESSAGE'][background],
				self._ColorScheme['USER_BACKGROUND'][background],
			], status_message_text, "~USER", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def MESSAGE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Message information logging:
		Can be used for the usual output of ordinary messages about the program's operation.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['MESSAGE_TIME'][background],
				self._ColorScheme['MESSAGE_STATUS'][background],
				self._ColorScheme['MESSAGE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_MESSAGE'][background],
				self._ColorScheme['MESSAGE_MESSAGE'][background],
				self._ColorScheme['MESSAGE_BACKGROUND'][background],
			], status_message_text, "@MESSAGE", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def INFO(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Default information logging:
		Can be used to log entry messages with specific content about the operation of the program.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['INFO_TIME'][background],
				self._ColorScheme['INFO_STATUS'][background],
				self._ColorScheme['INFO_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_INFO'][background],
				self._ColorScheme['INFO_MESSAGE'][background],
				self._ColorScheme['INFO_BACKGROUND'][background],
			], status_message_text, "@INFO", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def NOTICE(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = None):
		"""
		Notice information logging:
		Can be used to flag important events that might be missed with a normal logging level.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		background = local_background if local_background is not None else self.global_background
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['NOTICE_TIME'][background],
				self._ColorScheme['NOTICE_STATUS'][background],
				self._ColorScheme['NOTICE_STATUS_MESSAGE'][background],
				self._ColorScheme['TYPE_NOTICE'][background],
				self._ColorScheme['NOTICE_MESSAGE'][background],
				self._ColorScheme['NOTICE_BACKGROUND'][background],
			], status_message_text, "@NOTICE", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def WARNING(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Warning information logging:
		Can be used to log entry warnings that the program may work with unpredictable results.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['WARNING_TIME'][local_background],
				self._ColorScheme['WARNING_STATUS'][local_background],
				self._ColorScheme['WARNING_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_WARNING'][local_background],
				self._ColorScheme['WARNING_MESSAGE'][local_background],
				self._ColorScheme['WARNING_BACKGROUND'][local_background],
			], status_message_text, "!WARNING", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def ERROR(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Error information logging:
		Used to log entry errors and crashes in the program.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['ERROR_TIME'][local_background],
				self._ColorScheme['ERROR_STATUS'][local_background],
				self._ColorScheme['ERROR_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_ERROR'][local_background],
				self._ColorScheme['ERROR_MESSAGE'][local_background],
				self._ColorScheme['ERROR_BACKGROUND'][local_background],
			], status_message_text, "!!ERROR", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def CRITICAL(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = True, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Critical error information logging:
		Used to log entry for critical and unpredictable program failures.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['CRITICAL_TIME'][local_background],
				self._ColorScheme['CRITICAL_STATUS'][local_background],
				self._ColorScheme['CRITICAL_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_CRITICAL'][local_background],
				self._ColorScheme['CRITICAL_MESSAGE'][local_background],
				self._ColorScheme['CRITICAL_BACKGROUND'][local_background],
			], status_message_text, "!!!@CRITICAL", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def START_PROCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Stub.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		# self._buffer << self._assemble_entry(
		# 	[
		# 		self._ColorScheme['PROGRESS_TIME'][local_background],
		# 		self._ColorScheme['PROGRESS_STATUS'][local_background],
		# 		self._ColorScheme['PROGRESS_STATUS_MESSAGE'][local_background],
		# 		self._ColorScheme['TYPE_PROGRESS'][local_background],
		# 		self._ColorScheme['PROGRESS_MESSAGE'][local_background],
		# 		self._ColorScheme['PROGRESS_BACKGROUND'][local_background],
		# 	], status_message_text, "&PROGRESS [*******.............] - 37%", message_text, bold, italic, invert, self._environment
		# )
		# if self._environment == LogEnvironments.CONSOLE:
		# 	self._buffer.update_console()
		pass
		# Must run on a thread

	def STOP_PROCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = False, invert: bool = False, local_background: bool = True):
		"""
		Stub.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		pass
		# Make transition to SUCCESS or FAIL

	def SUCCESS(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, local_background: bool = True):
		"""
		Success information logging:
		Used to log entry a message about the success of the process.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['SUCCESS_TIME'][local_background],
				self._ColorScheme['SUCCESS_STATUS'][local_background],
				self._ColorScheme['SUCCESS_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_SUCCESS'][local_background],
				self._ColorScheme['SUCCESS_MESSAGE'][local_background],
				self._ColorScheme['SUCCESS_BACKGROUND'][local_background],
			], status_message_text, "&SUCCESS", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

	def FAIL(self, *, status_message_text: str = "...", message_text: str = "...", bold: bool = False, italic: bool = True, invert: bool = False, local_background: bool = True):
		"""
		Fail information logging:
		Used to log entry a message about the failed execution of the process.

		:param status_message_text: Log entry status message
		:param message_text: Log entry message
		:param bold: Display entry with bold font?
		:param italic: Display entry with italic font?
		:param invert: Display entry with invert font?
		:param local_background: Display entry with background?
		:return: the generated log entry string
		"""
		self._buffer << self._assemble_entry(
			[
				self._ColorScheme['FAIL_TIME'][local_background],
				self._ColorScheme['FAIL_STATUS'][local_background],
				self._ColorScheme['FAIL_STATUS_MESSAGE'][local_background],
				self._ColorScheme['TYPE_FAIL'][local_background],
				self._ColorScheme['FAIL_MESSAGE'][local_background],
				self._ColorScheme['FAIL_BACKGROUND'][local_background],
			], status_message_text, "&FAIL", message_text, bold, italic, invert, self._environment
		)
		if self._environment == LogEnvironments.CONSOLE:
			self._buffer.update_console()

# Test
if __name__ == "__main__":
	# buf = TextBuffer(115)
	logger = Logger(program_name="WiretappingScaner", log_environment=LogEnvironments.CONSOLE, console_width=115)
	# buf = logger.get_buffer()
	logger.DEBUG(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.DEBUG_PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.PERFORMANCE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.EVENT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.global_background = True
	logger.AUDIT(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.METRICS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.time = False
	logger.USER(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.MESSAGE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.status_type = False
	logger.INFO(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message Test message")
	logger.NOTICE(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.get_buffer().replace(7, "7")
	logger.WARNING(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.ERROR(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.CRITICAL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	# logger.START_PROCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.SUCCESS(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	logger.FAIL(status_message_text="Test text", message_text="Test message Test message Test message Test message Test message")
	# print(logger.FAIL(status_message_text="33", message_text="34", invert=True))
	logger.get_buffer() << "55"
	logger.get_buffer().insert(3, "150")
	logger.INFO(status_message_text="Test text", message_text="Entrying was successful!", bold=True)
	logger.get_buffer() >> "buf"

	# logger.timeEnabled(False)
	# print(logger.DEBUG(status_message_text="1", message_text="2"))