def get_user_list(data_file, target_file):  # function definition
    try:
        list_of_users = []

        for line in open(data_file):
            login = line.split(':')[0]
            list_of_users.append(login)
        list_of_users.sort()

        fw = open(target_file, 'w')
        # line_no = 1

        for index, user in enumerate(list_of_users, 1):  # using enumerate and starting enumerate value from 1
            content = '{:6} {}'.format(index, user)
            print(content)
            fw.write(content + '\n')
            #  line_no += 1
        fw.close()
    except (FileNotFoundError, IOError) as err:
        print(err)


get_user_list('passwd.txt', 'passwd.dat')  # function call
