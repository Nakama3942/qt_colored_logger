# ##########################   Qt_Сolored-logger   ########################### #
# ---------------------------------------------------------------------------- #
#                                                                              #
# Copyright © 2023 Kalynovsky Valentin. All rights reserved.                   #
#                                                                              #
# Licensed under the Apache License, Version 2.0 (the "License");              #
# you may not use this file except in compliance with the License.             #
# You may obtain a copy of the License at                                      #
#                                                                              #
#     http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                              #
# Unless required by applicable law or agreed to in writing, software          #
# distributed under the License is distributed on an "AS IS" BASIS,            #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.     #
# See the License for the specific language governing permissions and          #
# limitations under the License.                                               #
#                                                                              #
# ---------------------------------------------------------------------------- #
# ############################################################################ #

# To compile and publish the library, you need to enter the following commands:
# python setup.py sdist
# twine upload dist/*

from setuptools import setup

with open("README.md", "r", encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name="qt_colored_logger",
    version="0.2.0",

    author="Kalynovsky 'Nakama3942' Valentin",
    author_email="nakama3942@gmail.com",

    description="Powerful functional logger with support for qt programming",
    long_description=readme,
    long_description_content_type="text/markdown",

    url="https://github.com/Nakama3942/qt_colored_logger",

    license="Apache License, Version 2.0, see LICENSE file",

    packages=[
        'qt_colored_logger',
        'qt_colored_logger.src',
        'qt_colored_logger.basic',
        'qt_colored_logger.basic.patterns'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Topic :: System :: Logging",
    ],
    project_urls={
        'Releases': 'https://github.com/Nakama3942/qt_colored_logger/releases',
    },
)
