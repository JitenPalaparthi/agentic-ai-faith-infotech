Download ollama

docker run -d \
  --name ollama \
  -p 11434:11434 \
  -v ollama_data:/root/.ollama \
  ollama/ollama

download qwen

docker exec -it ollama ollama pull qwen3:4b

docker exec -it ollama ollama list

docker exec -it ollama ollama run qwen3:4b

test ollama http

curl http://localhost:11434/api/chat \
  -d '{
    "model": "qwen3:4b",
    "messages": [
      {
        "role": "user",
        "content": "Hello, explain Golang in one sentence"
      }
    ],
    "stream": false
  }'
