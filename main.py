import praw
import logging
import time
from dotenv import load_dotenv
import os

from config import SUBREDDIT_NAME, KEYWORDS, CHECK_LIMIT


load_dotenv()


logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def create_reddit_client():

    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )

    return reddit


def check_post(post):

    text = (
        post.title +
        " " +
        post.selftext
    ).lower()


    for word in KEYWORDS:

        if word.lower() in text:

            logging.info(
                f"Keyword found: {word} | {post.title}"
            )

            print(
                "\nFOUND:"
            )

            print(
                post.title
            )

            print(
                post.url
            )

            return True


    return False



def monitor():

    reddit = create_reddit_client()

    subreddit = reddit.subreddit(
        SUBREDDIT_NAME
    )


    logging.info(
        "Bot started"
    )


    while True:

        try:

            posts = subreddit.new(
                limit=CHECK_LIMIT
            )


            for post in posts:

                check_post(post)


            time.sleep(
                60
            )


        except Exception as error:

            logging.error(
                str(error)
            )

            time.sleep(
                60
            )



if __name__ == "__main__":

    monitor()