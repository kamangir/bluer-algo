#! /usr/bin/env bash

function test_bluer_algo_image_classifier_dataset_ingest() {
    local options=$1

    local object_name=test_bluer_algo_image_classifier_dataset_ingest-$(bluer_ai_string_timestamp)

    bluer_ai_eval ,$options \
        bluer_algo_image_classifier_dataset_review \
        ,$options \
        $BLUER_ALGO_FRUITS_360_TEST_DATASET
}
