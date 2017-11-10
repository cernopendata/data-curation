#!/usr/bin/env python3

import hashlib
import os

print('fft_file_cache_info = {}')
print('')

for root, dirs, files in os.walk('/home/simko/Local/'
                                 'opendata.cern.ch-fft-file-cache'):
    for filename in files:
        file_path = os.path.join(root, filename)
        file_size = os.path.getsize(file_path)
        file_checksum = hashlib.sha1(open(file_path, 'rb').read()).hexdigest()
        print('fft_file_cache_info["%s"] = {"size": %s, "checksum": "%s"}' %
              (os.path.basename(file_path), file_size, file_checksum))
