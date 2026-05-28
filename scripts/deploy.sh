```bash id="f5h0tz"
#!/bin/bash

echo "Starting deployment..."

cd /home/ubuntu/python-app

docker-compose down

docker-compose up -d --build

echo "Deployment completed."
```
