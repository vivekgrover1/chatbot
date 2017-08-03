# chatbot
Chatbot to troubleshoot a server in chatops way using slack and python.

## Requirements for bot:

*	Python 3 

*	[pip](https://pip.pypa.io/en/stable/) to handle Python application dependencies.

*	[Free Slack account](https://slack.com/) with a team on which you have API access 

*	Official Python [slackclient](https://github.com/slackhq/python-slackclient) code library built by the Slack team and fabric3 library to execute the command on remote machine.

*	Slack API testing [token](https://api.slack.com/tokens)

## Install python3 and required packages for centos/redhat:

```
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm

sudo yum -y install python36u

sudo yum -y install python36u-pip

sudo pip install slackclient

sudo pip install fabric3

```

## Export Variables and download files:

```
export SLACK_BOT_TOKEN="xxx-xxxx-xxx"

export CHATBOT_NAME="xyz"

export EC2_KEY_PATH=/path/to/key

wget https://raw.githubusercontent.com/vivekgrover1/chatbot/master/slack_cmd_process.py

wget https://raw.githubusercontent.com/vivekgrover1/chatbot/master/slackbot.py

```
