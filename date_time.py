class data_time:
    def __init__(self,time:str):
        time = time.split()
        self.hour = time[1].split(":")[0]
        self.minute = time[1].split(":")[1]
        self.year = time[0].split(".")[2]
        self.data = time[0].split(".")[0]
        self.moth = time[0].split(".")[1]
        self.moths = {1:"Yanvar",2:"Fevral",3:"Mart",4:"Aprel",5:"may",6:"Iyun",7:"Iyul",8:"Avgust",9:"Sentabr",10:"oktabr",11:"Noyabr",12:"Dekabr"}

    def __str__(self):
        return(f"{self.get_moth(self.moth)} {self.get_year()} {self.get_hour()} {self.get_minute()}")


    def get_minute(self):
        if int(self.minute) == 1: 
            return f"{int(self.minute)} minute"
        else:
            return f"{int(self.minute)} minutes "
    
    def get_hour(self):
        if int(self.hour) == 1:
            return f"{int(self.hour)} hour"
        else:
            return f"{int(self.hour)} hours"
    
    def get_moth(self,moth):
        return f"{int(self.data)} {self.moths[int(moth)]}"
    
    def get_year(self):
        return f"{int(self.year)} year" 

if __name__ =="__main__":
    obj = data_time("19.09.2999 01:59")
    print(obj)