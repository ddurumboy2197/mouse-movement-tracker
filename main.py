import threading
import time
import random

class Server:
    def __init__(self, id):
        self.id = id
        self.busy = False

    def serve(self):
        self.busy = True
        print(f"Server {self.id} is serving...")
        time.sleep(random.randint(1, 3))
        self.busy = False
        print(f"Server {self.id} is free.")

class LoadBalancer:
    def __init__(self, num_servers):
        self.servers = [Server(i) for i in range(num_servers)]
        self.lock = threading.Lock()

    def get_server(self):
        with self.lock:
            for server in self.servers:
                if not server.busy:
                    return server
            return None

    def start_servers(self):
        threads = []
        for server in self.servers:
            thread = threading.Thread(target=server.serve)
            thread.daemon = True
            thread.start()
            threads.append(thread)
        return threads

    def test_load_balancer(self, num_requests):
        threads = []
        for _ in range(num_requests):
            server = self.get_server()
            if server:
                thread = threading.Thread(target=server.serve)
                thread.daemon = True
                thread.start()
                threads.append(thread)
            else:
                print("No available servers.")
        for thread in threads:
            thread.join()

load_balancer = LoadBalancer(5)
load_balancer.start_servers()
load_balancer.test_load_balancer(10)
```

Kodda quyidagilar mavjud:

- `Server` klassi: har bir serverni ifodalaydi, u faol yoki emasligini ko'rsatadi.
- `LoadBalancer` klassi: balanslovchi funksiyalarni ifodalaydi, jumladan serverlarni qidirish, serverlarni boshlash va test balanslovchini boshlash.
- `start_servers` metodi: har bir serverni boshlash uchun o'zaro bog'liq bo'lmagan threadlarni boshlaydi.
- `test_load_balancer` metodi: balanslovchi testini boshlash uchun threadlarni boshlaydi.
- `get_server` metodi: faol bo'lmagan serverni qidirib topadi.
- `serve` metodi: server faol bo'lish uchun boshlaydi.
