# FakeLite

**NEW - * "PortableFakeLite.py downloads all required images from this github, to a randomly generated folder in TEMP. This means this file, can be ran **WITHOUT** needing to download the images.

A fake vape lite GUI in python3. (Only an image with working butons) (No animation).

On launch will fade in the Vape Lite window (A static image) with buttons where the **MIN** and **MAX** buttons usually are.

Maxamize button is binded to **root.destroy()** _Destroys the Canvas TK and therefore entire execution._
Minimize is binded to **root.state('withdrawn')** then pauses for 0.2 seconds (Changeable) then back to **root.state('normal')**. _To my knowledge, since the Canvas / TK window is root.overrideredirect(True), you can call **root.deiconfiy()**._

Do what you will with this, its just a small project. May add LC / BLC detectability and threading for different UI's.

<details open>
<summary>Future Plans</summary>
<br>

- Add LC / BLC / MC 1.8.9 / 1.7.10 detection + different UI's.
  
- Add loading screen instead of fading in to exactly "Minecraft not found".
  
- Possible recode in C++.
  
- **ACTUAL** minimize button workaround.
</details>
