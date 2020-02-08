# Reddit-Removed-Post-Snagger
Watches the modlog of a subreddit, and reposts removed posts in a target subreddit.

INSTRUCTIONS:
   Make <username> a mod on subreddit to be crawled. This will allow the bot access to the mod log.
   Make sure to have your reddit app registered, plug your client id and secret client into this script.
   Also, make sure to pip install praw before running. To learn more about praw visit https://praw.readthedocs.io/en/latest/
   I would also reccomend modding the bot, and adding it as an approved submitter on the target subreddit; else spam filters will 
   happen.
   
   Please ensure you have edited PostSnagger.py to contain all the information necessary for the script to run your bot.
   It is also recomended to have a dedicated reddit account specifically for the bot.
   
   Should spam filters continue to be an issue, set up automoderator on the target subreddit.
   
   In the config, add this:

    # User whitelist (comma delimited)
    
       ---
    
        author:
                name: <username>
            action: approve
            action_reason: user whitelist
