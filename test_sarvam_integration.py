#!/usr/bin/env python3
"""
Test Suite for Sarvam AI Deep Translation Integration
======================================================
Tests verify:
1. Python translation module (sarvam_translator.py)
2. Context-aware grammar and vocabulary preservation (English, Telugu, Hindi)
3. Formality detection based on honorifics and pronouns
4. Gender detection
5. Persistent disk and memory caching
6. HTML/JS bundle integrity (easyrail.html)
"""

import unittest
import os
import json
from sarvam_translator import (
    translate_text,
    detect_language,
    detect_formality,
    detect_gender,
    SUPPORTED_LANGUAGES,
    SARVAM_API_ENDPOINT,
    DEFAULT_MODEL
)


class TestSarvamTranslation(unittest.TestCase):

    def test_supported_languages(self):
        """Verify official language codes according to Sarvam AI documentation."""
        self.assertIn("en-IN", SUPPORTED_LANGUAGES)
        self.assertIn("te-IN", SUPPORTED_LANGUAGES)
        self.assertIn("hi-IN", SUPPORTED_LANGUAGES)
        self.assertEqual(SARVAM_API_ENDPOINT, "https://api.sarvam.ai/translate")
        self.assertEqual(DEFAULT_MODEL, "mayura:v1")

    def test_language_detection(self):
        """Verify automatic script/language detection."""
        self.assertEqual(detect_language("Book your train ticket"), "en-IN")
        self.assertEqual(detect_language("మీ రైలు టిక్కెట్‌ను సులభంగా బుక్ చేసుకోండి"), "te-IN")
        self.assertEqual(detect_language("अपनी ट्रेन टिकट आसानी से बुक करें"), "hi-IN")

    def test_formality_detection(self):
        """Verify formality detection based on pronouns and honorifics."""
        # Hindi
        self.assertEqual(detect_formality("कृपया आप अपनी सीट बताएं", "hi-IN"), "formal")
        self.assertEqual(detect_formality("तू कब आ रहा है", "hi-IN"), "modern-colloquial")

        # Telugu
        self.assertEqual(detect_formality("దయచేసి మీరు టికెట్ చూపించండి", "te-IN"), "formal")
        self.assertEqual(detect_formality("నువ్వు ఎప్పుడు వస్తున్నావు రా", "te-IN"), "modern-colloquial")

        # English
        self.assertEqual(detect_formality("Please kindly verify your PNR status, sir.", "en-IN"), "formal")
        self.assertEqual(detect_formality("Hey dude wanna check trains?", "en-IN"), "modern-colloquial")

    def test_gender_detection(self):
        """Verify gender context detection."""
        self.assertEqual(detect_gender("Mr. Sharma is traveling in Coach B2", "en-IN"), "Male")
        self.assertEqual(detect_gender("Mrs. Rao booked lower berth", "en-IN"), "Female")
        self.assertEqual(detect_gender("General passenger reservation", "en-IN"), "None")

    def test_deep_translation_english_to_telugu(self):
        """Test context-aware translation from English to Telugu."""
        text = "Booking Confirmed!"
        res = translate_text(text, target_language_code="te-IN", source_language_code="en-IN")
        self.assertEqual(res["target_language_code"], "te-IN")
        self.assertEqual(res["translated_text"], "బుకింగ్ విజయవంతంగా నిర్ధారించబడింది!")

    def test_deep_translation_english_to_hindi(self):
        """Test context-aware translation from English to Hindi."""
        text = "Booking Confirmed!"
        res = translate_text(text, target_language_code="hi-IN", source_language_code="en-IN")
        self.assertEqual(res["target_language_code"], "hi-IN")
        self.assertEqual(res["translated_text"], "बुकिंग सफलतापूर्वक कन्फर्म हुई!")

    def test_railway_tatkal_rules_telugu(self):
        """Test complex railway policy translation to Telugu."""
        text = "Tatkal quota tickets are subject to full cancellation charges after chart preparation."
        res = translate_text(text, target_language_code="te-IN", source_language_code="en-IN")
        self.assertIn("తత్కాల్", res["translated_text"])
        self.assertIn("రీఫండ్", res["translated_text"])

    def test_caching_behavior(self):
        """Verify that repeated queries hit cache."""
        text = "Please carry original government-issued photo ID for IRCTC ticket verification."
        res1 = translate_text(text, target_language_code="te-IN", source_language_code="en-IN", use_cache=True)
        res2 = translate_text(text, target_language_code="te-IN", source_language_code="en-IN", use_cache=True)
        self.assertTrue(res2["from_cache"])
        self.assertEqual(res1["translated_text"], res2["translated_text"])

    def test_easyrail_html_bundle_integrity(self):
        """Verify that easyrail.html contains all necessary Sarvam AI controls and markup."""
        html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "easyrail.html")
        self.assertTrue(os.path.exists(html_path), "easyrail.html does not exist!")

        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Check required DOM & engine elements
        required_elements = [
            'SarvamAI',
            'api.sarvam.ai/translate',
            'mayura:v1',
            'te-IN',
            'hi-IN',
            'en-IN',
            'setupFAQAccordion',
            'renderFAQAccordion',
            'openRefundTrackerModal'
        ]

        for elem in required_elements:
            self.assertIn(elem, content, f"Missing required element: {elem}")


if __name__ == "__main__":
    unittest.main()
