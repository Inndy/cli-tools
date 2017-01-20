#!/usr/bin/env python3

import glob
import hashlib
import logging
import os
import sys

logging.basicConfig(level=logging.INFO, stream=sys.stderr)

def hashfile(f):
    logging.getLogger('hashfile').info('Calculate hash for file %s' % f)
    h = hashlib.md5()
    with open(f, 'rb') as fin:
        while True:
            block = fin.read(1048576)
            if not block:
                break
            h.update(block)
    return h.hexdigest()

def find_dups_in(base, target):
    logger = logging.getLogger('find_dups_in')

    h_base = {}
    h_target = {}

    for directory, store in ((base, h_base), (target, h_target)):
        logger.info('Walking directory %s' % directory)
        for f in glob.iglob(directory + '/**', recursive=True):
            if os.path.isfile(f):
                store[f] = hashfile(f)

    h_base_inv = { v: k for k, v in h_base.items() }
    h_base_set = set(h_base_inv)

    for f, h in h_target.items():
        if h in h_base_set:
            yield (f, h_base_inv[h])

def main():
    try:
        base, target = sys.argv[1:1+2]
    except ValueError:
        print('Usage: %s base/dir target/dir' % sys.argv[0])
        return

    for f, dup_f in find_dups_in(base, target):
        print(f)

if __name__ == '__main__':
    main()
