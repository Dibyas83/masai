"""
search algorithm that expands the node  that is closest to the goal ,as estimated by a heuristic functon h(n) - a estimate taking h as input when coordinates are there of points
it is not always optimal

A* Search(a modification to greedy bfs)

search algorithm that expands node with lowest value of g(n) + h(n)
g(n) = cost to reach node
h(n) = estimated cost to goal
optimal if
- h(n) is admissible and consistent


-------------
Adversal search  -  in tic tac
find optimal + leading to future multi optimal sol + instead of finding optimal sol it will try to block anather to getting to optimal

1-minimax -three out comes x win -1,draw 0,y win 1
somebody trying to win somebody trying to draw

game functions

So init
player() whose turn one by one[xyxyxyxyx]
actions()  set of legal moves
result(s,a) returns state after action a taken
terminal() if draw or win, it has set of sol
utility(s)  1 0 or -1 output val

each player calculating own optimal and other pleyers next optimal move
will be like a tree and depth unlimited minmax

recursive process

func max-val(state): max player
  if terminal(state):
   return utility(state)

  v = -infinity
  for action in actions(state):
    v = max(v,min-value(result(state,action)))
  return v

func min-val(state): min player
  if terminal(state):
   return utility(state)

  v = infinity
  for action in actions(state):
    v = max(v,max-value(result(state,action)))
  return v

this gies huge result
                         u
possible-move    pm       pm   pm   pm   pm   pm   pm   pm
pm pm pm pm    pm pm pm
depth-limited minmax(optimized)
after certain amt of move i will stop
                         u
        pm          pm          pm
  pm  pm  pm     pm pm pm









"""









