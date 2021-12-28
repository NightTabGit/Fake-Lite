# FakeLite
A fake vape lite GUI in python3. (Only an image with working butons) (No animation).

On launch will fade in the Vape Lite window (A static image) with buttons where the **MIN** and **MAX** buttons usually are.

Maxamize button is binded to **root.destroy()** _Destroys the Canvas TK and therefore entire execution._
Minimize is binded to **root.state('withdrawn')** then pauses for 0.2 seconds (Changeable) then back to **root.state('normal')**. _To my knowledge, since the Canvas / TK window is root.overrideredirect(True), you can call **root.deiconfiy()**._

Do what you will with this, its just a small project. May add LC / BLC detectability and threading for different UI's.
