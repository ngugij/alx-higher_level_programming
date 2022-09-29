#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_replace_element(elem):
        return(elem if elem != search else replace)
    return list(map(search_replace_element, my_list)
