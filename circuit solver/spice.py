from sys import argv, exit
import numpy as np
import cmath
import math


#declaring constants for  startr stop conditions
CIRCUIT = '.circuit'
END = '.end'



ac_flag = 0

class Passive:
    def __init__(self,name,node1,node2,value,element):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        #if(element == 'R'):
        self.value = value
        self.element=element    

class IndependentSources():
    def __init__(self,name,node1,node2,value,element):
        self.name = name
        self.node1 = node1
        self.node2 = node2
        self.value = value
        self.element = element       

class Node:
    def __init__(self,name,index):
        self.name = name
        self.index = index
 
    
def value_draw(value):
    """""
    if('e'in value):
        val= value.split('e')
        ans= float(val[0])*pow(10,float(val[1]))
    else:
        """
    ans = float(value)    
    return ans
       



"""
It's a good practice to check if the user has given required and only the required inputs
Otherwise, show them the expected usage.
"""
if len(argv) != 2:
    print('\nUsage: %s <inputfile>' % argv[0])
    exit()

r_matx = np.array([])
v_matx = np.array([])
Nodal_R = np.array([])
Nodal_V = np.array([])
"""""        
The use might input a wrong file name by mistake.
In this case, the open function will throw an IOError.
Make sure you have taken care of it using try-catch
"""
try :
    with open(argv[1]) as f:
        
        lines = f.readlines()
        start = -1; end = -2
        for line in lines:              # extracting circuit definition start and end lines
            if CIRCUIT == line[:len(CIRCUIT)]:
                start = lines.index(line)
            elif END == line[:len(END)]:
                end = lines.index(line)
                break
            Ac_check = line.split()
            w=1
            if(Ac_check[0]== '.ac'):
                w = value_draw(float(Ac_check[2]))
                print("hi")
                w = w* 2*math.pi
                ac_flag=1
        if start >= end:                # validating circuit block
            print('Invalid circuit definition')
            exit(0)
        print(w)
       
       # r_val = np.array([])
        #v_val = np.array([])
         
        #lines.reverse()  # reversing order of lines in netlist
        for line in lines[start+1:end] :
            node = line.split()
            if "#" in node : # if comments are present , to neglect comments
               n=node.index('#')
               name = node[0]   # for analysing value, name and nodes
               value = node[n-1] 
               nodes = node[1:n-1]
               if( name[0] == 'R' or name[0] == 'C' or name[0] == 'L' ):
                   respass = Passive(name,nodes[0],nodes[1],value,node[0][0])
                   r_val = value_draw(respass.value)
                   r_matx =  np.append(r_matx,float(respass.value)) 
                   if(respass.node1 == 'GND'):
                            respass.node1 = 0
                   if(respass.node2 == 'GND'):
                            respass.node2 = 0  
                   n1 = int(respass.node1)
                   n2 = int(respass.node2)
                   if(n1 not in Nodal_R):
                            Nodal_R = np.append(Nodal_R,n1)
                           
                   if(n2 not in Nodal_R):
                            Nodal_R = np.append(Nodal_R,n2)  
               if('V' in name):
                   vsource = IndependentSources(name,nodes[0],nodes[1],value,node[0][0])
                   v_name = vsource.name               
                   #v_matx =  np.append(v_matx,float(vsource.value))
                   if(vsource.node1 == 'GND'):
                            vsource.node1 = 0
                   if(vsource.node2 == 'GND'):
                            vsource.node2 = 0  
                   n1 = int(vsource.node1)
                   n2 = int(vsource.node2)
                   
                  
                   Nodal_V = np.append(Nodal_V,v_name)


            
              
               
            else :
            
                 #out = ' '.join(reversed(node)) # printing in reverse order
                 #print(out)
                 name = node[0]
                 l = len(node)   
                 value = node[l-1]
                 nodes = node[1:l-1]

                 if(name[0] == 'R' or name[0] == 'C' or name[0] == 'L'):
                        respass = Passive(name,nodes[0],nodes[1],value,node[0][0])
                        r_val = respass.value
                        r_matx =  np.append(r_matx,float(respass.value)) 
                        if(respass.node1 == 'GND'):
                            respass.node1 = 0
                        if(respass.node2 == 'GND'):
                            respass.node2 = 0                            
                        n1 = int(respass.node1)
                        n2 = int(respass.node2)
                        if(n1 not in Nodal_R):
                            Nodal_R = np.append(Nodal_R,n1)
                           
                        if(n2 not in Nodal_R):
                            Nodal_R = np.append(Nodal_R,n2)
                       
 
                 if(name[0]=='V'):
                        vsource = IndependentSources(name,nodes[0],nodes[1],value,node[0][0])
                        v_name = vsource.name
                        #v_matx =  np.append(v_matx,float(vsource.value)) 
                        if(vsource.node1 == 'GND'):
                            vsource.node1 = 0
                        if(vsource.node2 == 'GND'):
                            vsource.node2 = 0 
                        n1 = int(vsource.node1)
                        n2 = int(vsource.node2)
                        
                        Nodal_V = np.append(Nodal_V,v_name)
                           
                        
                            
                       
           
                 
        print(Nodal_R)
        print(Nodal_V)   
        M = np.zeros((len(Nodal_R)-1+len(Nodal_V),len(Nodal_R)-1+len(Nodal_V)),dtype = "complex_")
        b = np.zeros(len(Nodal_R)+ len(Nodal_V)-1,dtype = "complex_") 
        k = len(Nodal_V)
        c=0
        A = len(Nodal_V)
        C=0


except IOError:
    print('Invalid file')


"""""
filling matrix
"""""


try :
    with open(argv[1]) as f:
        lines = f.readlines()
        start = -1; end = -2
        for line in lines:              # extracting circuit definition start and end lines
            if CIRCUIT == line[:len(CIRCUIT)]:
                start = lines.index(line)
            elif END == line[:len(END)]:
                end = lines.index(line)
                break
        if start >= end:                # validating circuit block
            print('Invalid circuit definition')
            exit(0)
        
       
       # r_val = np.array([])
        #v_val = np.array([])
         
        #lines.reverse()  # reversing order of lines in netlist
        for line in lines[start+1:end] :
            NoDe = line.split()
            if "#" in NoDe : # if comments are present , to neglect comments
               n=node.index('#')
               name = NoDe[0]   # for analysing value, name and nodes
               value = NoDe[n-1] 
               nodes = NoDe[1:n-1]
               respass1 = Passive(name,nodes[0],nodes[1],value,NoDe[0][0])
               print(name)
               if(name[0]=='R'):
                   R_Val = float(value)
                   #respass1 = Passive(name,nodes[0],nodes[1],value,NoDe[    R_Val = 
               elif(name[0]=='C'):

                  # respass1 = Passive(name,nodes[0],nodes[1],value,NoDe[    R_Val = 
                   R_Val = complex(0,-1/(w*R_Val))   #r_matx =  np.append(r_matx,float(respass.value)) 
               elif(name[0]== 'L'):   
                    R_Val = float(value)
                    R_Val = complex(0,(w*R_Val))

               if(respass1.node1 == 'GND'):
                        respass1.node1 = 0
               if(respass1.node2 == 'GND'):
                        respass1.node2 = 0  
               N1 = int(respass1.node1)
               N2 = int(respass1.node2)
                
               if(N1!=0 and N2!=0):
                    M[N1-1][N1-1] += 1/R_Val
                    print(R_Val)
                    M[N2-1][N2-1] += 1/R_Val
                    M[N1-1][N2-1] += -(1/R_Val)
                    M[N2-1][N1-1] += -(1/R_Val)

               if(N1==0):
                    M[N2-1][N2-1] += 1/R_Val
               if(N2==0):
                    M[N1-1][N1-1] += 1/R_Val


               
                
            
              
            
                           

                   
                    
               if(name[0]=='V'):
                   if(C==A):
                         break
                   if('ac' in NoDe):     
                        ac_val_split = NoDe.index('ac')
                        value = float(NoDe[ac_val_split +1])*complex(math.cos(float(NoDe[ac_val_split +2])),math.sin(float(NoDe[ac_val_split +2])))
                   if('dc' in NoDe):
                        dc_val_split = NoDe.index('dc')
                        value = float(NoDe[dc_val_split +1])
                   vsource1 = IndependentSources(name,nodes[0],nodes[1],value,NoDe[0][0])
                   V_Val = vsource1.value              
                  # v_matx =  np.append(v_matx,float(vsource.value))
                   if(vsource1.node1 == 'GND'):
                            vsource1.node1 = 0
                   if(vsource1.node2 == 'GND'):
                            vsource1.node2 = 0  
                   N1 = int(vsource1.node1)
                   N2 = int(vsource1.node2)

                   if(N1!=0 and N2!=0):
                       M[len(Nodal_R)+C-1][N1-1] = 1
                       M[len(Nodal_R)+C-1][N2-1] = -1
                       M[N1-1][len(Nodal_R)+C-1] = 1
                       M[N2-1][len(Nodal_R)+C-1] = -1
                       

                   if(N1==0):
                       M[len(Nodal_R)+C-1][N2-1] = 1
                       M[N2-1][len(Nodal_R)+C-1] =1
                       b[len(Nodal_R)+C-1] = v_matx[c]
                   if(N2==0):
                       M[len(Nodal_R)+C-1][N1-1] = 1
                       M[N1-1][len(Nodal_R)+C-1] =1
                       b[len(Nodal_R)+C-1] = v_matx[c]
                   C=C+1

            
              
             
            else :
            
                 #out = ' '.join(reversed(node)) # printing in reverse order
                 #print(out)
                 name = NoDe[0]
                 print(NoDe[0][0])
                 print(name[0])
                 l = len(NoDe)   
                 value = NoDe[l-1]
                 nodes = NoDe[1:l-1]

                 respass1 = Passive(name,nodes[0],nodes[1],value,NoDe[0][0])
                 R_Val = 1
                 print("R_Val =", R_Val)
               
                 if(name[0]=='R'):
                        
                        #respass1 = Passive(name,nodes[0],nodes[1],value,NoDe[0][0])
                        R_Val = float(value)
                 elif(name[0]=='C'):

                        # respass1 = Passive(name,nodes[0],nodes[1],value,NoDe[0][0])
                        R_Val = float(value)
                        R_Val = complex(0,-1/(w*R_Val)) 
                        print(R_Val)  #r_matx =  np.append(r_matx,float(respass.value)) 
                 elif(name[0]=='L'):   
                        R_Val = float(value) 
                        R_Val = complex(0,(w*R_Val))
                        print(R_Val) 

                 if(respass1.node1 == 'GND'):
                                respass1.node1 = 0
                 if(respass1.node2 == 'GND'):
                                respass1.node2 = 0  
                 N1 = int(respass1.node1)
                 N2 = int(respass1.node2)
                        
                 if(N1!=0 and N2!=0):
                            M[N1-1][N1-1] += 1/R_Val
                            print(R_Val)
                            M[N2-1][N2-1] += 1/R_Val
                            M[N1-1][N2-1] += -(1/R_Val)
                            M[N2-1][N1-1] += -(1/R_Val)

                 if(N1==0):
                            M[N2-1][N2-1] += 1/R_Val
                 if(N2==0):
                            M[N1-1][N1-1] += 1/R_Val

                        
                        
                 if(name[0]=='V'):
                   if(C==A):
                         break
                   if('ac' in NoDe):     
                        ac_val_split = NoDe.index('ac')
                        value = float(NoDe[ac_val_split +1])*complex(math.cos(float(NoDe[ac_val_split +2])),math.sin(float(NoDe[ac_val_split +2])))
                   if('dc' in NoDe):
                        dc_val_split = NoDe.index('dc')
                        value = float(NoDe[dc_val_split +1])
                   vsource1 = IndependentSources(name,nodes[0],nodes[1],value,NoDe[0][0])
                   V_Val = vsource1.value
                   value=value/2     ## Vpp/2 is amplitude              
                   v_matx =  np.append(v_matx,value)
                   if(vsource1.node1 == 'GND'):
                            vsource1.node1 = 0
                   if(vsource1.node2 == 'GND'):
                            vsource1.node2 = 0  
                   N1 = int(vsource1.node1)
                   N2 = int(vsource1.node2)

                   if(N1!=0 and N2!=0):
                       M[len(Nodal_R)+C-1][N1-1] = 1
                       M[len(Nodal_R)+C-1][N2-1] = -1
                       M[N1-1][len(Nodal_R)+C-1] = 1
                       M[N2-1][len(Nodal_R)+C-1] = -1
                       

                   if(N1==0):
                       M[len(Nodal_R)+C-1][N2-1] = 1
                       M[N2-1][len(Nodal_R)+C-1] = 1
                       b[len(Nodal_R)+C-1] = v_matx[c]
                   if(N2==0):
                       M[len(Nodal_R)+C-1][N1-1] = 1
                       M[N1-1][len(Nodal_R)+C-1] =1
                       b[len(Nodal_R)+C-1] = v_matx[c]
                   C=C+1

    print(M,"\n")
    print(b)
    X = np.linalg.solve(M,b)
    print(X)

            
              
               


except IOError:
    print('Invalid file')    
exit()
