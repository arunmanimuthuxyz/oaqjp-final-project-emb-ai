"""Unit tests for the emotion_detector function."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion_detector covering all five emotions."""

    def test_joy_emotion(self):
        """Text expressing joy should return 'joy' as dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_anger_emotion(self):
        """Text expressing anger should return 'anger' as dominant emotion."""
        result = emotion_detector("I am really angry at this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_emotion(self):
        """Text expressing disgust should return 'disgust' as dominant emotion."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sadness_emotion(self):
        """Text expressing sadness should return 'sadness' as dominant emotion."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_emotion(self):
        """Text expressing fear should return 'fear' as dominant emotion."""
        result = emotion_detector("I am really scared about this")
        self.assertEqual(result['dominant_emotion'], 'fear')


if __name__ == '__main__':
    unittest.main()