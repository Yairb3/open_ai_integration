#!/usr/bin/env bash

host_port="$1"
shift
cmd="$@"

host=$(echo $host_port | cut -d : -f 1)
port=$(echo $host_port | cut -d : -f 2)

until nc -z -v -w30 $host $port; do
  echo "Waiting for $host:$port to be ready..."
  sleep 1
done

exec $cmd
