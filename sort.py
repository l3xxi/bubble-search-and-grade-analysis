import random
arnums = [5,100,44,5,6,1,55,7,100000,442,1]

# for i in range(random.randint(1,20)):
#     arnums.append(random.randint(0, 1000))



def loopy(listy: list):
    for i in range(1, len(listy)):
        if (listy[i-1]<listy[i]):
            listy[i], listy[i-1] = listy[i-1], listy[i]
    
try:
    print(f"Unsorted list: {arnums}")
    for _ in range(len(arnums)):
        loopy(arnums)
    print(f"sorted list: {arnums}")
except(TypeError):
    print("Not funny, stop that 😠")

#arnums[0] = arnums[1]
