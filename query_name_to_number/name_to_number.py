
def check_name_queries(name_number_dict, name_queries):
    found = False
    
    for name_q in name_queries:
        for name_d in name_number_dict:
            if name_q == name_d:
                print("{0}={1}".format(name_q, name_number_dict[name_q]))
                found = True
                break
        if not found:
            print("Not found")
        else:
            found = False
        
            

if __name__ == '__main__':
    name_number = dict()
    n = int(input())
    
    # Get the names and numbers and assign them to the dictionary
    for x in range(n):
        # Separates the two space separated values into name and phone number
        name, phone_number = input().split()
        name_number[name] = phone_number  
    
    name_queries = list()
    try:
        while True:
            name = input()
            if name != "":
                name_queries.append(name)
            else:
                break
    except EOFError:
        pass
    
    check_name_queries(name_number, name_queries)
        
        