

## dowload istio 
1. `curl -L https://istio.io/downloadIstio | sh -`
2. `cd istio-1.20.1`
3. `export PATH=$PWD/bin:$PATH`
4. `istioctl install --set profile=demo -y`
5. `kubectl create namespace product`
6. `kubectl label namespace product istio-injection=enabled`
7. `kubectl config set-context --current --namespace=product`

export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT

echo "$GATEWAY_URL"
echo "$SECURE_INGRESS_PORT"
echo "$INGRESS_PORT"
echo "$ INGRESS_HOST"

## to get istio ip
1. `kubectl get svc -n istio-system istio-ingressgateway`

criar tres servicos
e acessos externamente
o servico 1 se comunica com o servico 2 e o servico 2 se comunica com o servico 3
both services has prometheus setting
servico 3 return "hello world servico 3"
servico 1 retain log save "i am servivo 1"
servico 2 return "hello world servico 2"
servico 2 retain log save "i am servivo 2"
servico 1 return "hello world servico 1"
servico 3 retain log save "i am servivo 3"
log de pod should be clear logs from last 24 hs