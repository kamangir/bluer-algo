#! /usr/bin/env bash

function bluer_algo_bps_loop_start() {
    if [[ -f "$BPS_FILE_LOCK" ]]; then
        bluer_ai_log_error "bps is locked, run \"@bps loop stop\" first."
        return 1
    fi

    bluer_ai_log "starting bps loop..."
    bluer_ai_log "locked" >$BPS_FILE_LOCK

    local options=$1
    local do_upload=$(bluer_ai_option_int "$options" upload 1)
    local do_simulate=$(bluer_ai_option_int "$options" simulate 1)

    local object_name=$(bluer_ai_clarify_object $2 bps-loop-$(bluer_ai_string_timestamp))

    while [[ -f "$BPS_FILE_LOCK" ]]; do
        bluer_algo_bps_beacon - \
            $object_name \
            --timeout $BLUER_AI_BPS_LOOP_BEACON_LENGTH \
            --simulate $do_simulate
        [[ $? -ne 0 ]] && return 1
        bluer_ai_hr

        [[ ! -f "$BPS_FILE_LOCK" ]] &&
            return 0

        local receiver_timeout=$(bluer_ai_string_random \
            --int 1 \
            --min $BLUER_AI_BPS_LOOP_RECEIVER_LENGTH_MIN \
            --max $BLUER_AI_BPS_LOOP_RECEIVER_LENGTH_MAX)
        bluer_ai_log "receiver timeout: $receiver_timeout s"

        @bps receiver - \
            $object_name \
            --grep $BLUER_AI_BPS_LOOP_GREP \
            --timeout $receiver_timeout
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    done
    bluer_ai_log "stop received."

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name

    return 0
}
