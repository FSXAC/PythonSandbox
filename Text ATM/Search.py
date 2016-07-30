class SearchTools():
    """ this will contain all the functions about seaching """

    def __init__(self):
        """ constructor """

    def searchList(self, key, search_list):
        """ search fucntion using linear search algorithms """
        results = []
        for i in range(len(search_list)):
            if key in search_list[i]:
                results.append(search_list[i])
        return results

    def searchName(self, name, search_accounts):
        """ get names """
        results = []

        # get all names from the directories
        for account in search_accounts:
            if name in account.getName().lower():
                results.append(account.getAccNumber())

        return results
        
    def searchFor(self, key, search_list):
        """ search function that uses binary search algorithms """
        lower_bound = 0
        upper_bound = len(search_list) - 1
        position = -1
        while lower_bound <= upper_bound and not position != -1:
            search_pos = (lower_bound + upper_bound) // 2
            if search_list[search_pos] < key:
                lower_bound = search_pos + 1
            elif search_list[search_pos] > key:
                upper_bound = search_pos - 1
            else:
                position = search_pos

        return position
