from github import Github
from slackclient import SlackClient

g = Github("tarchibald", "xxxxxxxx")

channel = 'pullrequest'

repo = g.get_repo("tarchibald/skillsoft_test1")

#todo - add date filter
pulls = repo.get_pulls(state='open', sort='created', base='master')

for pr in pulls:

    prinfo = "PR Number: %d  PR State: %s " % (pr.number, pr.state) 

    print(prinfo) 

    slack_message(prinfo, channel)


#slack no longer test tokens https://api.slack.com/legacy/custom-integrations/legacy-tokens
def slack_message(message, channel):

    token = 'XXXXXXXX'

    sc = SlackClient(token)

    sc.api_call('chat.postMessage', channel=channel, text=message, username='xxxxxxxx')   