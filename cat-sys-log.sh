#!/bin/bash

if [ $# -le 0 ]; then
    echo "usage: $0 [path] file-prefix.log" >&2
    echo "" >&2
    echo "  example: $0 /var/log auth.log"
    exit 1
elif [ $# -eq 1 ]; then
    log_path=.
    name="$1"
elif [ $# -eq 2 ];then
    log_path="$1"
    name="$2"
else
    echo "Too more arguments" >&2
    exit 2
fi

echo "log_path=$log_path"
echo "name=$name"

for log in $(ls $log_path -t | grep -e "^$name"); do
    log="${log_path}/${log}"
    if [ "${log: -3}" = ".gz" ]; then
        gzip -d --stdout $log
    else
        cat $log
    fi
done
