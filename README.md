# cloud-armor-demo

Minimal Flask app for testing a Cloud Armor + Cloud Run setup. Responds on `/` with:

```
hello, this site is serving on <cloud-run-service-name> cloudrun
```

The service name comes from Cloud Run's auto-injected `K_SERVICE` env var — no deploy-time
configuration needed.

## Local test

```bash
docker build -t cloud-armor-demo:local .
docker run --rm -p 8080:8080 -e K_SERVICE=cloud-armor-demo cloud-armor-demo:local
curl http://localhost:8080/
```
