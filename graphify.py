

class Graphiy():
    #contructor
    def __init__(self):
        self.data = []

    #add new element to the data set
    def newelem(self,element,children): #add parent as a str, children as a list
        #check if element already exists
        counter =0
        for n in self.data:
            if element == n['parent']:
                counter = counter+1
        if counter ==0:    
            self.data.append({'parent':element, 'children':children})
        else:
            self.newchildren(element, children)




    #add children to existing element
    def newchild(self,element,child): #add single children at time
        #check if element exists the update
        for n in self.data:
            if n['parent']==element:
                if child not in n['children']:
                    n['children'].append(child)
                else:
                    print('child exists')

    def newchildren(self,element,child):
        for n in self.data:
            if n['parent']==element:
                for m in child:
                    if m not in n['children']:
                        n['children'].append(m)
                    else:
                        print('This child already exists',m)

    #remove children from a existing element
    def removechild(self,element,child):
        for n in self.data:
            if n['parent']==element:
                n['children'].remove(child)

    #name all the children for an element
    def reportchildren(self,element):
        for n in self.data:
            if n['parent'] == element:
                print(self.data)
                print(n['children'])
                

if __name__=='__main__':
    Mygraph=Graphiy()
    element ='A'
    child = ['B','C','D']
    Mygraph.newelem(element,child)
    Mygraph.reportchildren(element)
    element ='A'
    child = 'D'
    Mygraph.newchild(element,child)
    Mygraph.newelem('B',['D','E'] )
    Mygraph.reportchildren('A')
