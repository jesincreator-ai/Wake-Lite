"""Wake Lite MicroPython wake state machine and pluggable detector event."""
class WakeLite:
    def __init__(self, phrase='hey billi'):
        self.phrase=str(phrase).lower().strip(); self.state='sleep'; self.last_text=''
    def wake_event(self): self.state='awake'; return True
    def detect_text(self, text):
        s=str(text or '').lower()
        if self.phrase in s or ('billi' in s and 'hey' in s):
            self.last_text=str(text); self.state='awake'; return True
        return False
    def sleep(self): self.state='sleep'
    def get_state(self): return self.state
if __name__=='__main__':
    w=WakeLite()
    while True:
        try:
            t=input('WAKE TEST> ')
            print('WAKE!' if w.detect_text(t) else 'No wake phrase',w.get_state())
        except KeyboardInterrupt: break
