#coding:utf-8
import numpy as np
# ____________________
#Création de la grande Matrice


M = np.array([[1,1,1,2,2,2,3,3,3],
[1,1,1,2,2,2,3,3,3],
[1,1,1,2,2,2,3,3,3],
[4,4,4,5,5,5,6,6,6],
[4,4,4,5,5,5,6,6,6],
[4,4,4,5,5,5,6,6,6],
[7,7,7,8,8,8,9,9,9],
[7,7,7,8,8,8,9,9,9],
[7,7,7,8,8,8,9,9,9]]) 

print(M[0,8])

## Décomposition en petite matrice
##################################
#def verif_case(posX, posY) :
#    if((posX ==  0 | posX == 1 | posX == 2) & (posY == 0 | posY == 1 | posY == 1 )):
#        m_1 = []                    
#        for i in range (0,3):                   
#            for j in range (0,3):                   
#                m_1.append(M[i,j])
#        for k in m_1:
#                if(k != k+1):
#                    
#
## MATRICE 1
#
#
## MATRICE 2
#m_2 = []                   
#for i in range (0,3):                  
#    for j in range (3,6):                  
#        m_2.append(M[i,j])
#
## MATRICE 3            
#m_3 = []                   
#for i in range (0,3):                  
#    for j in range (6,9):                  
#        m_3.append(M[i,j])                 
##################################
#
## MATRICE 4
#m_4 = []                   
#for i in range (3,6):                  
#    for j in range (0,3):                  
#        m_4.append(M[i,j])  
#
## MATRICE 5               
#m_5 = []                   
#for i in range (3,6):                  
#    for j in range (3,6):                  
#        m_5.append(M[i,j])
#
## MATRICE 6               
#m_6 = []                   
#for i in range (3,6):                  
#    for j in range (6,9):                  
#        m_6.append(M[i,j])                 
##################################
#m_7 = []                    
#for i in range (6,9):       
#    for j in range (0,3):   
#        m_7.append(M[i,j])  
#m_8 = []                    
#for i in range (6,9):       
#    for j in range (3,6):   
#        m_8.append(M[i,j])  
#m_9 = []                    
#for i in range (6,9):       
#    for j in range (6,9):   
#        m_9.append(M[i,j])  
##################################
#print(m_8)
