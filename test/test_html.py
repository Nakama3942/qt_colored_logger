from time import sleep

from mighty_logger import Logger
from mighty_logger.src import LogEnvironments, TypesEntries

if __name__ == "__main__":
	logger = Logger(program_name="Test", log_environment=LogEnvironments.HTML, status_message_global_entry=False)

	logger.message(message_text="Program installation started")

	sleep(1)
	logger.start_indefinite_process(message_text="File upload")
	sleep(2)
	logger.note_process(entry_type=TypesEntries.ACHIEVEMENT, message_text="Files downloaded")
	sleep(3)
	logger.progress_rise(100)
	logger.stop_process(message_text="Files unzipped")

	logger.warning(message_text="Newer version found")

	sleep(1)
	logger.start_definite_process(message_text="Installing files")
	sleep(0.6)
	logger.progress_rise(3)
	sleep(0.4)
	logger.progress_rise(7)
	sleep(0.3)
	logger.progress_rise(14)
	sleep(0.5)
	logger.progress_rise(16)
	sleep(1.1)
	logger.progress_rise(19)
	sleep(1.5)
	logger.progress_rise(25)
	sleep(1.4)
	logger.progress_rise(35)
	sleep(1.4)
	logger.progress_rise(45)
	sleep(1.6)
	logger.progress_rise(46)
	sleep(1.1)
	logger.progress_rise(47)
	logger.note_process(entry_type=TypesEntries.MILESTONE, message_text="Files prepared")
	sleep(3.7)
	logger.progress_rise(76)
	sleep(1.5)
	logger.progress_rise(77)
	sleep(1.4)
	logger.progress_rise(79)
	sleep(1.1)
	logger.progress_rise(81)
	sleep(1.2)
	logger.progress_rise(82)
	sleep(1.3)
	logger.progress_rise(85)
	sleep(0.8)
	logger.note_process(entry_type=TypesEntries.ERROR, message_text="Incompatibility found")
	sleep(1.3)
	logger.note_process(entry_type=TypesEntries.RESOLVED, message_text="Incompatibility eliminated")
	sleep(1.1)
	logger.progress_rise(86)
	sleep(0.6)
	logger.progress_rise(87)
	sleep(0.9)
	logger.progress_rise(88)
	sleep(0.9)
	logger.progress_rise(89)
	sleep(0.9)
	logger.progress_rise(90)
	sleep(1.4)
	logger.progress_rise(91)
	sleep(1.8)
	logger.progress_rise(97)
	sleep(1.5)
	logger.progress_rise(100)
	sleep(1.3)
	logger.stop_process(message_text="Program installed")

	logger.buffer().save("log.html")
