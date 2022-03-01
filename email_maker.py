import math
import Databasehandler

def email1(st,file_name):
    f = open(file_name,'w')
    for i in range(1,201):
        f.write(st+'0'*(3-int(math.log10(i)))+str(i)+"@nitsikkim.ac.in\n")
def insert():
    f = open('keywithrewards1','r').readlines()
    for i in f:
        i = i.strip()
        Databasehandler.Insert_Email(i,1)

if __name__ == '__main__':
    pass