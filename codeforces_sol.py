import requests
from lxml import html
import sys

def get_m_all(username,limit) :
    for idx in range(1,limit):
        page = requests.get('http://codeforces.com/submissions/'+username+'/page/'+str(idx))
        tree = html.fromstring(page.text)
        verdict = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[6]/span/span/text()')
        contestID = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[4]/a/text()')
        problemID = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[1]/a/text()')

        for i in range(len(contestID)):
            r = map(str,contestID[i].split())
            contestID[i] = list(r)[0][:-1]

        k=1

        for i in range(len(verdict)):
            if verdict[i] == 'Accepted':
                solutionPage = requests.get('http://codeforces.com/contest/'+str(contestID[i])+'/submission/'+str(problemID[i]))
                #problemPage = requests.get('http://codeforces.com/problemset/problem/'+str(problemID[i]))
                tree2 = html.fromstring(solutionPage.text)
                code = tree2.xpath('//*[@id="pageContent"]/div[3]/pre/text()')
                inp = 'solutions//p'+str(k)+'.txt' 
                f=open(inp,'w')
                sys.stdout = f
                for j in code:
                    j = j.rstrip('\r\n')
                    print(j)
                f.close()
                k=k+1

print('enter the name of the user :')
user = input()
print('enter the limit of the page :')
limit = int(input())
print('getting the solutions......')
get_m_all(user,limit)
print('got it....')