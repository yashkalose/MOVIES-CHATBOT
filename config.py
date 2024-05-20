###################################################################
######## Configuration files for Bot   ##########################
###################################################################

"""
    config.py 
    
    This files has all the configurations for your bot.
    
"""

import os
import watson_developer_cloud
from slackclient import SlackClient

location = r"C:\Users\yashk\OneDrive\Desktop\KELLY\Movie-Recommendation-Chatbot"  

###################################################################
######## Slack configuration   ##########################
###################################################################

SLACK_BOT_TOKEN='xoxp-7131580451249-7118914473250-7165047265280-7b17ed8bd6a87c6c7660c9a24173d31c'
SLACK_VERIFICATION_TOKEN='DyKNPejNcLpnFLhJY0epUQxI' 

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

service = watson_developer_cloud.AssistantV1(
    iam_apikey = 'Saltnpepper@1', 
    version = '2.97.3'
)

workspace_id = '0b861367-cf36-444d-bb89-f608466e4b2e' 

###################################################################
######## Log files configuration   ##########################
###################################################################

log_commands_path = location + "logs/log_commands.py" 
follow_up_path = location + "logs/followup_email.py" 
###################################################################
######## Temp files configuration   ##########################
###################################################################

onetime_path = location + "nlp/nlp_solutions/onetime_run_file.py" 
onetime_file = location + "nlp/nlp_solutions/onetime.txt" 
