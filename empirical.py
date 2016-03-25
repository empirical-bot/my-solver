
import zerorpc
import os

localhost = 'tcp://0.0.0.0:4242'
solver_host = 'tcp://solver:4242'

def run(solver):
    server = zerorpc.Server(solver)
    server.bind(localhost)
    print "Empirical: Solver is now running"
    server.run()

def Solver():
    client = zerorpc.Client()
    client.connect(solver_host)
    return client

def postResults(results):
    import requests
    endpoint = os.getenv('EMPIRICAL_API_URL', 'http://empiricaldev.localtunnel.me/api/x')
    # TODO: Get API_CREDENTIALS
    EXPERIMENT_ID = str(os.getenv('EXPERIMENT_ID'))
    endpoint = endpoint + '/' + EXPERIMENT_ID
    print "Endpoint:", endpoint
    print "Results:", results
    requests.patch(endpoint, json=results)
