#! /usr/bin/env bash

function bluer_algo_ai_agent_validate() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 1)
    local do_install=$(bluer_ai_option_int "$options" install 0)
    local do_play=$(bluer_ai_option_int "$options" play 1)
    local do_record=$(bluer_ai_option_int "$options" record 1)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)
    local filename=$(bluer_ai_option "$options" filename audio-$(bluer_ai_string_timestamp).wav)

    if [[ "$do_install" == 1 ]]; then
        brew install sox
    fi

    local object_name=$(bluer_ai_clarify_object $2 convo-$(bluer_ai_string_timestamp))

    filename=$ABCLI_OBJECT_ROOT/$object_name/$filename

    if [[ "$do_record" == 1 ]]; then
        bluer_ai_log "recording audio ... (^C to end)"

        bluer_ai_eval - \
            rec \
            -r 48000 \
            -c 1 \
            $filename
        [[ $? -ne 0 ]] && return 1
    fi

    if [[ "$do_play" == 1 ]]; then
        bluer_ai_eval - \
            afplay $filename
        [[ $? -ne 0 ]] && return 1
    fi

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name

    # https://docs.arvancloud.ir/fa/aiaas/api-usage
    curl --location "$BLUER_ALGO_AI_AGENT_ENDPOINT/audio/transcriptions" \
        --header "Authorization: apikey $BLUER_ALGO_AI_AGENT_API_KEY" \
        --form "model=whisper-1" \
        --form "file=@$filename" \
        --form "language=fa"
}
