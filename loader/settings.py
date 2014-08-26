settings = {
    'MCMP' : {
      'name' : 'MINT',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'MCMP',
        'stories' : 'project = MINT AND (labels != idea OR labels is empty) and status != Closed and issuetype = Story ORDER BY Rank ASC',
        'epics' : 'project = MINT AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    },
    'NDA' : {
      'name' : 'Spotlight',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'NDA',
        'stories' : 'project = NDA and status != Closed and issuetype = Story ORDER BY Rank ASC',
        'epics' : 'project = NDA AND issuetype = Epic AND status != Closed AND (labels != nobacklog OR labels is empty) ORDER BY Rank ASC'
      }
    }
  }


