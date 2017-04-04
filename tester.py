import CFsol.getSolutions as CF

if __name__ == '__main__':
    print('enter the name of the user :')
    user = input()
    print('enter the limit of the page :')
    limit = int(input())
    print('getting the solutions......')
    CF.get_m_all(user,limit)
    print('all done!!...')
