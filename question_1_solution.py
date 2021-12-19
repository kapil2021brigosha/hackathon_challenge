import re
def perfectTeam(skills):
    sortedskills = ''.join(sorted(skills))
    count_list = []
    decision_list=["p","c","m","b","z"] #decision skills
    for i,val in enumerate(decision_list):
        count_list.append(len(re.findall(decision_list[i],sortedskills)))
    #letter-count dictionary
    res = {decision_list[i]: count_list[i] for i in range(len(decision_list))}
    print("Letter dictionary is : " + str(res))
    for j in count_list :
        if j == 0 :
            return 0
            break
    if all(x > 0 for x in count_list) :
       result=min((count_list))
       return result

if __name__=='__main__':
    my_string=input("Enter a string = ")
    print("You can create {} team(s)" .format(perfectTeam(my_string)))