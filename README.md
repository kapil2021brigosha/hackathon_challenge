# Hackathon_challenge 


![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)   


# Question 1: 

1.THE PERFECT TEAM

The School of Languagaes and Science teaches five subjects:Physics,Chemistry,Math,Botany, and Zoology, Each student is skilled in one subject.The skills of the students are described by string of named skills that consists of the letters p,c,m,b, and z only.Each character describes the skill of a student.
 
  Given a list of students'skills, determine the total number of diffrent teams satisfying the following constraints:
 A team consits of a group of exactly five students.
 Each student is skilled in a different subject.
 A student may only be on one team.  
 
  EXAMPLE 1
 skills=pcmbzpcmbz
  
  There are 2 possible teams that can be formed at one time:[0-4]=pcmbz and skills[5-9]=pcmbz for example.

  EXAMPLE 2
 skills=mppzbmbpzcbmpbmczcz

The sorted string is bbbbcccmmmmppppzzzz. All of the skills are represented, but there are only 3 students skilled in Chemistry. Only 3 teams can be created.

  Function Description
 Complete the function differentTeams in the editor below. The function must return an integer value representing the number of teams that can be formed given the constraints.

differentTeams has the following parameter(s):
     string skills: a string of length where each position represents the skill of  a student. 

# Question 2: 

Fc Codelona is trying to assemble a team from a roster of avilable players.they have a minimum number of players they want to sign and each player needst ot have a skill rating within a certain range.Given a list of players skill levels with desired upper and lower bounds,determine how many teams can be created from the list. 

Example: 
skills=[12,46,13,5,10] 

minPlayers=3 

minLevel=4 

maxLevel=10 

The list includes players with skilll levels 
[12,4,6,13,5,10] 

They want to hire at least 3 players with the skill levels.beetween 4 and 10 inclusive. 

Four the players with the following skill levels {4,6,5,10} meet criteria. 

There are 5 ways to form a team of at least 3 players : {4,5,6} ,{4,6,10},{4,5,10},{5,6,10} and { 4,5,6,10} 

Return 5.


