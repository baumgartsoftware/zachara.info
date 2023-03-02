def user_dir_path(instance, filename):
    return 'users/user_{0}/{1}'.format(instance.user.id, filename)
