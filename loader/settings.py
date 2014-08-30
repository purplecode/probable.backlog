settings = {
    'MCMP' : {
      'name' : 'MINT',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'MCMP',
        'stories' : 'project = MINT AND (labels != idea OR labels is empty) and status != Closed and issuetype = Story ORDER BY Rank ASC',
        'epics' : 'project = MINT AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'tasks' : 'project = MINT AND (issuetype = "Technical task" OR issuetype = Bug) AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    },
    'NDA' : {
      'name' : 'Spotlight',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'NDA',
        'stories' : 'project = NDA and status != Closed and issuetype = Story ORDER BY Rank ASC',
        'epics' : 'project = NDA AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'tasks' : 'project = NDA AND (issuetype = "Technical task" OR issuetype = Bug) AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    },
    'RNTDIM' : {
      'name' : 'RAN Dim',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'RNTDIM',
        'stories' : 'project = "RAN Dim" and status != Closed and issuetype = "User Story" ORDER BY Rank ASC',
        'epics' : 'project = "RAN Dim" AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC',
        'tasks' : 'project = "RAN Dim" AND (issuetype != "Epic" AND issuetype != "Story" AND issuetype != "User story") AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    }
  }


