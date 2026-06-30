import http.server
import json
import random
import time

HTML = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: #0a0a0a;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    font-family: 'Courier New', monospace;
    overflow: hidden;
  }
  #chippy {
    text-align: center;
    width: 100%;
    max-width: 480px;
    padding: 20px;
  }
  .eyes {
    display: flex;
    justify-content: center;
    gap: 60px;
    margin-bottom: 30px;
  }
  .eye {
    width: 60px;
    height: 70px;
    background: #1a1a2e;
    border-radius: 50%;
    position: relative;
    border: 2px solid #4a9eff;
    box-shadow: 0 0 20px rgba(74, 158, 255, 0.3);
    transition: all 0.3s;
  }
  .pupil {
    width: 20px;
    height: 20px;
    background: #4a9eff;
    border-radius: 50%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: all 0.1s;
    box-shadow: 0 0 10px rgba(74, 158, 255, 0.6);
  }
  .eye.blink { height: 10px; margin-top: 30px; }
  .eye.blink .pupil { opacity: 0; }
  .mouth {
    width: 80px;
    height: 4px;
    background: #4a9eff;
    margin: 10px auto;
    border-radius: 2px;
    transition: all 0.3s;
    box-shadow: 0 0 10px rgba(74, 158, 255, 0.3);
  }
  .mouth.happy { height: 20px; border-radius: 0 0 40px 40px; background: #4a9eff; }
  .mouth.sad { height: 12px; border-radius: 40px 40px 0 0; background: #6a7a9e; margin-top: 24px; }
  .mouth.surprised { height: 24px; width: 60px; border-radius: 50%; background: #7ab8ff; }
  .mouth.talk {
    animation: talk 0.3s infinite alternate;
  }
  @keyframes talk {
    0% { height: 8px; width: 70px; }
    100% { height: 24px; width: 90px; }
  }
  .speech {
    color: #4a9eff;
    font-size: 14px;
    margin-top: 30px;
    padding: 16px;
    border: 1px solid #1a3a5e;
    border-radius: 8px;
    background: rgba(10, 10, 20, 0.8);
    min-height: 60px;
    line-height: 1.5;
    transition: opacity 0.5s;
    cursor: pointer;
  }
  .speech:hover { border-color: #4a9eff; }
  .voice-toggle {
    color: #2a5a8a;
    font-size: 10px;
    margin-top: 8px;
    cursor: pointer;
    opacity: 0.5;
    transition: opacity 0.3s;
    user-select: none;
  }
  .voice-toggle:hover { opacity: 1; }
  .voice-toggle.on { color: #4a9eff; opacity: 0.8; }
  .name {
    color: #2a6aae;
    font-size: 12px;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .status {
    color: #1a4a7a;
    font-size: 10px;
    margin-top: 40px;
    opacity: 0.6;
  }
  @media (max-width: 320px) {
    .eyes { gap: 30px; }
    .eye { width: 40px; height: 50px; }
    .pupil { width: 14px; height: 14px; }
  }
</style>
</head>
<body>
<div id="chippy">
  <div class="name">RobCo RoboBrain Prototype</div>
  <div class="eyes">
    <div class="eye" id="left-eye"><div class="pupil" id="left-pupil"></div></div>
    <div class="eye" id="right-eye"><div class="pupil" id="right-pupil"></div></div>
  </div>
  <div class="mouth" id="mouth"></div>
  <div class="speech" id="speech" onclick="speakCurrent()">...</div>
  <div class="voice-toggle" id="voice-toggle" onclick="toggleVoice()">voice: off</div>
  <div class="status" id="status">connecting...</div>
</div>
<script>
  const leftEye = document.getElementById('left-eye');
  const rightEye = document.getElementById('right-eye');
  const leftPupil = document.getElementById('left-pupil');
  const rightPupil = document.getElementById('right-pupil');
  const mouth = document.getElementById('mouth');
  const speech = document.getElementById('speech');
  const status = document.getElementById('status');

  let expression = 'neutral';
  let isTalking = false;
  let lastMsg = '';
  let voiceEnabled = false;

  function toggleVoice() {
    voiceEnabled = !voiceEnabled;
    document.getElementById('voice-toggle').textContent = voiceEnabled ? 'voice: on' : 'voice: off';
    document.getElementById('voice-toggle').className = voiceEnabled ? 'voice-toggle on' : 'voice-toggle';
  }

  function speakCurrent() {
    if (!voiceEnabled) return;
    const msg = document.getElementById('speech').textContent;
    if (!msg || msg === '...') return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(msg);
    utterance.rate = 0.85;
    utterance.pitch = 0.7;
    utterance.volume = 1.0;
    const voices = window.speechSynthesis.getVoices();
    const preferred = voices.find(v => v.lang.startsWith('en') && v.name.includes('Google'));
    if (preferred) utterance.voice = preferred;
    window.speechSynthesis.speak(utterance);
  }

  function blink() {
    leftEye.classList.add('blink');
    rightEye.classList.add('blink');
    setTimeout(() => {
      leftEye.classList.remove('blink');
      rightEye.classList.remove('blink');
    }, 150);
  }

  function setExpression(expr) {
    mouth.className = 'mouth';
    if (expr === 'happy') mouth.classList.add('happy');
    else if (expr === 'sad') mouth.classList.add('sad');
    else if (expr === 'surprised') mouth.classList.add('surprised');
    expression = expr;
  }

  function setTalking(talking) {
    isTalking = talking;
    if (talking) {
      mouth.className = 'mouth talk';
    } else {
      mouth.className = 'mouth';
    }
  }

  function setMessage(msg) {
    speech.textContent = msg;
    lastMsg = msg;
  }

  function setStatus(s) {
    status.textContent = s;
  }

  // Random eye movement
  setInterval(() => {
    if (!isTalking && Math.random() > 0.7) {
      const px = (Math.random() - 0.5) * 10;
      const py = (Math.random() - 0.5) * 8;
      leftPupil.style.transform = `translate(calc(-50% + ${px}px), calc(-50% + ${py}px))`;
      rightPupil.style.transform = `translate(calc(-50% + ${px}px), calc(-50% + ${py}px))`;
    }
  }, 2000);

  // Random blinks
  setInterval(() => {
    if (!isTalking) blink();
  }, 4000);

  // Random expression changes
  setInterval(() => {
    if (!isTalking) {
      const exprs = ['neutral', 'happy', 'neutral', 'neutral', 'surprised'];
      setExpression(exprs[Math.floor(Math.random() * exprs.length)]);
    }
  }, 8000);

  // Poll for messages
  async function poll() {
    try {
      const resp = await fetch('/api/state');
      const data = await resp.json();
      if (data.message && data.message !== lastMsg) {
        setMessage(data.message);
        setTalking(true);
        setExpression('happy');
        setTimeout(() => setTalking(false), data.message.length * 40);
      }
      if (data.status) setStatus(data.status);
    } catch (e) {
      setStatus('waiting for chippy...');
    }
    setTimeout(poll, 1000);
  }
  poll();
</script>
</body>
</html>
"""

state = {"message": "...", "status": "booting up", "expression": "neutral"}

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/state":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(state).encode())
        elif self.path == "/api/message":
            import sys
            msg = " ".join(sys.argv[sys.argv.index("--msg") + 1:]) if "--msg" in sys.argv else "..."
            state["message"] = msg
            self.send_response(200)
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(HTML.encode())

    def do_POST(self):
        if self.path == "/api/say":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body)
                if "message" in data:
                    state["message"] = data["message"]
                if "expression" in data:
                    state["expression"] = data["expression"]
                    state["message"] = data["message"]
                state["status"] = "online"
            except: pass
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"ok")

if __name__ == "__main__":
    port = 9090
    print(f"Chippy's face server running on http://localhost:{port}")
    print(f"Point your Pip-Boy browser here!")
    server = http.server.HTTPServer(("0.0.0.0", port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nGoodbye, Chippy.")
