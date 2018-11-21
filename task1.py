import os #here we import os module
def getData(dir): # creating  afunction
    for x in os.listdir(dir):
        print(dir,"--",x) #printing the inside dir or files
        try:
           for y in os.listdir(os.path.join(dir,x)):
               print(x,"----",y)#printing the subfiles or subdir
        except:
            pass
dire=input("Enter any Diretcory name OR path")# path or dir name taking input
getData(dire)