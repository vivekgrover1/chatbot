# chatbot
Chatbot to troubleshoot a server in chatops way using slack and python.

## Requirements for bot:

*	Python 3 

*	pip to handle Python application dependencies.

*	Free Slack account with a team on which you have API access 

*	Official Python slackclient code library built by the Slack team and fabric3 library to execute the command on remote machine.

*	Slack API testing token

## Install python3 and required packages for centos/redhat:

```
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm

sudo yum -y install python36u

sudo yum -y install python36u-pip

sudo pip install slackclient

sudo pip install fabric3

```

## Export Variables:

```
export SLACK_BOT_TOKEN="xxx-xxxx-xxx"

export CHATBOT_NAME="xyz"
```
