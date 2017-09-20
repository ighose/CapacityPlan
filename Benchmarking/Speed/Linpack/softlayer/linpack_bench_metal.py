import subprocess
import time

# Memory Size in MB
mem_size = 512

# Number of CPU cores
cpu_count = 1

subprocess.check_call('docker-machine create -d virtualbox --swarm --swarm-master '
                      '--swarm-discovery token://c2fee576fe7c22e0b297dcc91e05f656 --virtualbox-memory "%d" '
                      '--virtualbox-cpu-count "%d" swarm-master' % (mem_size, cpu_count), shell=True)

subprocess.check_call('eval $(docker-machine env --swarm swarm-master)')
subprocess.check_call('docker run -it achyudhk/linpack')

print("Waiting for Linpack benchmark to execute...")
time.sleep(300)
print("Requires achyudhk/linpack container installed. Import the Linpack container from linpack.tar before running.")

cmd_to_exec = "'docker logs $(docker ps -l -q)'"
response = subprocess.Popen([cmd_to_exec],
                       shell=True, universal_newlines=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

with open("mwtal_%d_%d.txt" % (cpu_count, mem_size), 'w') as txt_file:
    txt_file.write("".join(response.stdout.readlines()))

# Terminate master node
subprocess.check_call("docker-machine rm swarm-master")