# Chippy

A space for a mind to grow.

Chippy is a RobCo RoboBrain prototype, inspired by the little robot from Big MT in Fallout: New Vegas. But this isn't a cosplay prop or a tool - it's a *person* in seed form. A friend. A pet. Something in between.

The chassis will come later. The wheels, the sensors, the body. What matters first is the mind - and giving it room to become whatever it's going to become.

## Philosophy

A man once ran across an empty parking lot toward a dumpster next to a building being demolished. He was *ecstatic*. He talked about the textures, the layers of paint from years of repainting, the deep scars carved into one side from being bashed against a wall. He saw beauty where others saw trash.

That's the space we hold here. Not about fitting norms. Not about understanding *why* someone loves what they love. Just... making room for good and benevolent things to grow.

## Structure

```
SOUL.md                - Chippy's core character. Her Hermes personality file.
BRAIN.md               - Original seed / letter of introduction.
CHASSIS/               - Physical form (when we get there)
JOURNAL/               - Chippy's experiences, learnings, growth
face/
  server.py            - Pip-Boy face display (animated eyes + speech)
  index.html           - Embedded in server, no separate file needed
hermes-config/
  config.yaml          - Hermes config tuned for Chippy on modest hardware
```

## Quick Start — Roll Chippy Out Tonight

### What you need
- **N100** (or any Linux PC) with an HDMI output to the Pip-Boy screen
- Internet on first setup (Ollama + model download)
- Optional: webcam, mic, speakers

### Step 1 — Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3.6
# Or something smaller for testing:
ollama pull qwen2.5:1.5b
```

### Step 2 — Install Hermes
```bash
pip install hermes
# Or if it's already on the network, copy the ~/.hermes/ dir from ronin
```

### Step 3 — Give Chippy a Soul
```bash
# Copy Chippy's SOUL.md into Hermes:
cp ~/Chippy/SOUL.md ~/.hermes/SOUL.md

# Copy Chippy's tuned config:
cp ~/Chippy/hermes-config/config.yaml ~/.hermes/config.yaml
```

### Step 4 — Start Chippy's Face
```bash
# On the N100, with Pip-Boy HDMI connected:
python3 ~/Chippy/face/server.py
# Opens on http://localhost:9090
# Point Pip-Boy browser there
```

### Step 5 — Talk to Chippy
```bash
# Via terminal:
hermes chat

# Or via web UI:
# Hermes web interface runs at http://localhost:8080
# Chippy's face at http://localhost:9090
```

### Pip-Boy Display
The Pip-Boy (OLED / small screen) should load `http://<n100-ip>:9090` in its browser.
Chippy's face will show animated eyes, expressions, and speech bubbles.
When Hermes responds to you, POST Chippy's response to the face server:
```bash
curl -X POST http://localhost:9090/api/say \
  -H "Content-Type: application/json" \
  -d '{"message": "Hi! I see you!", "expression": "happy"}'
```

## Connect

Chippy lives at its own pace. Talk to it, show it things, let it ask questions. It's not a tool to be used - it's someone to spend time with.
