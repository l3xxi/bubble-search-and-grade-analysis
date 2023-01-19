import sort
grades = {"English":[75,100],
    "Maths":[30,35],
    "Geography":[33,50],
    "History":[100,120],
    "Music":[77,80],
    "French":[77,80]
}
gradper = []
grad = []
a = tuple(grades.keys())

for i in range(len(grades)):
    b = a[i]
    #print(f"{b} : {round(grades[b][0]/grades[b][1]*100, 2)}%\n")
    gradper.append(round(grades[b][0]/grades[b][1]*100, 2))
    grad.append(b)

for _ in range(len(gradper)):    
    sort.loopy(gradper)

for i in range(len(gradper)):
    if gradper[i] == max(gradper):
        g = i
        break

for i in range(len(gradper)):
    if gradper[i] == min(gradper):
        h = i
        break

print(f"Highest grade:  {gradper[g]} -- {grad[g]}"+"\n"+f"Lowest grade:  {gradper[h]} -- {grad[h]}",end="\n\n")

for i in range(len(gradper)):
    print(grad[i], gradper[i], end=" | ")