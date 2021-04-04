# Topmonitor

## Requirements

* Set env variables `TELEGRAM_CHAT_ID` and `TELEGRAM_BOT_TOKEN` to get notifications over Telegram

    ``` sh
    export TELEGRAM_CHAT_ID=<your telegram chat ID>
    export TELEGRAM_BOT_TOKEN=<your telegram bot token>
    export URL=<url to monitor>
    ```

* Install `python3` and `git` 

* clone repository

* Imstall dependencies:
  ``` sh
  pip install -r requirements.txt
  ``` 

## Usage

### Run
``` sh
python3 app/topmonitor.py --area outdoor-length --start-at 17:00 --date 2021-04-05
```

### Get help

``` sh
$ python3 app/topmonitor.py --help
Usage: topmonitor.py [OPTIONS]

  Monitor top logger for free slots

Options:
  --area TEXT      Climbing area: bouldering, indoor-length, outdoor-length
  --date TEXT      date: yyyy-mm-dd
  --start-at TEXT  Starting time hh:mm
  --help           Show this message and exit.
```  