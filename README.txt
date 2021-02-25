Graph Data Set Creator
Input Nodes and child/children as <str> and <str>/<list>.

newelem(node,children)
  create a new node as a <str> e.g 'A' with children as <list> e.g [],['B','C','D']
  
newchild(node, child)
  Add single child as a <str>. e.g newchild('A','E').

newchildren(node, children)
  Add multiple children as a <list> e.g newchildren('A',['E','F','G'])

removechild(node, child)
  Remove a child <str> from a node. e.g removechild('A','G')

nodedelete(node)
  Delete entire node and children. e.g removechild('A')

reportchildren(node)
  retrieve list of children for specified node. e.g result = reportchildren('A'), output = [] 
