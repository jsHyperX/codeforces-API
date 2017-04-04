import requests
from lxml import html
import sys

def get_m_all(username,limit) :
    for idx in range(1,limit):
        page = requests.get('http://codeforces.com/submissions/'+username+'/page/'+str(idx))
        tree = html.fromstring(page.text)
        status = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[6]/span/span/text()')
        contest_id = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[4]/a/text()')
        problem_id = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[1]/a/text()')

        for i in range(len(contest_id)):
            r = map(str,contest_id[i].split())
            contest_id[i] = list(r)[0][:-1]

        k=1

        for i in range(len(status)):
            if status[i] == 'Accepted':
                solutionPage = requests.get('http://codeforces.com/contest/'+str(contest_id[i])+'/submission/'+str(problem_id[i]))
                tree2 = html.fromstring(solutionPage.text)
                code = tree2.xpath('//*[@id="pageContent"]/div[3]/pre/text()')
                inp = 'CFsol//solutions//p'+str(k)+'.txt' 
                f=open(inp,'w')
                sys.stdout = f
                for j in code:
                    j = j.rstrip('\r\n')
                    print(j)
                f.close()
                k=k+1

