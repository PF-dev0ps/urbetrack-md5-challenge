#!/usr/bin/env bash
set -euo pipefail

URL="http://localhost:8080/health"

while true; do
  if curl -fsS "$URL" >/dev/null; then
    echo "$(date '+%Y-%m-%d %H:%M:%S') OK - $URL"
  else
    echo "$(date '+%Y-%m-%d %H:%M:%S') ERROR - $URL"
  fi

  sleep 5
done
