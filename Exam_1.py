## 1. REST API: Number of Drawn Matches

# Input:
# year = 2011
# Output:
# 516

import requests
import json
def getNumDraws(year):
    total = 0
    for g in range(0, 11):
        url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' +str(year)+ '&team1goals=' +str(g)+ '&team2goals=' +str(g)+ '&page=1'
        response = requests.request('GET', url, headers={}, data={})
        r = json.loads(response.text.encode('utf8'))
        total += r['total']
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip()
    result = getNumDraws(year)
    fptr.write(str(result) + '\n')
    fptr.close()

