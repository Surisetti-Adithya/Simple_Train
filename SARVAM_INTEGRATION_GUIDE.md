# Sarvam AI Deep Translation Integration Guide (English, Telugu, Hindi)

This document provides complete documentation for the Sarvam AI deep, context-aware translation integration implemented in EasyRail, compatible with and inspired by [mugdhav/SarvamAPICodeSample](https://github.com/mugdhav/SarvamAPICodeSample.git).

---

## 1. Official Sarvam AI API Verification & Specifications

| Dimension | Specification | Notes |
| :--- | :--- | :--- |
| **API Endpoint** | `POST https://api.sarvam.ai/translate` | Official REST endpoint for text translation |
| **Authentication** | `api-subscription-key: <KEY>` (Header) | Obtained from [Sarvam AI Dashboard](https://dashboard.sarvam.ai/) |
| **Alternative Header** | `Authorization: Bearer <KEY>` | Supported |
| **Supported Languages** | English (`en-IN`), Telugu (`te-IN`), Hindi (`hi-IN`) | All 22 Indian scheduled languages supported |
| **Official Models** | `mayura:v1` (Default) & `sarvam-translate:v1` | `mayura:v1` supports deep context-aware translations |
| **Character Limits** | 1,000 chars for `mayura:v1`, 2,000 chars for `sarvam-translate:v1` | Input validation enforced in UI & Python |
| **Official Pricing** | ₹2.00 per 1,000 characters | Pay-as-you-go pricing (drops to ₹1.50–₹1.70 on Pro tiers) |
| **Rate Limiting** | Token bucket (continuous replenishment) | Managed at account level |

---

## 2. Request & Response Payload Format

### HTTP Request
```http
POST https://api.sarvam.ai/translate HTTP/1.1
Content-Type: application/json
api-subscription-key: YOUR_SARVAM_API_KEY

{
  "input": "Booking Confirmed! Have a safe and pleasant journey.",
  "source_language_code": "en-IN",
  "target_language_code": "te-IN",
  "model": "mayura:v1",
  "mode": "formal",
  "speaker_gender": "None",
  "numerals_format": "international"
}
```

### Response
```json
{
  "translated_text": "బుకింగ్ విజయవంతంగా నిర్ధారించబడింది! శుభప్రదమైన మరియు సురక్షితమైన ప్రయాణం కావాలని కోరుకుంటున్నాము."
}
```

---

## 3. Translation Quality & Context Preservation

### A. Context-Aware vs. Word-to-Word Translation
- **Sentence-Level Understanding**: Rather than translating isolated words, the translation engine analyzes the complete sentence structure, applying grammatical verb inflections and honorifics.
- **Authentic Regional Vocabulary**: Avoids writing English words into regional scripts. Standard terms are rendered naturally:
  - *Origin Station*: "బయలుదేరే స్టేషన్" / "प्रस्थान स्टेशन"
  - *Destination Station*: "గమ్యస్థానం స్టేషన్" / "गंतव्य स्टेशन"
  - *Passengers*: "ప్రయాణీకులు" / "यात्री"
  - *Confirmation*: "నిర్ధారించబడింది" / "कन्फर्म"
- **Standard Technical Abbreviations Preserved**: Universally understood railway acronyms like **PNR**, **RAC**, **Tatkal**, **IRCTC**, **2A**, **3A**, **SL**, and **139** are kept intact to avoid confusion.

### B. Standardized Railway Terminology Table

| Concept | English (`en-IN`) | Hindi (`hi-IN`) | Telugu (`te-IN`) |
| :--- | :--- | :--- | :--- |
| **Ticket Booking** | Book your train ticket easily | अपनी ट्रेन टिकट आसानी से बुक करें | మీ రైలు టిక్కెట్‌ను సులభంగా బుక్ చేసుకోండి |
| **Search Trains** | Search Trains | ट्रेन खोजें | రైళ్లు వెతకండి |
| **Available Berth** | AVAILABLE | उपलब्ध | లభ్యం |
| **Reservation Against Cancellation** | RAC | आरएसी | ఆర్.ఎ.సి |
| **Waitlist** | Waitlist (WL) | प्रतीक्षा सूची (वेटलिस्ट) | వెయిట్‌లిస్ట్ |
| **Tatkal Quota** | Tatkal Quota | तत्काल कोटा | తత్కాల్ కోటా |
| **Lower Berth Priority** | Lower Berth Priority | निचली बर्थ प्राथमिकता | దిగువ బెర్త్ ప్రాధాన్యత |
| **Immediate Confirmation** | Immediate Confirmation | त्वरित पुष्टि | తక్షణ నిర్ధారణ |
| **Fare Breakdown** | Fare Breakdown | किराया विवरण | ఛార్జీల పూర్తి వివరాలు |
| **Total Payable** | Total Payable | कुल देय राशि | మొత్తం చెల్లించవలసిన మొత్తం |
| **Payment Success** | Payment Confirmed | भुगतान संपन्न | చెల్లింపు నిర్ధారించబడింది |
| **Helpline** | 24x7 Railway Helpline 139 | 24x7 रेलवे हेल्पलाइन 139 | 24x7 రైల్వే హెల్ప్‌లైన్ 139 |

---

## 4. Architectural Features & Resilience

1. **Non-Destructive Reversibility**:
   - The original dataset and strings are preserved in clean English source registries (`trains`, `stations`, `classDescriptions`, `i18n.en`).
   - Switching between English ↔ Telugu ↔ Hindi ↔ English can be done infinitely without cumulative translation degradation.

2. **Multi-Tier Caching System**:
   - **Persistent Web Storage**: Stored in `localStorage` (`sarvam_trans_cache_v2`).
   - **File-based Cache**: Cached on disk in `.sarvam_cache.json` for CLI and batch processes.
   - Eliminates redundant API billing and latency for repetitive UI phrases.

3. **Graceful Failover / Sandboxed Resilience**:
   - If an API key is not yet provided, or if the user is offline/sandboxed, EasyRail automatically falls back to its built-in context-aware neural dictionary.
   - When an API key is provided, the live cloud API is called seamlessly.

---

## 5. User Interface Features

- **Header Deep Translate Trigger**: Access the Sarvam AI Studio from any screen via the top navigation bar.
- **Language Selector Dropdown**: Switch standard app language between English (EN), हिन्दी (HI), and తెలుగు (TE), or launch the Deep Studio.
- **Screen 2 Quick Translate Bar**: One-click pills to toggle train search results, routes, days, and quotas between English, Hindi, and Telugu.
- **Screen 6 Ticket Translation**: One-click button on the confirmed e-ticket to view and print the ticket in Telugu, Hindi, or English.
- **Sarvam AI Deep Studio Modal**:
  - Live bi-directional translation for custom text, announcements, or rules.
  - Tone and formality selection (`formal`, `modern-colloquial`, `code-mixed`).
  - Gender agreement context (`Male`, `Female`, `None`).
  - Text-to-Speech audio preview in native Telugu, Hindi, or English voice.
  - One-click "Apply to Entire App" button.
  - Preloaded railway presets (PNR status, Tatkal rules, RAC explanation, Senior quota, Helpline).

---

## 6. Standalone Python Tool (`sarvam_translator.py`)

### Setup
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Add your Sarvam API Key:
   ```env
   SARVAM_API_KEY=your_key_here
   ```

### Command Line Usage
- **Translate to Telugu**:
  ```bash
  python3 sarvam_translator.py --text "Booking Confirmed!" --target te-IN
  ```
- **Translate to Hindi**:
  ```bash
  python3 sarvam_translator.py --text "Tatkal quota tickets are subject to full cancellation charges after chart preparation." --target hi-IN
  ```
- **Interactive Mode**:
  ```bash
  python3 sarvam_translator.py --interactive
  ```

### Running the Test Suite
```bash
python3 test_sarvam_integration.py
```
All 9 unit tests verify language codes, detection heuristics, context-aware translations, and bundle integrity.
