#! /usr/bin/env bash

function bluer_algo_tracker_sandbox() {
    local options=$1
    local algo=$(bluer_ai_option "$options" algo camshift)

    local object_name="mean-cam-shift-data-v1"
    local url="https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4"
    local filename="$ABCLI_OBJECT_ROOT/$object_name/slow_traffic_small.mp4"

    local do_download=1
    [[ -f $filename ]] &&
        do_download=0
    do_download=$(bluer_ai_option_int "$options" download $do_download)

    if [[ "$do_download" == 1 ]]; then
        mkdir -pv $ABCLI_OBJECT_ROOT/$object_name
        bluer_ai_eval - \
            wget -O $filename $url -v
        [[ $? -ne 0 ]] && return 1
    fi

    bluer_ai_eval - \
        python3 $abcli_path_git/bluer-algo/sandbox/mean-cam-shift/$algo.py \
        $ABCLI_OBJECT_ROOT/$object_name/slow_traffic_small.mp4 \
        "${@:3}"
}
