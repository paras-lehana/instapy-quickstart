# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'paras.lehana'
insta_password = 'coolXDA@4'

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
                        u'This post is 🔥',
                        'I can feel your passion @{} :muscle:'],

        "photo": [],

        "video": []
}



# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username, password=insta_password, headless_browser=False)

with smart_run(session):
        """ Activity flow """		
        # general settings		

        # ~70% of the by InstaPy viewed posts will be liked
        session.set_do_like(enabled=True, percentage=70)


        session.set_dont_include(["friend1", "friend2", "friend3"])		

        # activity		
        session.like_by_tags(["natgeo"], amount=10)

        # Joining Engagement Pods

        # default enabled=False, ~ every 4th image will be commented on
        session.set_do_comment(enabled=True, percentage=35)

        # you can also set comments for specific media types (Photo / Video)
        session.set_comments(comments["photo"], media='Photo')
        session.set_comments(comments["video"], media='Video')

        # default enabled=False, follows ~ 10% of the users from the images, times=1
        # times = 2: (only follows a user twice (if unfollowed again))
        session.set_do_follow(enabled=True, percentage=10, times=1)

        session.join_pods(topic='sports', engagement_mode='no_comments')
