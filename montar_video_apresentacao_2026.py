import os
import sys
import glob
import subprocess
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
FRAMES_DIR = os.path.abspath("frames_2026")
AUDIOS_DIR = os.path.abspath("audios_tiago_2026")
OUTPUT_VIDEO = os.path.abspath(os.path.expanduser("~") + "/Desktop/Apresentacao de Vendas 2026 - BotConversa - Voz Tiago.mp4")

def get_audio_duration(file_path: str) -> float:
    cmd = [FFMPEG, "-i", file_path]
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="ignore")
    for line in p.stderr.splitlines():
        if "Duration:" in line:
            parts = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = parts.split(":")
            return float(h) * 3600 + float(m) * 60 + float(s)
    return 3.0 # fallback

def main():
    total_slides = 84
    print(f"Verificando {total_slides} slides para montagem do vídeo...")

    timeline_entries = []
    audio_concat_list = []

    for idx in range(1, total_slides + 1):
        frame_path = os.path.join(FRAMES_DIR, f"slide_{idx:03d}.png").replace("\\", "/")
        audio_path = os.path.join(AUDIOS_DIR, f"Slide_{idx:02d}.mp3").replace("\\", "/")

        if not os.path.exists(frame_path):
            print(f"[ERRO] Frame ausente: {frame_path}")
            return

        if not os.path.exists(audio_path):
            print(f"[AVISO] Áudio do Slide {idx} não encontrado. Aguarde a síntese completa.")
            return

        dur = get_audio_duration(audio_path)
        # Adicionar um pequeno respiro no slide (0.2s) para transição suave
        dur_with_padding = round(dur + 0.2, 3)
        timeline_entries.append((frame_path, dur_with_padding))
        audio_concat_list.append(audio_path)

    # Criar arquivo de timeline ffconcat
    timeline_file = os.path.abspath("slides_timeline_2026.txt")
    with open(timeline_file, "w", encoding="utf-8") as f:
        f.write("ffconcat version 1.0\n")
        for f_path, dur in timeline_entries:
            f.write(f"file '{f_path}'\n")
            f.write(f"duration {dur:.3f}\n")
        # Repetir o último frame para conformidade com ffconcat
        f.write(f"file '{timeline_entries[-1][0]}'\n")

    # Criar lista de concatenação de áudios
    audio_list_file = os.path.abspath("audio_concat_2026.txt")
    with open(audio_list_file, "w", encoding="utf-8") as f:
        for a_path in audio_concat_list:
            f.write(f"file '{a_path}'\n")

    # Passo 1: Concatenar todos os áudios em master_audio_2026.wav
    master_audio = os.path.abspath("master_audio_2026.wav")
    print("Concatenando áudios no master_audio_2026.wav...")
    cmd_audio = [
        FFMPEG, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", audio_list_file,
        "-c:a", "pcm_s16le",
        master_audio
    ]
    subprocess.run(cmd_audio, check=True)

    # Passo 2: Renderizar o vídeo final Full HD 1080p
    print(f"Renderizando vídeo final sincronizado em: {OUTPUT_VIDEO}...")
    cmd_video = [
        FFMPEG, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", timeline_file,
        "-i", master_audio,
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUTPUT_VIDEO
    ]
    subprocess.run(cmd_video, check=True)
    print(f"VÍDEO CRIADO COM SUCESSO!\nSalvo em: {OUTPUT_VIDEO}")

if __name__ == "__main__":
    main()
