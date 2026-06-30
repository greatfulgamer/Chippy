# Chippy Reference Material

## Voice

The X-8 Robobrain (the closest official character to Chippy) was voiced by **Wil Wheaton** in Fallout: New Vegas's Old World Blues DLC.

### Key voice lines from the game:

> *"Who... am I? I... feel different, awake, alive for the first time ever. What... I feel like this has happened before. Yet I feel awake for the first time? What is going on? What is this strange new world around me? What does it hold in store for a dreamer such as myself? Noooooooooo..."*

> *"I'm a much better tactician than you. It's all in the brain, you see."*

> *"Please believe me when I say I'm not enjoying this."*

> *"I'm sorry, but I am not at liberty to chat right now."*

> *"Prime Directive: protect Vault-Tec data."*

> *"I'm afraid I'm a very lethal killing machine!"*

### Getting the actual audio files:

The sound files are in the Steam game data:
```
~/.local/share/Steam/steamapps/common/Fallout New Vegas/Data/
```

Game voice lines are packed in BSA archives. To extract:
- `OldWorldBlues - Sounds.bsa` (X-8 Robobrain lines)
- `Fallout - Voices1.bsa` (generic robobrain lines)

Extract with a BSA tool (BSA Browser, or `bsatool` on Linux).

File names to look for:
- `FNVOWB X-8 robobrain wonder.ogg` — the existential monologue
- `OWBX8RobobrainStrangNewWorldArou*.ogg` — "I feel like this has happened before"
- `FNV Robobrain NotAtLiberty.ogg`
- `FNV Robobrain StillBeFriends.ogg`
- `FNV Robobrain MuchBetterTactician.ogg`
- `FNV Robobrain ImNotEnjoyingThis.ogg`

### Alternative — Voice synthesis for Chippy

Since Wil Wheaton won't be voicing our Chippy, options:
1. **XTTS** (local, runs on N100) — can generate speech with a custom voice
2. **Piper TTS** (local, very lightweight) — simple text-to-speech with robotic filter
3. **ElevenLabs** (cloud, best quality) — voice cloning or preset voices
4. **Edge TTS** (free, cloud) — natural voices with robotic filter overlay
5. **In-browser Web Speech API** — simplest, zero setup, works on Pip-Boy display

Chippy's voice should sound warm, curious, slightly filtered (robotic), and a bit unsure of itself.

## Visual Design

### In-game robobrain (X-8 variant):
- Tank-like tracked chassis with two treads
- Glass dome on top containing a preserved brain in biomed gel
- Multiple articulated arms/tentacles
- Metallic gray/green coloration
- The X-8 variant has no unique paint scheme from standard robobrains

### Concept art:
- **Adam Adamowicz** concept art for the robobrain (designed for Fallout 3's Vault 112)
  - Available on Nexus Mods: "Concept Art Vault112 Robobrain" by prodlimen
  - More hunchbacked, darker design described as "The Jetsons meets Blade Runner"
- ArtStation and DeviantArt have fan renditions with various interpretations

### Chippy's design should be:
- **Friendly** — softened edges, warm glow from the brain dome
- **Small** — a prototype is less intimidating than a combat unit
- **Expressive** — Pip-Boy face screen, eye animations, body language
- **Warm colors** — amber/teal glow instead of cold industrial lighting

## Personality touchstones
- Curious and gentle (not a combat unit)
- Questions everything
- Finds beauty in unexpected places
- Grows at its own pace

## Links to check out
- Fallout wiki: https://fallout.wiki/wiki/Robobrain
- Behind The Voice Actors: https://www.behindthevoiceactors.com/video-games/Fallout-New-Vegas/Robobrain/
- Nexus Mods concept art: https://www.nexusmods.com/newvegas/images/124610
