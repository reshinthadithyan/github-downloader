import os
import json
import uuid
import zstandard
import subprocess
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file_name",type=str)

args = parser.parse_args()

def loadJsonL(fname):
    import json

    data = []
    with open(fname) as fp:
        for line in fp.readlines():
            data.append(json.loads(line))
    return data


def checkZSTLink(url):
    zstfile = url
    jsonlfile = zstfile[:-4]    
    with open(zstfile, 'rb') as compressed:
        decomp = zstandard.ZstdDecompressor()
        with open(jsonlfile, 'wb') as destination:
            decomp.copy_stream(compressed, destination)
    data = loadJsonL(jsonlfile)
    check_data = []
    for row in data:
        file_name = row['meta']['file_name']
        check_data.append(file_name)
    if len(check_data) != 0:
        assert len(list(set(check_data))) != len(check_data)
    print("PASS")

checkZSTLink(args.file_name)
#checkZSTLink(r"github_data/data_0_time1635098409_default.jsonl.zst")