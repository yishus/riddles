#!/bin/bash
docker build . -t google-ctf-2019 || exit
docker run -it --rm google-ctf-2019