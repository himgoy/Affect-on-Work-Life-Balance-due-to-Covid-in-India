from Scweet.scweet import scrape

# taggs = [['worklife'], ['workplacewellness'],
#          ['homeschooling', 'hometasking', 'backtoschool', 'homeschool']]

# # 10 March to 23 May
# for tag in taggs:
data = scrape(
    words=['workplacewellness india'], since="2020-03-10", until="2020-05-23", from_account=None, interval=1,
    headless=False, display_type="Top", save_images=False, lang="en", resume=False, filter_replies=False,
    proximity=False)

# ['getjob', 'jobless', 'unemployment', 'unemployed',  'jobsearch','backtowork','workplacewellness','homeschooling', 'hometasking', 'backtoschool', 'homeschool', 'homeoffice']


# [['worklifebalance india'], ['worklife'],
#  ['homeschooling india', 'hometasking india', 'backtoschool india', 'homeschool india']]

# DONE

# ['WFH', 'workfromhome', 'work from home', 'workingfromhome', 'working from home',
#                      'worklifebalance', 'work life balance', 'worklife', 'work life']

# Lockdown1.zip: March 25, 2020 - April 02, 2020; corona_tweets_08.csv to corona_tweets_14.csv
#
# Lockdown2.zip: April 14, 2020 - April 21, 2020; corona_tweets_27.csv to corona_tweets_33.csv
#
# Lockdown3.zip: May 01, 2020 - May 07, 2020; corona_tweets_44.csv to corona_tweets_49.csv
#
# Lockdown4.zip: May 18, 2020 - May 23, 2020; corona_tweets_61.csv to corona_tweets_66.csv
