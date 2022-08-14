## 2. REST API: Football Competition Winner's Goals
# Input:
# competition = 'UEFA Champions League'
# year = 2011
# Output:
# 28
# Input (stdin)
# English Premier League
# 2014
# Expected Output
# 73
# Input (stdin)
# La Liga
# 2012
# Expected Output
# 115

import requests
import json
def getWinnerTotalGoals(competition, year):
    goals = 0
    url = 'https://jsonmock.hackerrank.com/api/football_competitions?name=' +competition+ '&year=' +str(year)
    response = requests.request('GET', url, headers={}, data={})
    winner = json.loads(response.text.encode('utf8'))['data'][0]['winner']
    for team in ['team1', 'team2']:
        url = 'https://jsonmock.hackerrank.com/api/football_matches?competition=' +competition+ '&year=' +str(year)+ '&' +team+ '=' +winner+ '&page=1'
        response = requests.request('GET', url, headers={}, data={})
        total_pages = json.loads(response.text.encode('utf8'))['total_pages']
        for i in range(1, total_pages+1):
            url = 'https://jsonmock.hackerrank.com/api/football_matches?competition=' +competition+ '&year=' +str(year)+ '&' +team+ '=' +winner+ '&page=' +str(i)
            response = requests.request('GET', url, headers={}, data={})
            r = json.loads(response.text.encode('utf8'))
            r_data = r['data']
            for record in r_data:
                goals += int(record[team+'goals'])
    return goals
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    competition = input()
    year = int(input().strip())
    result = getWinnerTotalGoals(competition, year)
    fptr.write(str(result) + '\n')
    fptr.close()
