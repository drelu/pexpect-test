#!/bin/bash

for i in `seq 1 60`; do
    date | tee data-log.txt
    sleep 5
done