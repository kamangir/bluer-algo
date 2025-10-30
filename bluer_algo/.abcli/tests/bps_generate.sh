#! /usr/bin/env bash

function test_bluer_algo_bps_generate() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_algo_bps generate - . \
        --sigma 1.0 \
        --x 0 \
        --y 0 \
        --z 0 "${@:2}"
    [[ $? -ne 0 ]] && return 1
    bluer_ai_hr

    bluer_ai_eval ,$options \
        bluer_algo_bps generate - . \
        --simulate 1 \
        --z 0 "${@:2}"
}
