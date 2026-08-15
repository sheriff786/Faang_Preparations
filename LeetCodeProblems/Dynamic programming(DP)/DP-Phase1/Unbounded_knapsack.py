'''
Unbunded Knapsack

diffrenece in 0-1 knapsack and unbounded knapsack

problems 

1)Rod cutting
2)coin change
3)coin change 2
4)maximum ribbon cut

unbounded take multiple occurances 

if i say no for 1 item then i say noit processed and if i say yes than we can take multiple occurances

diffrence in matrix wise 

diffrence in code wise

if(wt[i-1]<=j)
    t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
else:
    t[i]=t[i-1][j]
    
unbounded kanpsack

if(wt[i-1]<=j)
    t[i][j] = max(val[i-1]+t[i][j-wt[i-1]],t[i-1][j])
else:
    t[i]=t[i-1][j]


minor changes

'''

'''

Rod cutting

approach flow:
1.probem statements
2.marketing
3.How to identify 0-1 or unbounded
4.code variiation if any
'''




