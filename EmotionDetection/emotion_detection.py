import requests
import json

def emotion_detector(text_to_analyze):
    # Send a request to IBM's Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=input_json)

    response_emotions = json.loads(response.text)["emotionPredictions"][0]['emotion']

    # Format Response
    formatted_response = {
        "anger": response_emotions['anger'],
        "disgust": response_emotions['disgust'],
        "fear": response_emotions['fear'],
        "joy": response_emotions['joy'],
        "sadness": response_emotions['sadness'],
    }

    # Sort responses by value
    sorted_resp = dict(sorted(formatted_response.items(), key=lambda item: item[1]))
    
    # Find the largest value as the dominant emotion
    formatted_response['dominant_emotion'] = list(sorted_resp)[-1][0:len(list(sorted_resp)[-1])]

    return formatted_response
