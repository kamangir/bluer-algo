#! /usr/bin/env bash

function bluer_algo_bps_loop_stop() {
    local options=$1
    local rpi=$(bluer_ai_option_int "$options" rpi 0)

    if [[ "$rpi" == 1 ]]; then
        local machine_name=$2
        if [[ -z "$machine_name" ]]; then
            bluer_ai_log_error "machine_name not found."
            return 1
        fi

        ssh \
            pi@$machine_name.local \
            "rm -v /home/pi/storage/temp/ignore/bps-lock"
        return
    fi

    rm -v $BPS_FILE_LOCK
}
