player1=input()
player2=input()
user1=input()
user2=input()
while 1:
 if (user1=='Rock' and user2=='Scissor') or (user1=='Scissors' and user2=='Paper') or (user1=='Paper' and user2=='Rock'):
    print(player1,"win")
    break
 if (user1=='Scissor' and user2=='Rock') or (user1=='Paper' and user2=='Scissor') or (user1=='Rock' and user2=='Paper'):
    print(player2,"win")
    break