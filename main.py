import sys
import os
import asyncio
import time
import logging

from twikit import Client
from dotenv import load_dotenv
import twikit

def twikit_result_to_list(result: twikit.utils.Result):
    tweet_list = []

    for tweet in result:
        tweet_list.append(tweet)

    return tweet_list


async def print_user_tweets(client, user_name, limit):
    """prints out the specified number of tweets made by the user who's username matches

    Args:
        client (Client): the logged in user, used to scrape twitter
        user_name (str): username of the user who's tweets will be displayed
        limit (int): how many tweets will be displayed
    """
    user = await client.get_user_by_screen_name(user_name)

    print(
        f'id: {user.id}',
        f'name: {user.name}',
        f'followers: {user.followers_count}',
        f'tweets count: {user.statuses_count}',
        sep='\n'
    )

    if limit == 0:
        limit = user.statuses_count

    user_tweets_result = await user.get_tweets('Tweets')
    user_tweets = twikit_result_to_list(user_tweets_result)

    counter = 0
    for tweet in user_tweets:
        print("-------------------------------------")
        
        if counter >= limit:
            break

        time.sleep(0.5)
        print(tweet.text)
        counter += 1

        if counter == len(user_tweets):
            user_tweets_result = await user_tweets_result.next()

            more_tweets = twikit_result_to_list(user_tweets_result)

            for new_tweet in more_tweets:
                user_tweets.append(new_tweet)
        


async def main(user_name, limit):
    load_dotenv()

    client = Client('en-US')
    
    try:
        await client.login(
            auth_info_1=os.getenv("USERNAME"),
            auth_info_2=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD")
        )

        client.save_cookies("cookies.json")
    except:
        logging.exception("error while logging in")

    try:
        await print_user_tweets(client, user_name, limit)

    except:
        logging.exception("error while scraping twitter/X")


if __name__ == "__main__":
    limit = 0

    user_name = ""

    if "-u" not in sys.argv:
        print("no flag for user_name (-u)")
        sys.exit(1)

    user_name = sys.argv[sys.argv.index("-u")+1]
            
    try:
        limit = int(sys.argv[sys.argv.index("-l")+1])
    except ValueError:
        print("limit not set getting all tweets")

    asyncio.run(main(user_name, limit))