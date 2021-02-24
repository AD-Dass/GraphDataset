

class Graphiy():
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
        for n in self.data:
            if n['parent']==node:
                if child not in n['children']:
                    n['children'].append(child)
                else:
                    print('child exists')

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
        for n in self.data:
            if n['parent'] == node:
                print(self.data)
                print(n['children'])
                

if __name__=='__main__':
    Mygraph=Graphiy()
    node ='A'
    child = ['B','C','D']
    Mygraph.newelem(node,child)
    Mygraph.reportchildren(node)
    node ='A'
    child = 'D'
    Mygraph.newchild(node,child)
    Mygraph.newelem('B',['D','E'] )
    Mygraph.reportchildren('A')
