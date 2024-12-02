# tweet-grab

<img src="assets/logo.png" alt="Logo" width="200">

## overview
simple python script to webscrape a users tweets.

## features

+ Fetch a user's profile details (ID, name, followers count, and tweet count).
+ Retrieve and display tweets from the user's timeline.
+ Limit the number of tweets displayed.
+ Logs errors to assist in debugging issues with authentication or scraping.

## prerequisites


### python version (3.8+)

check if python 3.8+ is installed:

```bash
python --version
```

### conda environment

create a conda environment for the project:
```bash
conda create -n tweet-grab python=3.8
conda activate tweet-grab
```
you can set any python version above 3.8, I wrote this script using 3.12.2.

### dependencies

install dependencies:

```bash
pip install -r requirements.txt
```

### environment variables
create a ``.env`` file in the project root directory with the following keys:

```
USERNAME=<your_twitter_username>
EMAIL=<your_twitter_email>
PASSWORD=<your_twitter_password>
```

## usage

### running the script

Open a terminal in the project directory.

Run the script using the following format:

```bash
python main.py -u <username> [-l <limit>]
```

### example

```bash
python main.py -u ohnePixel -l 50
```

This will fetch and display the latest 50 tweets from ohnePixel's timeline.

you can also save the printed text into a file:

```bash
python main.py -u ohnePixel -l 50 > tweets.txt
```

if you leave out the ``-l``, the program will fetch all tweets of the given user

## logging

+ The script uses Python's built-in logging module to log exceptions during:
    - Login: Logs errors encountered while authenticating.
    - Tweet Retrieval: Logs errors encountered while fetching tweets.
+ Logs are output to the console for immediate debugging.

## error handling

+ Login Failure: If the login credentials are incorrect, the script will log an exception with the message error while logging in.
+ Scraping Error: If fetching tweets fails, an exception will be logged with the message error while scraping twitter/X.
+ Command-Line Arguments:
    - If -u is not provided, the script will terminate with the message: no flag for user_name (-u).
    - If an invalid value is provided for -l, the script defaults to fetching 100 tweets.

## notes

Rate Limiting: built in delay of 0.5 seconds to avoid being banned for scraping
    
Async Operations: everything is async

## Disclaimer

Not my fault if your account gets banned. Program crashes sometimes because twitter login is unreliable