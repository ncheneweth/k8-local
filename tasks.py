from invoke import task

@task
def init(ctx):
    # print('install CoreDNS')
    # ctx.run('bash ./dns/update_dns.sh | kubectl apply -f -')
    # ctx.run('kubectl delete --namespace=kube-system deployment kube-dns')

    print('apply metrics-server and heapster based hpa')
    ctx.run('kubectl apply -f metrics-server/')
    ctx.run('kubectl apply -f heapster/')

    print('deploy traefik ingress controller')
    ctx.run('kubectl apply -f ingress/')
    ctx.run('kubectl describe svc -n kube-system traefik-ingress-service')
    ctx.run('cat ingress/usage.txt')

    print('deploy kubernetes dashboard')
    ctx.run('kubectl apply -f dashboard/')

@task
def core(ctx):
    print('deploy observability tools')
    ctx.run('kubectl apply -f observe/namespaces.yaml') # defines the following: "monitoring"
    ctx.run('kubectl apply -f observe/elasticsearch/')
    ctx.run('kubectl apply -f observe/fluentd/')
    ctx.run('kubectl apply -f observe/kibana/')
    ctx.run('cat observe/usage.txt')

@task
def test(ctx):
    print('test')
