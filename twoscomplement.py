# To import:
# from twoscomplement import *

def lars_reverse_twos_complement(j, bits=1):
   return (1<<j.bit_length()+bits) - j

def lars_twos_complement(j):
   return (1<<(j.bit_length()))-j

def build_twos_complement_down(j):
   origj=j
   prevj=0
   while prevj != j:
     print(f'{j:10d}, {prevj^j:10d}')
     prevj=j
     j=lars_twos_complement(j)

def build_reverse_twos_complement(vv):
  vv = list(reversed(vv))
  j = vv[0]
  for x in vv[1:]:
     j = lars_reverse_twos_complement(j, x)
  return j

def build_twos_complement_array(hm):
   vv = []
   j = hm
   while j != 1:
     prevhm = j
     j = lars_twos_complement(j)
     if j == prevhm:
        break
     count = 0
     tempj = j
     tempprevhm = prevhm
     prevtempj = tempj
     while tempj != tempprevhm:
        count+=1
        tempj = lars_reverse_twos_complement(prevtempj,count)
     vv.append(count)  
   vv.append(j)       
   return vv
