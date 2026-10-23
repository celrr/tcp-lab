#!/usr/bin/env bash
# Uso: ./link.sh on [retardo] [pérdida]   |   ./link.sh off
set -e
cd "$(dirname "$0")"
if [ "$1" = "off" ]; then
  docker compose exec sender tc qdisc del dev eth0 root || true
  echo "Enlace limpio"
else
  DELAY=${2:-100ms}; LOSS=${3:-5%}
  docker compose exec sender tc qdisc replace dev eth0 root netem delay "$DELAY" loss "$LOSS"
  echo "Enlace: retardo $DELAY, pérdida $LOSS"
fi
docker compose exec sender tc qdisc show dev eth0
