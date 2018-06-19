# iliadbot

iliadbot è un bot telegram che permette di conoscere soglie e credito della tua SIM iliad. Il bot non è ufficiale e non conserva o salva le tue credenziali di accesso. Il codice sorgente è rilasciato sotto licenza AGPL 3.0.

Potresti non fidarti che non salviamo le tue credenziali e voler eseguire una tua istanza del bot. Di seguito le istruzioni per farlo.

## Run this bot by yourself:

### On Linux:

- Move to the path where you want to create the virtualenv directory
```
cd path
```
- Create a folder containing the env named `iliadbotenv`
```
virtualenv -p python3 iliadbotenv 
```
- Install the bot from the zip
```
iliadbotenv/bin/pip install https://github.com/91dariodev/iliadbot/archive/master.zip
```
- Run the bot. The first parameter of the command is the `config.yaml` file. Copy from the source `config.example.yaml` and create a file named `config.yaml` replacing values.
```
iliadbotenv/bin/iliadbot path/config.yaml
```
- To upgrade the bot:
```
iliadbotenv/bin/pip install --upgrade https://github.com/91dariodev/iliadbot/archive/master.zip
```
- To delete everything:
```
cd ..
rm -rf iliadbotenv
```



### COMANDI SUPPORTATI:
```
/info - permette di conoscere stato soglie e credito`
/help - mostra un messaggio di aiuto
```
