import sys
random_list =['a',0,2]

for entry in random_list:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Failure", sys.exc_info()[0], "occurred.")
        print("Next Entry.")
        print()
print("The reciprocal of", entry, "is", r)