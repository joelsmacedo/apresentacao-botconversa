import os
import sys
import json
import time
import urllib.request
import urllib.error

# Pipeline de síntese de voz usando o VoiceStudio Local (Gratuito)
# Endpoint OpenAI-compatível em http://localhost:3900/v1/audio/speech
# Perfil Clonado: "Tiago" (id: 9ec7e033)

VOICESTUDIO_URL = "http://localhost:3900/v1/audio/speech"
VOICE_PROFILE_ID = "9ec7e033" # Perfil clonado do Tiago
SPEED = 1.10 # Dinâmica do Tiago: fala rápida, segura e com convicção
NUM_STEP = 10 # 10 passos para qualidade excelente e síntese otimizada na RTX 3050

OUTPUT_DIR = "audios_tiago_2026"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_slide_audio(slide_num: int, text: str, retries: int = 3) -> str:
    filename = os.path.join(OUTPUT_DIR, f"Slide_{slide_num:02d}.mp3")
    
    if os.path.exists(filename) and os.path.getsize(filename) > 5000:
        print(f"[Slide {slide_num:02d}] Já gerado ({os.path.getsize(filename)} bytes). Pulando.")
        return filename

    # Se o texto for excessivamente curto ou vazio
    if not text.strip():
        text = "BotConversa."

    payload = {
        "input": text,
        "voice": VOICE_PROFILE_ID,
        "language": "pt",
        "speed": SPEED,
        "num_step": NUM_STEP,
        "response_format": "mp3",
        "denoise": True
    }

    data_bytes = json.dumps(payload).encode("utf-8")

    for attempt in range(1, retries + 1):
        try:
            t0 = time.time()
            req = urllib.request.Request(
                VOICESTUDIO_URL,
                data=data_bytes,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=180) as resp:
                audio = resp.read()
                with open(filename, "wb") as f:
                    f.write(audio)
                elapsed = time.time() - t0
                print(f"[Slide {slide_num:02d}] Sucesso! {len(audio)} bytes gerados em {elapsed:.1f}s.")
                return filename
        except Exception as e:
            print(f"[Slide {slide_num:02d}] Tentativa {attempt}/{retries} falhou: {e}")
            time.sleep(3)

    raise RuntimeError(f"Falha ao gerar áudio para Slide {slide_num}")

def main():
    with open("slides_roteiro_tiago_2026.json", "r", encoding="utf-8") as f:
        slides = json.load(f)

    # Permitir passar argumentos: e.g. python gerar_audio_tiago.py 1 5 (para slides 1 a 5)
    start_slide = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end_slide = int(sys.argv[2]) if len(sys.argv) > 2 else len(slides)

    print(f"Iniciando síntese de voz do Tiago para slides {start_slide} a {end_slide}...")
    for s in slides:
        num = s["slide_number"]
        if start_slide <= num <= end_slide:
            script = s["script_tiago"]
            generate_slide_audio(num, script)

    print("Processamento concluído.")

if __name__ == "__main__":
    main()
