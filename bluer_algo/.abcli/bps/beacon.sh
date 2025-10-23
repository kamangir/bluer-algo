#! /usr/bin/env bash

function bluer_algo_bps_beacon() {
    bluer_ai_eval ,$1 \
        sudo -E \
        $(which python3) -m \
        bluer_algo.bps.utils.beacon \
        "${@:2}"
}
