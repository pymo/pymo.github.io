#!/bin/bash
python3 generate_index.py 
mv index_real.html ../
cd ..
chown nslab:nslab -R ./*
chmod 755 -R ./*
service nginx restart
