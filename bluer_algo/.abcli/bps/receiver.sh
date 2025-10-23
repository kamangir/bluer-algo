#! /usr/bin/env bash

function bluer_algo_bps_receiver() {
    local options=$1
    local use_python=$(bluer_ai_option_int "$options" python 1)

    if [[ "$use_python" == 1 ]]; then
        sudo -E \
            $(which python) -m \
            bluer_algo.bps.utils.receiver \
            "${@:2}"

    else
        bluer_ai_eval ,$options \
            sudo \
            hcitool \
            lescan \
            "${@:2}"
    fi
}
