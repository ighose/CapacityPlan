import sys
from util.gcp_node_configs import *
import subprocess
import time


machine_zone_pairs = [('n1-standard-8','asia-east1-a'), ('n1-standard-4', 'asia-east1-a')]

for node_pair in machine_zone_pairs:
    node_type = node_pair[0]
    node_zone = node_pair[1]
    cluster_name = "sc-%s-%s-%s" %(node_type, node_zone, str(1))
    # subprocess.run('gcloud auth application-default login', shell=True)
    subprocess.run('gcloud container clusters create %s -m %s -z %s --num-nodes=%s' % (cluster_name, machine_types[2], zones[0], str(1)), shell=True)
    subprocess.run('gcloud container clusters get-credentials ' + cluster_name, shell=True)

    # Uncomment to test scaling while Apache HTTPD is running:
    # subprocess.run('kubectl run httpd-node --image=asia.gcr.io/my-project-1470428279137/httpd --port=8080', shell=True)
    # subprocess.run('kubectl get deployments && kubectl get pods', shell=True)
    # subprocess.run('kubectl expose deployment httpd-node --port=80 --target-port=80 --type="LoadBalancer"', shell=True)
    #
    # print("Waiting for Apache server to start...")
    # time.sleep(60)
    # response = subprocess.run('kubectl get services httpd-node', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    # external_ip = None
    # for line in response.stdout.split('\n'):
    #     if 'httpd-node' in line:
    #         external_ip = line.split()[2]
    #         break
    # if external_ip is None:
    #     print("ERROR: Deployment not exposed!")
    #     exit()

    start_time = time.time()
    proc = subprocess.check_call('gcloud container clusters resize %s -q --size 5' % cluster_name, shell=True)
    # proc.wait()
    print("Scaling 1 to 5 nodes: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    subprocess.check_call('gcloud container clusters resize %s -q --size 10' % cluster_name, shell=True)
    print("Scaling 1 to 10 nodes: --- %s seconds ---" % (time.time() - start_time))

    subprocess.Popen('gcloud container clusters delete -q %s' % cluster_name, shell=True)

