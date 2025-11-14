"""
ClarifyAI is a leading platform for computer vision and
multi-modal AI. It offers powerful APIs for image, video and text analysis.
Can be used for object detection, face recognition, etc.

curl -X POST "https://api.clarifai.com/v2/models/moderation-output/outputs" \
    -H "Authorization: Key API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "inputs": [
            {
                "data": {
                    "images": {
                        "url": "https://example.com/image.jpg"
                    }
                }
            }
        ]
    }'    
"""
