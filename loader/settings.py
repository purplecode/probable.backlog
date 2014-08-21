settings = {
    'MINT' : {
      'name' : 'MINT',
      'url' : 'https://jira3.inside.nsn.com',
      'queries' : {
        'project' : 'MCMP',
        'stories' : 'project = MINT AND (labels != idea OR labels is empty ) and status != Closed and issuetype = Story ORDER BY Rank ASC',
        'epics' : 'project = MINT and issuetype = Epic and status != Closed'
      }
    }
  }