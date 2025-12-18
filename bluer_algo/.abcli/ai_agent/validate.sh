#! /usr/bin/env bash

function bluer_algo_ai_agent_validate() {
    # https://docs.arvancloud.ir/fa/aiaas/api-usage
    curl --location '[Endpoint]/v1/chat/completions' \ 
    --header 'Authorization: apikey ****' \ 
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
