#!/bin/bash


for i in "$@"; do
    if [[ $i == "gau" ]]; then
        echo $1 | gau -providers wayback | httpx -status-code -content-length -title -json -o $2/urls_wayback.json
    fi
    if [[ $i == "hakrawler" ]]; then
        hakrawler -plain -url $1 | httpx -status-code - content-length -title -json -o $2/urls_hakrawler.json
    fi
done

cat $2/urls* > $2/all_urls.json
rm -rf $2/urls*
