import CFsol

if __name__ == '__main__' :
    print('enter the name of the user :')
    user = input()
    print('enter the limit of the pages you want to download solutions from :')
    limit = int(input())
    print('getting the solutions......')
    CFsol.get_m_all(user,limit)
    print('got it....')
