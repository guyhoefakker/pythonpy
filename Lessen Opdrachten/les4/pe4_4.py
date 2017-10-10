def new_password():
    oldpassword = input('old password: ')
    newpassword = input('new password: ')

    if len(newpassword) >= 5 and newpassword != oldpassword:
        return True
    else:
        return False

print(new_password())