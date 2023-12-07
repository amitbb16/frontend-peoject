#! /bin/bash -
if [[ ! -e /Scripts/file.txt ]]; then
    mkdir -p /Scripts
    touch /Scripts/file.txt
fi