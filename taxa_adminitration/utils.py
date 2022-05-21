def get_lower_first_name_from(users):
    """
        transform first name in lower from users dict
    :param users:
    :return:
    """
    return users['first_name'].lower()


def get_sorted_users_list_by_first_name(users):
    """
        sorted users dict ny first Name.
    :param users:
    :type : list
    :return: users_list
    :rtype : list
    """

    # test the type
    if not isinstance(users, dict):
        raise TypeError("users is not a dict")

    if not len(dict):
        raise ValueError("dict is empty")

    users_sorted_list = sorted(users, key=get_sorted_users_list_by_first_name)

    return users_sorted_list


users_list = {

}
