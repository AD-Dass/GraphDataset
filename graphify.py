

class Graphify():
    #contructor
    def __init__(self):
        self.data = []

    #add new node to the data set
    def newelem(self,node,children): #add parent as a str, children as a list
        #check if node already exists
        counter =0
        for n in self.data:
            if node == n['parent']:
                counter = counter+1
        if counter ==0:    
            self.data.append({'parent':node, 'children':children})
            
        else:
            self.newchildren(node, children)
        


    #add children to existing node
    def newchild(self,node,child): #add single children at time
        #check if node exists the update
        counter =0
        for n in self.data:
            if n['parent']==node:
                counter = counter + 1
                if child not in n['children']:
                    n['children'].append(child)
                else:
                    print('This child already exists')
        if counter ==0:
                print('Node does not exist')

    def newchildren(self,node,child):
        for n in self.data:
            if n['parent']==node:
                for m in child:
                    if m not in n['children']:
                        n['children'].append(m)
                    else:
                        print('This child already exists',m)

    #remove children from a existing node
    def removechild(self,node,child):
        for n in self.data:
            if n['parent']==node:
                n['children'].remove(child)

    #name all the children for an node
    def reportchildren(self,node):
        counter=0
        for n in self.data:
            if n['parent'] == node:
                output=n['children']
                print(output)
                counter = counter +1
        if counter ==0:
            print('Node does not exist or has no children ,', node)
            output = ''
        return output

    def nodedelete(self,node):
        counter =0
        for n in self.data:
            if n['parent'] == node:
                self.data.remove(n)
                counter = 1
        if counter == 0:
            print('Node does not exist', node)

if __name__=='__main__':
    Mygraph=Graphify()
    node ='A'
    child = ['B','C','D']
    Mygraph.newelem(node,child)
    Mygraph.reportchildren(node) # Result: be B C D
    node ='B'
    child = 'F'
    Mygraph.newchild(node,child) #Result: No node exists
    Mygraph.newelem('B',['D','E','F'] )
    Mygraph.reportchildren('B') #Result: D E F
    Mygraph.removechild('A','D')
    Mygraph.reportchildren('A') #Result: B C
    Mygraph.nodedelete('C') #Result: Node does not exist
    Mygraph.nodedelete('B')
    Mygraph.reportchildren('B') #Result: Node does not exist

#Things that could be improved.
#- Parse inputs so child (str) and children (list) are not mixed up
#- Add a new node in when it is first mentioned as a child. Would require multiple nested loops requiring significant computation time when scaled.
# -Add Delete Node 