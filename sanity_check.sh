#!/bin/bash
rm -r github_data
python download_repo_text.py
rm "github_data/current_chunk_incomplete"
for  filename in github_data/*.jsonl.zst;
    do  
        echo $filename
        python check_sanity.py ${filename}
    done

for  filename in github_data/*.jsonl;
    do  
        echo $filename
        rm ${filename}
    done