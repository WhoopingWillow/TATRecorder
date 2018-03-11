import os

q_List = {1:'What do I hate about this/myself?', 2:'What do I want to avoid about this/myself?', 3:'What makes me feel most like a victim about this/myself?', 4:'What makes me feel sad about this/myself?', 5:'What makes me feel isolated about this/myself?', 6:'What makes me angry about this/myself?', 7:'What are mean or critical voices saying to me about this/myself?', 8:'What do I worry about related to this/myself?', 9:'What’s overwhelming about this?'}
#print(q_List[1])
a_List = {}
y = 'x'
z = input("What is the topic?")
saved_File = open(r"C:\Users\Xeitz\Desktop\tat.txt", 'w')
saved_File.write(z)
saved_File.write("\n")

while (y.upper() != 'Y'):
    
    for items in q_List:
        #print(q_List[items])
        x = input(q_List[items])
        saved_File.write(q_List[items])
        saved_File.write("\n")
        saved_File.write(x)
        saved_File.write("\n")
        
##        a_List[items] = x
##
##    for items in q_List:
##        saved_File.write(q_List[items])
##        saved_File.write(a_List[items])

    y = input("done?")

saved_File.close()
