#! /usr/bin/env bash

function bluer_algo_ai_agent_speech_to_text() {
    local task=$1

    local function_name=bluer_algo_ai_agent_speech_to_text_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m bluer_algo.ai_agent.speech_to_text "$@"
}

bluer_ai_source_caller_suffix_path /speech_to_text
