import graphviz
A="{0,1,2,3}"
R="{ (0,0), (0,1), (0,3), (1,0), (1,1), (2,2), (3,0), (3,3) }" 
AElements=[]
countRef=0
countSym=0
firstElement=0
secondElement=0
symmetryValues=[]
transitiveValues=[]
def getAElements():
    for s in A:
        if s.isdigit():
            AElements.append(s)
    

def analyze():
    c=0
    while c < len(R):
        if R[c] in AElements:
            firstElement=R[c]
            secondElement=R[c+2]
            CheckReflexive(firstElement,secondElement)
            checkSymmetry(firstElement,secondElement)
            checkTransitive(firstElement,secondElement)
            c=c+3
        elif R[c] == '}':
            c=len(R)+1
        else:
            c+=1
def CheckReflexive(f,s):
    if f==s:
       global countRef
       countRef+=1
def printRef():
    if countRef == len(AElements):
        print("R is reflexive")
    else:
        print("R is not reflexive")
def checkSymmetry(f,s):
    if not f==s:
        var =str(f+s)
       
        if var in symmetryValues:
            
            global countSym
            countSym+=1
        else:
            var =str(s+f)
            
            symmetryValues.append(var)
def printSym():
    if countSym==len(symmetryValues):
        print("R is Symetric")
    else:
        print("R is not Symetric")
def checkTransitive(f,s):
    if not f==s:
        var = str(f+s)
        transitiveValues.append(var)
def printTransitive():
    var1=transitiveValues[0]
    var2=transitiveValues[1]
    newVar=str(var1[1]+var2[1])
    if newVar in transitiveValues:
        print("R is transitive" )
    else:
        print("R is not transitive")
def graphAutomat():
    Graph = {"0":["0","1","3"],"1":["0","1"], "2":["2"], "3":["0","3"] }
    g = graphviz.Digraph('G',filename='hello.gv')
    for node in Graph:
        for edge in Graph[node]:
            g.edge(node,edge)
    g.view()
getAElements()
analyze()
printRef()
printSym()
printTransitive()
graphAutomat()