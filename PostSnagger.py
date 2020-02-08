# Copyright Jon Just 2/8/2020
# Please feel free to edit, distribute, or run this code to your hearts content, but
# contact me if you intend to profit off of it.

import praw
import time
import traceback

def main():
    reddit = praw.Reddit(client_id = '<ENTER CLIENT ID HERE>',
                         client_secret = '<ENTER CLIENT SECRET ID HERE>',
                         username = '<ENTER USERNAME OF BOT HERE>',
                         password = '<ENTER PASSWORD HERE>',
                         user_agent = 'PostSnagger')

    # INSTRUCTIONS:
    # Make <username> a mod on subreddit to be crawled. This will allow the bot access to the mod log.
    # Make sure to have your reddit app registered, plug your client id and secret client into this script.
    # Also, make sure to pip install praw before running. To learn more about praw visit https://praw.readthedocs.io/en/latest/
    # I would also recomend making the bot a mod and an approved submitter on the target subreddit; else spam filters will happen.

    # Should spam filters continue to be an issue, set up automoderator on the target subreddit.
    # In the config, add this (Make sure to remove the leftmost pound signs):

    ## User whitelist (comma delimited)
    #
    #    ---
    #
    #    author:
    #            name: <username>
    #        action: approve
    #        action_reason: user whitelist

    subreddit = reddit.subreddit('<ENTER SUBREDDIT TO BE CRAWLED HERE>')#subreddit to be crawled
    targetreddit = subreddit = reddit.subreddit('<ENTER SUBREDDIT TO BE POSTED IN HERE>')#Subreddit to be posted to

    while True:
        print('Initiating....')
        try:
            start_time = time.time()
            for log in subreddit.mod.stream.log():
                
                if log.created_utc > start_time:
                    print("action: {}, Mod: {}".format(log.action, log.mod))
                    print("description: {}, details: {}".format(log.description, log.details))
                    print("Link: {}, body: {}".format(log.target_permalink, log.target_body))
                    print("Id: {}, title: {}".format(log.id, log.target_title))
                    print("Created: {}".format(log.created_utc))

                    if log.action == 'removelink':
                        str = "https://old.reddit.com/" + log.target_permalink
                        print(str)
                        title = 'le "' + log.target_title + '" rage'
                        Submission = reddit.submission(url=str)
                        print(Submission.url)
                        print(title)

                        if not Submission.is_self:
                            print('checking if repost.... stage 1')
                            isNewPost = True

                            for submission in targetreddit.new(limit=5):
                                print(submission.title)
                                print('checking if repost.... stage 2')
                                if submission.title == title:
                                    isNewPost = False
                                    print('doublepost')

                            if isNewPost == True:
                                print('Posting....')
                                newLink = Submission.url
                                targetreddit.submit(title, url=newLink)

                    print('=============================================')
                    print('')
                    
        except Exception as e:
            traceback.print_exc() #Should only be happen when reddit servers stutter

if __name__ == "__main__":
    main()
