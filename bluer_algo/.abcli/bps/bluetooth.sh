#! /usr/bin/env bash

function bluer_algo_bps_bluetooth() {
    local task=${1:-timing}

    local function_name=bluer_algo_bps_bluetooth_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m bluet_algo.bps.bluetooth "$@"
}

bluer_ai_source_caller_suffix_path /bluetooth
