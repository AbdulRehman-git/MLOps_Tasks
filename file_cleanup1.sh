#!/bin/bash

if [ ! -d "/tmp/old_files" ]; then
    mkdir /tmp/old_files
fi

mv /tmp/*.log /tmp/old_files/

echo "$(date '+%Y-%m-%d %H:%M:%S') - Moved .log files to /tmp/old_files" >> /var/log/file_cleanup.log

