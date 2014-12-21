settings = {
    'MCMP' : {
      'name' : 'MINT',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'MCMP',
        'epics' : 'project = MINT AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'stories' : 'project = MINT and issuetype = Story and "Epic Link" in (%s) AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'tasks' : 'project = MINT AND (issuetype in (subTaskIssueTypes(), Bug, Improvement, "Technical task")) AND parent in (%s) AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    },
    'NDA' : {
      'name' : 'Spotlight',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'NDA',
        'epics' : 'project = NDA AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'stories' : 'project = NDA and issuetype = Story and "Epic Link" in (%s) AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'tasks' : 'project = NDA AND (issuetype in (subTaskIssueTypes(), Bug, Improvement, "Technical task")) AND parent in (%s) AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    },
    'RNTDIM' : {
      'name' : 'RAN Dim',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'RNTDIM',
        'epics' : 'project = "RAN Dim" AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'stories' : 'project = "RAN Dim" and issuetype = "User Story" and "Epic Link" in (%s) AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'tasks' : 'project = "RAN Dim" AND (issuetype in (subTaskIssueTypes(), Bug, Improvement, "Technical task")) AND parent in (%s) AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    },
    'CSCLOUD': {
      'name' : 'Cloud Controller',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'CSCLOUD',
        'epics' : 'project = CSCLOUD AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'stories' : 'project = CSCLOUD and issuetype = Story and "Epic Link" in (%s) AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'tasks' : 'project = CSCLOUD AND (issuetype in (subTaskIssueTypes(), Bug, Improvement, "Technical task")) AND parent in (%s) AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    }
  }


