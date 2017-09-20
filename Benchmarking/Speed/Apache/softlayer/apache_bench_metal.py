import subprocess
import time
from util.gcp_node_configs import *

# Memory Size in MB
mem_size = 512

# Number of CPU cores
cpu_count = 1

subprocess.check_call('docker-machine create -d virtualbox --swarm --swarm-master '
                      '--swarm-discovery token://c2fee576fe7c22e0b297dcc91e05f656 --virtualbox-memory "%d" '
                      '--virtualbox-cpu-count "%d" swarm-master' % (mem_size, cpu_count), shell=True)

subprocess.check_call('eval $(docker-machine env --swarm swarm-master)')

print("Waiting for Apache to start...")
time.sleep(10)
print("Requires achyudhk/apache container installed. Import the Linpack container from linpack.tar before running.")

ip_to_test = "127.0.0.1"
# Change concurrency based on requirement
concurrency = 10
for num_conn in [10, 100, 1000, 10000]:
    print("Benchmarking httpd server at %s with %d connections..." % (ip_to_test, num_conn))
    response = subprocess.Popen(['ab -n %d -c %d %s/' % (num_conn, concurrency, ip_to_test)],
                           shell=True, universal_newlines=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    response.wait()
    with open("data_apache/gcp_%d_%d_n%d_c%d.txt" % (cpu_count, mem_size, num_conn, concurrency), 'w') as txt_file:
        txt_file.write("".join(response.stdout.readlines()))

# Terminate master node
subprocess.check_call("docker-machine rm swarm-master")

