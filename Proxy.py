import threading, queue, requests

test_link = "http://scholar.google.com/scholar?hl=en&q=info:MJ4i-QZfzPUJ:scholar.google.com/&output=cite&scirp=0&hl=en"

class Proxy(): 
    def _init_(self): 
        self.q = queue.Queue()
        self.valid_proxy = ""
        with open("proxy_list.txt", "r") as f: 
            proxies = f.read().split("\n")
            for p in proxies: 
                self.q.put(p) 
    
    def check_proxies(self): 
        while not self.q.empty(): 
            proxy = self.q.get()
            try: 
                res = requests.get(test_link, proxies={"http":proxy, "https":proxy})
            except: 
                continue
            if(res.status_code==200): 
                self.valid_proxy = proxy
                return
        print("check proxy" ,self.q )

    def get_proxy(self): 
        for _ in range(10): 
            threading.Thread(target=self.check_proxies).start()
        print("get proxy", self.q)
        return self.valid_proxy
    
if __name__=="__main__": 
    p = Proxy() 
    print(p.get_proxy())