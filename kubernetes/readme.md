

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



1. kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.0.0" | kubectl apply -f -; }



# Create a root certificate and private key to sign the certificates for your service

mkdir evostack_certs1


openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj '/O=evostack Inc./CN=evostack.com' -keyout evostack_certs1/evostack.com.key -out evostack_certs1/evostack.com.crt

openssl req -out evostack_certs1/evostack.app.com.csr -newkey rsa:2048 -nodes -keyout evostack_certs1/evostack.app.com.key -subj "/CN=evostack.app.com/O=httpbin organization"

openssl x509 -req -sha256 -days 365 -CA evostack_certs1/evostack.com.crt -CAkey evostack_certs1/evostack.com.key -set_serial 0 -in evostack_certs1/evostack.app.com.csr -out evostack_certs1/evostack.app.com.crt


kubectl create -n istio-system secret tls httpbin-credential \
  --key=evostack_certs1/evostack.app.com.key \
  --cert=evostack_certs1/evostack.app.com.crt



curl -v -HHost:httpbin.example.com --resolve "httpbin.example.com:$SECURE_INGRESS_PORT:$INGRESS_HOST" \
  --cacert example_certs1/example.com.crt "https://httpbin.example.com:$SECURE_INGRESS_PORT/status/418"



curl -kv https://app-receiver.com/app-receiver --resolve "app-receiver.com:443:10.110.57.156"
curl -kv https://app-orchestrating.com/app-orchestrating --resolve "app-orchestrating.com:443:10.110.57.156"
curl -kv https://app-sender.com/app-sender --resolve "app-sender.com:443:10.110.57.156"



base64 -w0 evostack_certs1/evostack.app.com.crt
base64 -w0 evostack_certs1/evostack.app.com.key
