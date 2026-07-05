def pathwithmaxscore(board):

    n=len(board)
    MOD=10**9+7

    #dp_score will track the maximum path score
    dp_score=[[-float('inf')]*(n+1) for _ in range(n+1)]

    #dp_paths: tracking of number of paths that reaches to maximum score
    dp_paths=[[0]*(n+1) for _ in range(n+1)]

    #basecase: Bottom right cell ('s)

    dp_score[n-1][n-1]=0
    dp_paths[n-1][n-1]=1

    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):

            # if there is any obstacle or if we are at the starting position

            if board[i][j]=='X' or (i==n-1 and j==n-1):
                continue

            # find the maximum score between three choices i.e max_prev_score

            max_prev_score=max(dp_score[i+1][j],dp_score[i+1][j+1],dp_score[i][j+1])

            # if the max_prev_score is -inf then skip that position

            if max_prev_score!=-float('inf'):

                val=0 if board[i][j] in 'SE' else int(board[i][j])

                dp_score[i][j]=max_prev_score+val


                # those previous states giving max_prev_score add those paths

                if dp_score[i+1][j]==max_prev_score:
                    dp_paths[i][j]=(dp_paths[i][j]+dp_paths[i+1][j])%MOD
                
                if dp_score[i][j+1]==max_prev_score:
                    dp_paths[i][j]=(dp_paths[i][j]+dp_paths[i][j+1])%MOD
                
                if dp_score[i+1][j+1]==max_prev_score:
                    dp_paths[i][j]=(dp_paths[i][j]+dp_paths[i+1][j+1])%MOD

    if dp_paths[0][0]==0:
        return [0,0]
   
    return [dp_score[0][0],dp_paths[0][0]]

board = ["E23","2X2","12S"]
print(pathwithmaxscore(board))