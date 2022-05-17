# LineWar Data Collection

## What it does

The main.py script downloads the current leaderboard from the game LineWar. After that it is parsed and than stored in a *.csv table for further use.

Leaderboard:

https://linewar.com/leaderboard

## How to automate
https://tecadmin.net/crontab-in-linux-with-20-examples-of-cron-schedule/

Example:

Add crontab job:

````
crontab -e
````

Starts the main.py script every 2 hours:
(replace YOUR_PATH with ``pwd`` of the main.py file location)

````
* */2 * * * python YOUR_PATH/main.py
````
