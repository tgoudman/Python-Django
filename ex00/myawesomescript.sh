#!/bin/sh

echo $1
curl -X GET $1 | grep body | cut -d'"' -f2