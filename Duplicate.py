names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
duplicated_names = []

def locate_duplicates(names):
    for name in names:
        if names.count(name) > 1: 
            if name in duplicated_names: 
                pass
            else: 
                duplicated_names.append(name)
                duplicatesFound = True

    return duplicatesFound

# delete Duplicated names
def delete_duplicates(names,duplicated_names):
    for name in duplicated_names:
        names.remove(name)
        

