
#the function is expected to return an ınteger
#the functions accepts following parameters
#1. INTEGER ARRAY skills
#2. INTEGER minPlayers
#3. INTEGER minLevel
#4. INTEGER maxLevel

from itertools import combinations
def countTeams(skills,minplayers,minLevel,maxLevel):
    decision_list=[]
    for i in skills:
        if minLevel<=i<=maxLevel :
            decision_list.append(i)

        ####combination block##
    def comb_func(val1,i) :
        comb=combinations(decision_list, i)
        for i in list(comb):
                print(i)
    i=minplayers
    for i in range(minplayers,len(decision_list)+1,1) :
        comb_func(decision_list,i)

if __name__ == '__main__':
        ##Input block from user###
    skills = input("Enter a skill element separated by comma:")
    list_target  = skills.split(",")
    #string to integer operation
    list_target=map(int, list_target)
    list_target=list(list_target)

    minplayers=int(input("Enter a min player="))
    minlevel=int(input("Enter a min level="))
    maxlevel=int(input("Enter a max level = "))

    countTeams(list_target,minplayers,minlevel,maxlevel)