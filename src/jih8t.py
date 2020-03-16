#!/usr/bin/env python3
#
# Configuration is loaded from ~/.jih8t.yml. Example config:
# jira:
#   server: https://foo.atlassian.net
#   user: foo@example.com
#   password: your-API-token
# issues_query: your JQL query
#

import yaml
from jira import JIRA
from pathlib import Path

# WORKLOG_AUTHOR = "radoslaw.kujawa"

with open(str(Path.home()) + "/.jih8t.yml", 'r') as ymlcfgfile:
    cfg = yaml.load(ymlcfgfile, yaml.FullLoader)

jira = JIRA(server=cfg['jira']['server'], basic_auth=(cfg['jira']['user'], cfg['jira']['password']))

# XXX search result can include worklog field if explicitedly asked for it
issues = jira.search_issues(cfg['issues_query'])

for i in issues:

    issue_complete = jira.issue(str(i))
    worklogs = issue_complete.fields.worklog.worklogs

    for w in worklogs:
        print(str(i) + "," + str(w.author) + "," + str(w.timeSpentSeconds))

