player1=input()
player2=input()
while 1:
 if (player1=='rock' or player2=='scissor') or (player1=='scissors' or player2=='paper') or (player1=='paper' or player2=='rock'):
    print("player1 wins the game")
    break
 if (player1=='scissor' or player2=='rock') or (player1=='paper' or player2=='scissor') or (player1=='rock' or player2=='paper'):
    print("player2 wins the game")
    break
 if (player1=='scissor' or player2=='scissor') or (player1=='paper' or player2=='paper') or (player1=='rock' or player2=='rock'):
    print("draws")
    break