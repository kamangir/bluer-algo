#! /usr/bin/env bash

function bluer_algo_ai_agent_validate() {
    # https://docs.arvancloud.ir/fa/aiaas/api-usage
    curl --location '$BLUER_ALGO_AI_AGENT_ENDPOINT/chat/completions' \ 
    --header 'Authorization: apikey $BLUER_ALGO_AI_AGENT_API_KEY' \ 
    --header 'Content-Type: application/json' \ 
    --data '{  
    "model": "DeepSeek-R1-qwen-7b-awq",  
    "messages": [  
        {"role": "user", "content": "چرا آسمان آبی است؟"}  
    ],  
    "max_tokens": 3000,  
    "temperature": 0.7  
}'
}
