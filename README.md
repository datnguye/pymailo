# pymailo
Discord bot template in pythonic


#### Development or Installation:
1. Clone source code:
```
git clone https://github.com/datnguye/pymailo.git
cd pymailo
```

2. Create enviroment:
```
python -m venv env
.\env\Scripts\activate
OR source env/bin/activate (linux)

python -m pip install -r requirements.txt

```

3. Create dotenv file: ~/pymailo/.env
```
DISCORD_TOKEN=your_token
DISCORD_GUILD=your_discord_server_name
ERROR_PATH=/path/to/your_file.log
```

4. Run it!
```
.\env\Scripts\activate
python run.py
```

### Version used
```
Python 3.7.5
```

### USAGE - run.py

```
from pymailo import bot
bot.start()
```

### Available Commands
Typing -help in discord to see available commands


![Sample](/resources/sample.png)