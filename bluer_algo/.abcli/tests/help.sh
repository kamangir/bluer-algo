#! /usr/bin/env bash

function test_bluer_algo_help() {
    local options=$1

    local module
    for module in \
        "@algo" \
        \
        "@algo pypi" \
        "@algo pypi browse" \
        "@algo pypi build" \
        "@algo pypi install" \
        \
        "@algo pytest" \
        \
        "@algo test" \
        "@algo test list" \
        \
        "@algo image_classifier" \
        "@algo image_classifier dataset" \
        "@algo image_classifier dataset ingest" \
        "@algo image_classifier dataset review" \
        "@algo image_classifier dataset sequence" \
        "@algo image_classifier model" \
        "@algo image_classifier model prediction_test" \
        "@algo image_classifier model train" \
        \
        "@image_classifier" \
        "@image_classifier dataset" \
        "@image_classifier dataset ingest" \
        "@image_classifier dataset review" \
        "@image_classifier dataset sequence" \
        "@image_classifier model" \
        "@image_classifier model prediction_test" \
        "@image_classifier model train" \
        \
        "@algo socket" \
        "@algo socket test" \
        \
        "@algo tracker" \
        \
        "bluer_algo"; do
        bluer_ai_eval ,$options \
            bluer_ai_help $module
        [[ $? -ne 0 ]] && return 1

        bluer_ai_hr
    done

    return 0
}
