# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'paras.lehana'
insta_password = 'DR-QdNNRw9cN&Z6'

""" comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration :thumbsup:',
        'Just incredible :open_mouth:',
        'What camera did you use @{}?',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        'I can feel your passion @{} :muscle:'] """

comments = {
        "default": ['Nice shot! @{}',
                        'I love your profile! @{}',
                        'Your feed is an inspiration :thumbsup:',
                        'Just incredible :open_mouth:',
                        'What camera did you use @{}?',
                        'Love your posts @{}',
                        'Looks awesome @{}',
                        'Getting inspired by you @{}',
                        ':raised_hands: Yes!',
                        'I can feel your passion @{} :muscle:']

        , "photo": [u'Stunning Shot 📸, @{}',
                        u'That is what you call a shot 🔥 @{}',
                        ':thumbsup:',
                        u'Incredible shot 🤩',
                        u'Camera or mobile?, @{}? 🤩',
                        u'🔥', u'📸 👍', u'📸 ❤️', u'🤓', u'🤩',
                        u'Awesome, @{} 🔥',
                        u'Gear? 📸',
                        'Which camera did you use? 🔥',
                        u'This pic is 🔥']

        , "video": []
}

tags = {
        "default": ['mobile photography', 'photography', 'low light photography', "galaxy note 9", "note 9", "note9", "samsung", "samsung galaxy note", "note 9 photography", "india", "i love india", "snapseed", "eyeem"]
        , "specific": []
}



# get an InstaPy session!
# headless_browser: set True to run InstaPy in the background
# geckodriver_path: If browser doesn't start, there is probably issue with geckodriver. Download latest driver and add path in geckodriver_path

# Use this for windows (geckdriver path is required)
""" session = InstaPy(username=insta_username, password=insta_password, headless_browser=False,
        geckodriver_path="D:\\Developer\\geckodriver-v0.26.0-win64\\geckodriver.exe",
        want_check_browser = False
) """

# Else use this for Linux 
session = InstaPy(
        headless_browser=False,
        geckodriver_path="/home/paras/Storage/path/geckodriver",
        want_check_browser = False
)

with smart_run(session):
        """ Activity flow """		
        # general settings		

        # -- LIKE
        # ~70% of the by InstaPy viewed posts will be liked
        session.set_do_like(enabled=True, percentage=100)

        session.set_dont_like(['#exactmatch', '[startswith', ']endswith', '[lesbian', '[gay', '[like'])
        # will ignore the don't like if the description contains one of the given words
        session.set_ignore_if_contains(['glutenfree', 'french', 'tasty'])

        # completely ignore liking images from certain users
        session.set_ignore_users(['random_user', 'another_username'])

        #  searches the description, location and owner comments for words and will like the image if any of those words are in there
        # session.set_mandatory_words(['#food', '#instafood'])

        session.set_mandatory_language(enabled=True, character_set=['LATIN'])

        session.set_delimit_liking(enabled=True, max_likes=500, min_likes=5)
	

        # activity		
        # session.like_by_tags(["natgeo"], amount=10)

        # Joining Engagement Pods


        # -- COMMENT
        # default enabled=False, ~ every 4th image will be commented on
        # session.set_do_comment(enabled=True, percentage=25)
        session.set_do_comment(enabled=True, percentage=50)

        # you can also set comments for specific media types (Photo / Video)
        session.set_comments(comments["photo"], media='Photo')
        session.set_comments(comments["video"], media='Video')

        session.set_delimit_commenting(enabled=True, max_comments=30, min_comments=2)

        # -- FOLLOW
        # default enabled=False, follows ~ 10% of the users from the images, times=1
        # times = 2: (only follows a user twice (if unfollowed again))
        session.set_do_follow(enabled=True, percentage=50, times=1)

        # will prevent commenting on and unfollowing your good friends (the images will still be liked)
        # session.set_dont_include(['friend1', 'friend2', 'friend3'])

        session.set_dont_unfollow_active_users(enabled=True, posts=1)

        session.set_skip_users(skip_private=True,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100,
                       skip_business=True,
		       skip_non_business=False,
                       business_percentage=100,
                       skip_business_categories=[],
                       dont_skip_business_categories=[]
        )

        # potency_ratio: follows users having greater followers/following. If negative, absolute value of following/followers is checked. 

        session.set_relationship_bounds(enabled=True,
                                potency_ratio=None,
                                delimit_by_numbers=True,
                                max_followers=3000,
                                max_following=900,
                                min_followers=50,
                                min_following=50,
                                min_posts=25,
                                max_posts=10000
        )

        session.set_simulation(enabled=False)

        # session.follow_likers(['paras.lehana'], photos_grab_amount = 10, follow_likers_per_photo = 10, randomize=True, sleep_delay=600, interact=False)
        # session.follow_commenters(['paras.lehana'], amount=10, daysold=10, max_pic = 10, sleep_delay=600, interact=False)

        session.unfollow_users(amount=60, instapy_followed_enabled=True, instapy_followed_param="nonfollowers", style="RANDOM", unfollow_after=7*24*60*60, sleep_delay=501)

        # session.join_pods(topic='sports', engagement_mode='no_comments')

        # -- TAGS
        # Generate smart hashtags based on https://displaypurposes.com ranking,
        # banned and spammy tags are filtered out.
        # (limit) defines amount limit of generated hashtags by hashtag
        # (sort) sort generated hashtag list 'top' and 'random' are available
        # (log_tags) shows generated hashtags before use it
        # (use_smart_hashtags) activates like_by_tag to use smart hashtags

        session.set_smart_hashtags(tags["default"], limit=5, sort='top', log_tags=True)
        session.like_by_tags(amount=50, use_smart_hashtags=True)


        # Use_smart_location_hashtags activates like_by_tag to use smart hashtags
        # Generate smart hashtags based on https://displaypurposes.com/map ranking. Banned and spammy tags are filtered out.

        # session.set_smart_location_hashtags(['noida'], radius=40, limit=20)
        # session.like_by_tags(amount=10, use_smart_location_hashtags=True)


        # -- SUPERVISE
        session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True,
                peak_likes_hourly=None,
                peak_likes_daily=585,
                peak_comments_hourly=21,
                peak_comments_daily=182,
                peak_follows_hourly=2,
                peak_follows_daily=10,
                peak_unfollows_hourly=35,
                peak_unfollows_daily=402,
                peak_server_calls_hourly=None,
                peak_server_calls_daily=4700
        )