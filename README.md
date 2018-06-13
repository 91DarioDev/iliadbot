# iliadbot

Questo bot permette di conoscere soglie e credito della tua SIM iliad. Il bot non è ufficiale e non conserva o salva le tue credenziali di accesso. Il codice sorgente è rilasciato sotto licenza AGPL 3.0.

Potresti non fidarti che non salviamo le tue credenziali e voler eseguire una tua istanza del bot. Di seguito le istruzioni per farlo.

## Run this bot by yourself:

**Clone e install:**
```
cd path
git clone https://github.com/91DarioDev/iliadbot
cd iliadbot
pip install .
```

**Config the bot:**
- open `iliadbot/config/config.example.yaml`
- select all and copy
- create a file `iliadbot/config/config.yaml`
- paste and replace the values with real values
- save and close

**Run the bot:**
```
iliadbot
```
Note: _In case you want to call iliadbot from another path, you can, but you have to specify the path of the config.yaml file as first argument in the cli.
Example:_

```
iliadbot path/iliadbot/config/config.yaml
```

**Upgrade the bot:**
```
cd path/iliadbot
git pull https://github.com/91DarioDev/iliadbot
pip install --upgrade .
```



### COMANDI SUPPORTATI:
```
/info - permette di conoscere stato soglie e credito`
/help - mostra un messaggio di aiuto
```
