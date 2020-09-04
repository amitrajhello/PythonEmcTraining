def get_user_list(data_file):
    """function definition"""
    try:
        list_of_users = []

        for line in open(data_file):
            login = line.split(':')[0]
            list_of_users.append(login)

        list_of_users.sort()

        # line_no = 1

        for index, user in enumerate(list_of_users, 1):  # using enumerate and starting enumerate value from 1 
            print('{:6} {}'.format(index, user))
            #  line_no += 1

    except (FileNotFoundError, IOError) as err:
        print(err)


get_user_list('passwd.txt')  # function call
