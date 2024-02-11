# functions-from-zero
live training

[![Python application test with Github Actions](https://github.com/mnbrshd/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/mnbrshd/functions-from-zero/actions/workflows/main.yml)


### To call Microservices

something like this
``` bash
curl -X 'POST' \
  'https://reimagined-carnival-jq59gw6v4pg2qr69-8000.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build container
`docker build .`
`docker image ls`

### Run container
Something like this

`docker run -p 127.0.0.1:8080:8080 153bccea264e`

### Invoke POST request
run `invoke.sh`