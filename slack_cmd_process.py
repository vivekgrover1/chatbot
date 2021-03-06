from fabric.api import *
from fabric.tasks import execute
import os

help="""Use below commands to get the system information.\n\ncommand apache status host <hostname> - to get the apache status.\n
command free host <hostname> - to get the amount of used and free memory in the system.\n
command last log host <hostname>- to get the last ten line of log file /var/file/messages.\n
command uptime host <hostname> - to get the time how long the system has been running and load average.\n
command list cpu host <hostname> - to get the information about CPU architecture."""


def cmd_process(command):
    """
      Decide the command which is to be run based on user message directed
      at bot.
    """
    lis=command.split(" ")
   # print lis
    if lis[0].startswith("hi"):
        return "I am doing good, How about you?","good"
    if lis[0]=="help" and len(lis)==1:
        return help, "good"
    if lis[0]=="command" and len(lis)>=3:
        if lis[1]=="apache" and lis[2]=="status" and lis[3]=="host":
           return cmd_exec("systemctl status httpd",lis[4],"apache_status")
        if lis[1]=="free" and lis[2]=="host":
            return cmd_exec("free -m",lis[3],"free")
        if lis[1]=="last" and lis[2]=="log" and lis[3]=="host":
            return cmd_exec("sudo tail -10 /var/log/messages",lis[4],"last_10_lines_log")
        if lis[1]=="uptime" and lis[2]=="host":
              return cmd_exec("uptime",lis[3],"uptime")
        if lis[1]=="list" and lis[2]=="cpu" and lis[3]=="host":
            return cmd_exec("lscpu",lis[4],"lscpu")
        if lis[1]=="search" and lis[3]=="host":
            return cmd_exec("sudo grep %s /var/log/messages | head " %lis[2],lis[4],"search_log")
        if lis[1]=="process" and lis[3]=="host":
            return cmd_exec("sudo ps -ef | grep %s " %lis[2],lis[4],"search_process")

    return "Not sure what you mean, please use help.","danger"

def cmd_exec(command,host,keyword):
    """
      execute the command on the provided host in the message and return message
      based of successfull or unsuccessful cmd execution.

    """
    try:
        status = execute(remote_exec, 'ec2-user','%s' %command,hosts=["%s" %host])
        #print status["%s" %host][0]
        if  status["%s" %host][1] == False :
            return "Action EC2.%s completed." %keyword +" \nStatus: Successfull\nHost: %s\n\nResult:\n\n" %host + status["%s" %host][0],"good"
    except :
        return "Coundn't Connect the host, please check the host name or try again.","danger"

def remote_exec(user,cmd):
    """
      execute the actual command on the remote aws machine using fabric maodule and return the output
      of the command and status of the cmd execution success or failed.
    """

    with hide('output'):
         env.user=user
         env.key_filename = os.environ.get('EC2_KEY_PATH')
         env.warn_only='True'
         result= run(cmd)
         return result, result.failed

