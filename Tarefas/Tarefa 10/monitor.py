import numpy as np


class Processo:
    def __init__(self, id):
        self.id = id
        self.received_heartbeat = False
        self.is_timedout = False

    def __eq__(self, p2):
        return self.id == p2.id

    def has_received_heartbeat(self):
        return self.received_heartbeat

    def receive_heartbeat(self, value):
        self.received_heartbeat = value

    def send_heartbeat(self, p):
        # Simulando que o processo 2 está falho
        if p.id != 2:
            p.received_heartbeat = True

    def has_timedout(self):
        return self.is_timedout


    def update_timeout(self):
        self.is_timedout = False


    def compute_timeout(self):
        pass



def main():
    suspeitos = np.empty(0, dtype = Processo)
    falhos = np.empty(0, dtype = np.int32)
    
    n_processos = 4

    '''
    Estamos simulando que, dos 4 processos, o de ID 2 está falho!
    '''

    for id in range(n_processos):
            suspeitos = np.append(suspeitos, Processo(id))


    for i in suspeitos:

        for j in suspeitos:
            j.received_heartbeat = False
            j.is_timedout = False


        for j in suspeitos:
            if i == j:
                continue

            j.compute_timeout()
            i.send_heartbeat(j)


            if j.has_received_heartbeat():
                j.update_timeout()
            else:
                j.is_timedout = True

            if j.has_timedout():
                falhos = np.append(falhos, j)


    for f in falhos:
        print(f"O processo {f.id} está falho!")

main()