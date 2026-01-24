#!/bin/sh

# Start the www app (port 3000)
echo "Starting www app on port 3000..."
cd /app/www && \
PORT=3000 HOSTNAME=0.0.0.0 node server.js 2>&1 | sed 's/^/[www] /' &

# Start the docs app (port 3001)
echo "Starting docs app on port 3001..."
cd /app/docs && \
PORT=3001 HOSTNAME=0.0.0.0 node server.js 2>&1 | sed 's/^/[docs] /' &

# Give apps a few seconds to start before Nginx
sleep 5

# Start Nginx
echo "Starting Nginx..."
nginx -g 'daemon off;'
