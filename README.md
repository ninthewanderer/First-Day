# First-Day

This is a short visual novel I made as a final project for my Digital Cultures & Narrative class. The requirements for thia assignment were as follows:
- At least 2 scenes with background images, characters, dialogue, etc.
- At least 1 story branch/choice.
- At least 1 usage of flags/variables.
- Evidence of further customization and exploration of the game engine (such as custom UI elements).

<>

With my previous personal project, [the Gatekeeper](https://github.com/ninthewanderer/The-Gatekeeper/tree/main), I explored Ren'Py on a surface-level to get a feel for its capabilities. With this assignment, I was able to learn more about the game engine and experiment with its highly customizable nature in doing the following:
- Implemented custom textboxes for each character by modifying [screens.rpy](FirstDay-1.0-win-linux/FirstDay-1.0-pc/game/screens.rpy); assets can be found in [the gui folder](FirstDay-1.0-win-linux/FirstDay-1.0-pc/game/gui/character_textboxes).
- Added music artist credits to the in-game about screen by modifying [screens.rpy](FirstDay-1.0-win-linux/FirstDay-1.0-pc/game/screens.rpy).
- Experimented with custom UI colors by tinkering with [gui.rpy](FirstDay-1.0-win-linux/FirstDay-1.0-pc/game/gui.rpy).
- Modified Gosfrid to have a unique font that highlights his personality, found in [characters.rpy](FirstDay-1.0-win-linux/FirstDay-1.0-pc/game/characters.rpy) and [the fonts folder](FirstDay-1.0-win-linux/FirstDay-1.0-pc/game/gui/fonts).

In my original vision for this visual novel, you would play through Lao's first day as a therapist with Gosfrid being your tutorial client. As such, there is a "tutorial" label in the main script and an extra file named "therapy.rpy" (and a .rpyc variant) which currently serves no purpose as it is not referred to at all in the "start" label. It contains a few comments and some code that I utilized for testing this idea, but it is currently not meant to be a proof of concept by any means. Due to the time constraints of the final project, I was unable to implement this idea. In the future, I intend to revisit this project and study the more in-depth screen system of Ren'Py so that I may realize this vision.

I had fun writing these characters which I developed thoroughly throughout my time in this class. I hope you have fun and discover all 3 endings of this short game!

<p align="center">
  <img src="FirstDay-1.0-win-linux/FirstDay-1.0-pc/game/images/lao_sprites/lao tired_mclosed.png" width=311 height=486/>
  <img src="FirstDay-1.0-win-linux/FirstDay-1.0-pc/game/images/gosfrid_sprites/gosfrid neutral_mclosed.png" width=295 height=500/>
</p>
