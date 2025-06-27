#! /usr/bin/env bash

function bluer_algo_image_classifier_ingest() {
    local options=$1
    local do_clone=$(bluer_ai_option_int "$options" clone 0)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)

    local object_name=$(bluer_ai_clarify_object $2 image_classifier_ingest-$(bluer_ai_string_timestamp))

    [[ "$do_clone" == 1 ]] &&
        bluer_ai_git_clone \
            https://github.com/fruits-360/fruits-360-100x100.git

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_algo.image_classifier \
        ingest \
        --object_name $object_name \
        "${@:3}"
    [[ $? -ne 0 ]] && return 1

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - $object_name
}
