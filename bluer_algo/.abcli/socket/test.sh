#! /usr/bin/env bash

function bluer_algo_socket_test() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    bluer_ai_eval dryrun=$do_dryrun \
        python3 -m bluer_algo.socket \
        test \
        "${@:2}"
}
