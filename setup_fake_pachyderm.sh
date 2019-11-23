#!/usr/bin/env bash

mkdir -p /pfs/texts
cp ./data/* /pfs/texts

python split_text.py
/bin/bash


