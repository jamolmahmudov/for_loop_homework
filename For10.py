def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    a=[]
    for i in list1:
        i=i.title()
        a.append(i)
    return a
print(main(['zufar','bobur','lochin']))