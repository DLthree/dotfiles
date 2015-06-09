#!/bin/sh

emacsclient -n "$@"
if [ "$?" = "1" ]; then
   emacsclient -c -n -a "" "$@"
fi