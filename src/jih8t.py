#!/usr/bin/env python3
#
# Configuration is loaded from ~/.jih8t.yml. Example config:
# jira:
#   server: https://foo.atlassian.net
#   user: foo@example.com
#   password: your-API-token
# issues_query: your JQL query
#

#from collections import Counter
import yaml
from jira import JIRA
from pathlib import Path

with open(str(Path.home()) + "/.jih8t.yml", 'r') as ymlcfgfile:
    cfg = yaml.load(ymlcfgfile, yaml.FullLoader)

jira = JIRA(server=cfg['jira']['server'], basic_auth=(cfg['jira']['user'], cfg['jira']['password'])) 

issues = jira.search_issues(cfg['issues_query'])

print(issues)

# iterate over issues, query for issue individually to obtain worklog
# store worklog entries from current time_period

#print(issue.fields.worklog.worklogs[0].timeSpentSeconds)

# Find the top three projects containing issues reported by admin
#top_three = Counter([issue.fields.project.key for issue in issues]).most_common(3)

#print(top_three)
