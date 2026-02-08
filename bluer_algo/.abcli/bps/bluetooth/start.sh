#! /usr/bin/env bash

function bluer_algo_bps_bluetooth_start() {
    local options=$1
    local verbose=$(bluer_ai_option_int "$options" verbose 0)
    local use_python=$(bluer_ai_option_int "$options" python 0)

    if [[ "$use_python" == 1 ]]; then
        python3 -m bluer_algo.bps.bluetooth \
            start \
            --verbose $verbose \
            "${@:2}"
        return
    fi

    bluer_ai_log "starting bluetooth..."

    if [[ "$abcli_is_rpi4" == true ]]; then
        bluer_ai_log "rpi4b detected."
        bluer_ai_eval - \
            sudo rfkill unblock bluetooth
        bluer_ai_eval - \
            sudo hciconfig hci0 up
    fi

    bluer_ai_eval - \
        sudo systemctl start bluetooth
    [[ $? -ne 0 ]] && return 1

    [[ "$verbose" == 1 ]] &&
        bluer_ai_eval - \
            sudo systemctl status \
            --no-pager bluetooth

    bluer_ai_eval - \
        sudo bluetoothctl power on
    [[ $? -ne 0 ]] && return 1

    bluer_ai_eval - \
        sudo bluetoothctl discoverable on
    [[ $? -ne 0 ]] && return 1

    [[ "$verbose" == 1 ]] &&
        bluer_ai_eval - \
            sudo bluetoothctl show

    return 0
}
