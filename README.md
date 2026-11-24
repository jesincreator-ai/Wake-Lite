# Wake Lite

A small wake-word adapter for BILLI R-20 with an optional openWakeWord backend and a safe push-to-talk fallback.


## ESP32-WROOM local build
The repository includes `wake_lite.py`, a minimal text wake-phrase state machine suitable for MicroPython and serial/push-to-talk testing. Raw microphone wake-word detection is not included in this microcontroller file; connect a detector through `wake_event()` when an audio front-end is available. Mobile demo: `mobile_test.html`.
