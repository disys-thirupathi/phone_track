import random
ap={}
class app_manager:
    def __init__(self):
        self.__n=eval(input("Number of apps "))
        
        if (type(self.__n) != int):
            raise ValueError("Invalid number")

        for i in range(self.__n):
            print("App #",i+1)
            self.__user_app = input("Enter app ")
            self.__app_size = int(input("App size "))
            self.__app_data = 0.30*self.__app_size
            ap[self.__user_app]= {}
            ap[self.__user_app]["app_size"]= self.__app_size
            ap[self.__user_app]["app_data"]= self.__app_data
        
        

    def userapp_val(self):
        if isinstance (self.__user_app,str):
            if len(self.__user_app)<= 12:
                print ("Apps Included")
        else:
            raise ValueError ("Enter the app which is available in playstore/ appstore")
        if isinstance (self.__app_size, int):
            print("Apps installed")
        elif len(str(self.__app_size)) == None:
            raise ValueError ("Invalid Size")
                

    def storage(self):
        display()
        print("Reset app data Y/N ")
        self.__in = input()
        
        if self.__in == "y":
            self.__in_ap = input("Enter app name to reset data")
            ap[self.__user_app]["app_data"] = 0
            display()
        else:
            pass
              
    def data_usage(self):
        for i,j in ap.items():
            ap[i]["int_usage"] = random.randint(10,99)
        display()
        
    def notification(self):
        print ("\nNumber of notifications")
        for i,j in ap.items():
            ap[i]["notification"] = random.randint(10,39)
        display()
        
    def permissions(self):
        self.__per=["Phone","contacts","storage"]
        for i,j in ap.items():
            ap[i]["permission"] = random.choice(self.__per)
        display()

def display():
    for i,k in ap.items():
                print("\n",i)
                print("----------\n")
                if type(k) is dict:
                    for j,l in k.items():
                        print(j,"\t---\t",l)
a=app_manager()
a.userapp_val()
a.storage()
a.data_usage()
a.notification()
a.permissions()
