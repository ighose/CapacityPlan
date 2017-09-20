

# Cluster Deletion Request - API Authentication Required
# response_obj = requests.delete('https://container.googleapis.com/v1/projects/my-project-1470428279137/zones/asia-northeast1-a/clusters/whetstone-bench?fields=detail%2Cname%2CoperationType%2CselfLink%2Cstatus%2CstatusMessage%2CtargetLink%2Czone&key={AIzaSyBohgTxwmOpRZ0JdTzPBqYMVx_IYAR-2K4}')

# Cluster Creation Request - API Authentication Required
# response_obj = requests.post('https://container.googleapis.com/v1/projects/my-project-1470428279137/zones/asia-northeast1-a/clusters?fields=detail%2CselfLink%2CtargetLink&key={AIzaSyBohgTxwmOpRZ0JdTzPBqYMVx_IYAR-2K4}',
#               data={
#                     "cluster": {
#                         "initialNodeCount": 1,
#                         "nodeConfig": {
#                             "machineType": "n1-standard-1",
#                             "diskSizeGb": 10
#                         },
#                         "name": cluster_name
#                     }
#               })
# print("Insertion Response:\n", response_obj)