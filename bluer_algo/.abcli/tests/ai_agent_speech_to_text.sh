#! /usr/bin/env bash

function test_bluer_algo_ai_agent_speech_to_text() {
    local options=$1

    bluer_ai_eval ,$options \
        bluer_algo_ai_agent_speech_to_text_validate \
        download,filename=farsi.wav,language=fa,verbose \
        $BLUER_ALGO_AI_AGENT_S2T_TEST_OBJECT
    [[ $? -ne 0 ]] && return 1
    bluer_ai_hr

    bluer_ai_eval ,$options \
        bluer_algo_ai_agent_speech_to_text_validate \
        download,filename=english.wav,language=env,verbose \
        $BLUER_ALGO_AI_AGENT_S2T_TEST_OBJECT
}
