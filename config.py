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