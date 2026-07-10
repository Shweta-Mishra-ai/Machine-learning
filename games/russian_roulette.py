"""Josephus-style Russian Roulette elimination simulation.

Refactored to support optional audio dependencies (playsound, pyttsx3) to ensure
cross-platform stability.
"""

import time
import random

# Optional dependencies handling
try:
    import pyttsx3
    HAS_TTS = True
except ImportError:
    HAS_TTS = False

try:
    import playsound
    HAS_PLAYSOUND = True
except ImportError:
    HAS_PLAYSOUND = False

class RussianRoulette:
    def __init__(self, names: list[str] = None):
        if names:
            self.players = list(names)
        else:
            self.players = ["Shweta", "Gunjan", "Arti", "Shivani", "Nidhi", "Deeksha", "Neha", "Alka"]
        
        self.tts_engine = None
        if HAS_TTS:
            try:
                self.tts_engine = pyttsx3.init()
            except Exception:
                self.tts_engine = None

    def speak(self, text: str):
        """Speak text using text-to-speech if available, otherwise log to console."""
        print(text)
        if self.tts_engine:
            try:
                self.tts_engine.say(text)
                self.tts_engine.runAndWait()
            except Exception:
                pass

    def play_sound(self, sound_type: str):
        """Play sound effects if playsound is installed and assets are present."""
        # Since original paths were absolute to a physical drive (G:\), we bypass
        # missing file crashes. If we had local audio assets we would play them here.
        if HAS_PLAYSOUND:
            # Placeholder for potential audio file playback
            pass

    def start_elimination(self, step: int = 2):
        """Run the elimination game using a Josephus step interval.
        
        Default step is 2 (eliminating every second person).
        """
        print("\n--- Starting Russian Roulette (Josephus Elimination) ---")
        print(f"Initial Players: {', '.join(self.players)}")
        time.sleep(1)
        
        idx = 0
        while len(self.players) > 1:
            # Determine next index to eliminate
            # With step=2, we advance by 2 from the current index (but because we
            # remove an element, the list shifts, so we effectively add step - 1)
            idx = (idx + step - 1) % len(self.players)
            eliminated = self.players.pop(idx)
            
            self.play_sound("gunshot")
            message = f"{eliminated} has been eliminated!"
            self.speak(message)
            print("-" * 35)
            time.sleep(1)
            
        winner = self.players[0]
        self.play_sound("victory")
        victory_msg = f"The winner of Russian Roulette is {winner}! Congratulations!"
        self.speak(victory_msg)
        time.sleep(1)

if __name__ == "__main__":
    game = RussianRoulette()
    game.start_elimination()
