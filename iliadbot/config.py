# iliadbot - A telegram bot to check your iliad's balance and quotas
# Copyright (C) 2018  iliadbot authors: see AUTHORS file at the top-level directory of this repo
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


import yaml
import sys


PATH = "config/config.yaml"
if len(sys.argv) == 2:
    PATH = sys.argv[1]  # takes the path specified as arg instead of the default one
try:
    with open(PATH, 'r') as stream:
        conf = yaml.load(stream)
except FileNotFoundError:
    print(
        "\n\nWARNING:\n"
        "before of running iliadbot you should create a file named `config.yaml`"
        " in `config`.\n\nOpen `config/config.example.yaml`\ncopy all\ncreate a file "
        "named `config.yaml`\nPaste and replace sample variables with true data."
        "\nIf the file is in another path, you can specify it as the first parameter."
        "\nExample: <iliadbot /home/my_files/config.yaml>"
    )
    sys.exit()

BOT_TOKEN = conf['bot_token']