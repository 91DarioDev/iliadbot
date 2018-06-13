# iliadbot - A telegram bot for telegram public groups leaderboards
# Copyright (C) 2018  Dario <dariomsn@hotmail.it> (github.com/91DarioDev)
#
# iliadbot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# iliadbot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with iliadbot.  If not, see <http://www.gnu.org/licenses/>.


import setuptools


setuptools.setup(

    name="iliadbot",
    version="1",

    license="AGPL-3.0",

    author="iliadbot authors",

    install_requires=[
        "requests==2.7.0",
        "lxml==4.2.1"
    ],

    packages=[
        "iliadbot",
    ],

    entry_points={
        "console_scripts": [
            "iliadbot = iliadbot.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)