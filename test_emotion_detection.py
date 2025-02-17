from EmotionDetection import emotion_detection
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Test case for joy emotion
        result_1 = emotion_detection.emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for anger emotion
        result_2 = emotion_detection.emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case for disgust emotion
        result_3 = emotion_detection.emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case for sadness emotion
        result_4 = emotion_detection.emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case for fear emotion
        result_5 = emotion_detection.emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()