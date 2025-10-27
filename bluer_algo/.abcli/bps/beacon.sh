#! /usr/bin/env bash

function bluer_algo_bps_beacon() {
    local options=$1
    local do_upload=$(bluer_ai_option_int "$options" upload 0)

    local object_name=$(bluer_ai_clarify_object $2 bps-beacon-$(bluer_ai_string_timestamp))

    bluer_ai_log "starting bps beacon -> $object_name ..."

    bluer_ai_eval ,$options \
        sudo -E \
        $(which python3) -m \
        bluer_algo.bps.utils.beacon \
        --object_name $object_name \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name

    return 0
}
