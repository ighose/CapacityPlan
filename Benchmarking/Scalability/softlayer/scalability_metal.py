import sys
import subprocess
import time

subprocess.check_call('docker-machine create -d virtualbox --swarm --swarm-master '
                      '--swarm-discovery token://c2fee576fe7c22e0b297dcc91e05f656 --virtualbox-memory "512" '
                      '--virtualbox-cpu-count "1" swarm-agent-1Cx2G', shell=True)

start_time = time.time()
for i0 in range(5):
    subprocess.check_call('docker-machine create -d virtualbox --swarm --virtualbox-memory "512" '
                          '--swarm-discovery token://c2fee576fe7c22e0b297dcc91e05f656 swarm-agent%d-1Cx2G' % i0, shell=True)
print("Setup time for 5 nodes: --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
processes = list()

for i0 in range(4):
    processes.append(subprocess.Popen('sudo docker run -it httpd', shell=True))

for pr in processes:
    pr.wait()

print("Scaling time for 5 containers: --- %s seconds ---" % (time.time() - start_time))

for i0 in range(5):
    subprocess.check_call('docker-machine rm swarm-agent%d-1Cx2G' % i0)

start_time = time.time()
for i0 in range(10):
    subprocess.check_call('docker-machine create -d virtualbox --swarm --virtualbox-memory "512" '
                          '--swarm-discovery token://c2fee576fe7c22e0b297dcc91e05f656 swarm-agent%d-1Cx2G' % i0, shell=True)
print("Setup time for 10 nodes: --- %s seconds ---" % (time.time() - start_time))

for i0 in range(9):
    processes.append(subprocess.Popen('sudo docker run -it httpd', shell=True))

for pr in processes:
    pr.wait()

print("Scaling time for 10 containers: --- %s seconds ---" % (time.time() - start_time))

for i0 in range(10):
    subprocess.check_call('docker-machine rm swarm-agent%d-1Cx2G' % i0)