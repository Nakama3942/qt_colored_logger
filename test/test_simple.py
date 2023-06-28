from time import sleep

from mighty_logger import Logger
from mighty_logger.src.lib_types_collection import LogEnvironments

if __name__ == "__main__":
	logger = Logger("Installer", LogEnvironments.CONSOLE, 115)
	sleep(1)
	logger.message("Program installation started")
	sleep(1)
	logger.warning("Newer version found")
	sleep(1)
	logger.might().separator()
	sleep(1)
	data = logger.might().getty("Enter password: ")
	sleep(1)
	logger.error("Incompatibility found")
	sleep(1)
	logger.fail("Program not installed")
	sleep(1)
	logger.might().empty(data)
	sleep(1)
	logger.might().savy("log", False)
	sleep(1)
	logger.debug("la la la")
	sleep(1)
	logger.might().loady("log")
	sleep(1)
	logger.debug("bla bla bla")
	sleep(1)
	logger.might().extractly(2)
	sleep(1)
	logger.debug("String has deleted")
	sleep(1)
	logger.might().empty(logger.might().catchy(1))
	logger.might().savy("log", False)
