
def minimax(depth,node,ismax,alpha,beta,values):
    if depth ==2:
        return values[node]
    
    if ismax:
        
        best=-999
        
        for i in range(2):
            val = minimax(depth+1,node*2+i,False,alpha,beta,values)
            
            best=max(best,val)
            alpha=max(alpha,best)
            
            if alpha>=beta:
                break
        return best
            
    
    else:
        best = 999
        for i in range(2):
            val = minimax(depth+1,node*2+i,True,alpha,beta,values)
            
            best=min(best,val)
            beta=min(beta,best)

            if alpha>=beta:
                break
        return best
values = [1, 5, 2, 9]

answer = minimax(0, 0, True, -999, 999, values)

print("Best value:", answer)





        
    