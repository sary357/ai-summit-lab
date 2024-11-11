#!/bin/sh
#
curl --verbose  -H 'accept: application/json'   -H 'Content-Type: application/json'  -X POST http://localhost:8081/v1/exec_aws_lambda/ -d '{"codes":"code line 1\ncode line 2\n", "requirements_txt":"requests"}'
