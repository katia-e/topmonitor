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

### List available time slots
``` sh
python3 app/topmonitor.py list-slots --area outdoor-length --date 2021-04-19
```


### Run
``` sh
python3 app/topmonitor.py --area outdoor-length --slots 17:00,19:30 --date 2021-04-05
```

### Get help

``` sh
$ python3 app/topmonitor.py --help
Usage: topmonitor.py [OPTIONS] COMMAND [ARGS]...

  Monitor top logger for free slots

Options:
  --area TEXT                 Climbing area: ['bouldering', 'indoor-length',
                              'outdoor-length']
  --date TEXT                 Date: yyyy-mm-dd or today/tomorrow, default:
                              today
  --slots TEXT                List of slots to monitor, format: hh:mm,
                              default: all time slots will be monitored
  --pooling-interval INTEGER  Time interval between calls, default 60s
  --help                      Show this message and exit.

Commands:
  list-slots
```  