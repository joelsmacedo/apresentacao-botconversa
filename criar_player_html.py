import os
import json
import base64

def generate_player_html():
    with open('slides_roteiro_tiago_2026.json', 'r', encoding='utf-8') as f:
        slides = json.load(f)

    with open('botconversa_mark.png', 'rb') as f:
        logo_b64 = base64.b64encode(f.read()).decode('utf-8')
    logo_data_uri = f'data:image/png;base64,{logo_b64}'

    slides_json = json.dumps(slides, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>BotConversa • Apresentação de Vendas 2026</title>
  <link rel="icon" type="image/png" href="botconversa_mark.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=Nunito+Sans:wght@400;600;700&display=swap" rel="stylesheet">

  <style>
    :root {{
      --primary: #3083FF;
      --primary-hover: #1e70ea;
      --primary-light: rgba(48, 131, 255, 0.12);
      --brand-green: #28C765;
      --brand-green-hover: #22b157;
      --brand-green-light: rgba(40, 199, 101, 0.16);

      --bg-dark: #0a0a0c;
      --bg-card: #121316;
      --bg-surface: #161619;
      --bg-surface-hover: #212127;
      --border: rgba(255, 255, 255, 0.08);
      --border-strong: rgba(255, 255, 255, 0.15);

      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --text-dim: #6b7280;

      --font-family: 'Inter Tight', 'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --radius-sm: 6px;
      --radius-md: 8px;
      --radius-lg: 12px;
      --radius-pill: 9999px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      font-family: var(--font-family);
      background: var(--bg-dark);
      color: var(--text-main);
      height: 100vh;
      height: 100dvh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    /* Scrollbars elegantes */
    ::-webkit-scrollbar {{
      width: 5px;
      height: 5px;
    }}
    ::-webkit-scrollbar-track {{
      background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-pill);
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: var(--primary);
    }}

    /* HEADER */
    header {{
      background: var(--bg-card);
      border-bottom: 1px solid var(--border);
      padding: 10px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-shrink: 0;
      z-index: 30;
    }}
    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 12px;
      color: #fff;
    }}
    .brand-logo-img {{
      height: 32px;
      width: auto;
      object-fit: contain;
      display: block;
      border-radius: var(--radius-sm);
    }}
    .brand-title {{
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-muted);
      border-left: 1px solid var(--border);
      padding-left: 12px;
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
    }}
    .brand-title span {{
      color: #fff;
      font-weight: 700;
    }}
    .partner-tag {{
      font-size: 0.72rem;
      font-weight: 500;
      color: #94a3b8;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
      padding: 2px 8px;
      border-radius: var(--radius-sm);
      letter-spacing: 0.02em;
      white-space: nowrap;
    }}
    .sidebar-footer {{
      padding: 10px 14px;
      font-size: 0.72rem;
      color: var(--text-dim);
      border-top: 1px solid var(--border);
      text-align: center;
      background: var(--bg-card);
      flex-shrink: 0;
    }}
    .desk-partner-note {{
      font-size: 0.76rem;
      color: var(--text-dim);
      border-left: 1px solid var(--border);
      padding-left: 12px;
      white-space: nowrap;
    }}
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .badge-tiago {{
      background: var(--primary-light);
      border: 1px solid rgba(48, 131, 255, 0.3);
      color: #93c5fd;
      padding: 4px 12px;
      border-radius: var(--radius-pill);
      font-size: 0.8rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }}
    .btn-drawer-toggle {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: var(--radius-md);
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: none;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}
    .btn-drawer-toggle:hover {{
      background: var(--bg-surface-hover);
      border-color: var(--primary);
    }}

    /* MAIN WRAPPER */
    main {{
      display: flex;
      flex: 1;
      min-height: 0;
      overflow: hidden;
      position: relative;
    }}

    /* SIDEBAR (DESKTOP) & DRAWER (MOBILE) */
    .sidebar {{
      width: 320px;
      background: var(--bg-card);
      border-right: 1px solid var(--border);
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      z-index: 40;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }}
    .sidebar-header {{
      padding: 14px 18px;
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      background: var(--bg-card);
      z-index: 10;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .sidebar-close-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 1.1rem;
      cursor: pointer;
      display: none;
      padding: 4px;
    }}
    .slide-item {{
      padding: 10px 14px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      gap: 10px;
      align-items: center;
    }}
    .slide-item:hover {{
      background: var(--bg-surface-hover);
    }}
    .slide-item.active {{
      background: var(--primary-light);
      border-left: 3px solid var(--primary);
    }}
    .slide-badge {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      padding: 2px 7px;
      border-radius: var(--radius-sm);
      font-size: 0.75rem;
      font-weight: 700;
      min-width: 32px;
      text-align: center;
      color: #93c5fd;
    }}
    .slide-item.active .slide-badge {{
      background: var(--primary);
      border-color: var(--primary);
      color: #fff;
    }}
    .slide-info {{
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
      font-size: 0.86rem;
      font-weight: 500;
    }}

    /* DRAWER OVERLAY (MOBILE) */
    .drawer-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.65);
      backdrop-filter: blur(4px);
      z-index: 35;
    }}
    .drawer-backdrop.active {{
      display: block;
    }}

    /* CONTENT AREA */
    .content-area {{
      flex: 1;
      display: flex;
      flex-direction: column;
      padding: 18px 24px;
      overflow: hidden;
      min-height: 0;
      height: 100%;
    }}
    .visual-and-script {{
      display: grid;
      grid-template-columns: minmax(0, 1.25fr) minmax(0, 0.75fr);
      gap: 20px;
      flex: 1;
      min-height: 0;
      height: 100%;
      align-items: stretch;
    }}

    /* VISUAL BOX (SLIDE) */
    .visual-box {{
      background: #000;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
      height: 100%;
      max-height: 100%;
      min-height: 0;
    }}
    .visual-box img {{
      width: 100%;
      height: 100%;
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      cursor: zoom-in;
    }}
    .fullscreen-btn {{
      position: absolute;
      top: 12px;
      right: 12px;
      background: rgba(18, 19, 22, 0.85);
      border: 1px solid var(--border-strong);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      backdrop-filter: blur(8px);
      transition: all 0.15s ease;
      z-index: 20;
    }}
    .fullscreen-btn:hover {{
      background: var(--primary);
      border-color: var(--primary);
    }}

    /* BOTÃO DISCRETO PARA VOLTAR DA TELA CHEIA */
    .fs-exit-btn {{
      display: none;
      position: absolute;
      top: 14px;
      right: 14px;
      top: max(14px, env(safe-area-inset-top, 14px));
      right: max(14px, env(safe-area-inset-right, 14px));
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(18, 19, 22, 0.72);
      border: 1px solid rgba(255, 255, 255, 0.24);
      color: rgba(255, 255, 255, 0.88);
      cursor: pointer;
      z-index: 100;
      align-items: center;
      justify-content: center;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
      padding: 0;
    }}
    .fs-exit-btn:hover {{
      background: rgba(30, 41, 59, 0.92);
      border-color: rgba(255, 255, 255, 0.5);
      color: #fff;
      transform: scale(1.06);
    }}
    .fs-exit-btn:active {{
      transform: scale(0.92);
      background: rgba(239, 68, 68, 0.85);
    }}

    /* BOTÃO DE VELOCIDADE EM TELA CHEIA */
    .fs-speed-btn {{
      display: none;
      position: absolute;
      top: 14px;
      right: 64px;
      top: max(14px, env(safe-area-inset-top, 14px));
      right: max(64px, env(safe-area-inset-right, 64px));
      height: 40px;
      padding: 0 13px;
      border-radius: var(--radius-pill);
      background: rgba(18, 19, 22, 0.78);
      border: 1px solid rgba(255, 255, 255, 0.24);
      color: #93c5fd;
      font-weight: 700;
      font-size: 0.85rem;
      cursor: pointer;
      z-index: 100;
      align-items: center;
      justify-content: center;
      gap: 6px;
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
    }}
    .fs-speed-btn:hover {{
      background: rgba(30, 41, 59, 0.95);
      border-color: var(--primary);
      color: #fff;
      transform: scale(1.05);
    }}
    .fs-speed-btn:active {{
      transform: scale(0.95);
    }}
    .fs-speed-btn.speed-modified {{
      border-color: rgba(48, 131, 255, 0.8);
      color: #60a5fa;
      box-shadow: 0 0 12px rgba(48, 131, 255, 0.35);
    }}

    /* FULLSCREEN SEM AVISOS INTRUSIVOS */
    .visual-box.is-fullscreen,
    .visual-box:fullscreen,
    .visual-box:-webkit-full-screen {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      width: 100dvw;
      height: 100vh;
      height: 100dvh;
      max-height: none !important;
      border: none;
      border-radius: 0;
      background: #000;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 99999;
      box-sizing: border-box;
    }}
    .visual-box::backdrop {{
      background: #000;
    }}
    .visual-box::-webkit-backdrop {{
      background: #000;
    }}
    .visual-box:fullscreen img,
    .visual-box:-webkit-full-screen img,
    .visual-box.is-fullscreen img {{
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      max-height: none !important;
      object-fit: contain;
      cursor: pointer;
    }}
    .visual-box:fullscreen .fullscreen-btn,
    .visual-box:-webkit-full-screen .fullscreen-btn,
    .visual-box.is-fullscreen .fullscreen-btn {{
      display: none !important;
    }}
    .visual-box:fullscreen .fs-exit-btn,
    .visual-box:-webkit-full-screen .fs-exit-btn,
    .visual-box.is-fullscreen .fs-exit-btn,
    .visual-box:fullscreen .fs-speed-btn,
    .visual-box:-webkit-full-screen .fs-speed-btn,
    .visual-box.is-fullscreen .fs-speed-btn {{
      display: flex !important;
      opacity: 0;
      pointer-events: none;
      visibility: hidden;
      transition: opacity 0.25s ease, visibility 0.25s ease, transform 0.2s ease;
    }}
    /* APARECEM SOMENTE AO PAUSAR EM TELA CHEIA */
    .visual-box.is-fullscreen.is-paused .fs-exit-btn,
    .visual-box.is-fullscreen.is-paused .fs-speed-btn,
    .visual-box:fullscreen.is-paused .fs-exit-btn,
    .visual-box:fullscreen.is-paused .fs-speed-btn,
    .visual-box:-webkit-full-screen.is-paused .fs-exit-btn,
    .visual-box:-webkit-full-screen.is-paused .fs-speed-btn {{
      opacity: 1 !important;
      pointer-events: auto !important;
      visibility: visible !important;
    }}
    .fs-hud {{
      display: none !important;
    }}

    /* SCRIPT BOX */
    .script-box {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 25px -5px rgba(0,0,0,0.3);
      position: relative;
      height: 100%;
      max-height: 100%;
      min-height: 0;
      overflow: hidden;
    }}
    .script-header {{
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      color: var(--primary);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-shrink: 0;
    }}
    .script-header-badge {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .script-text {{
      font-size: 1.05rem;
      line-height: 1.7;
      color: #e2e8f0;
      overflow-y: auto;
      white-space: pre-wrap;
      flex: 1;
      min-height: 0;
      padding-right: 6px;
    }}

    /* CONTROLES MOBILE INLINE (APARECEM APENAS NO CELULAR ABAIXO DO SLIDE) */
    .mobile-player-bar {{
      display: none;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 10px 14px;
      flex-direction: column;
      gap: 8px;
      flex-shrink: 0;
    }}
    .mobile-controls-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }}
    .mobile-btn-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* FOOTER (DESKTOP) */
    footer {{
      background: var(--bg-card);
      border-top: 1px solid var(--border);
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-shrink: 0;
      z-index: 30;
    }}
    .controls {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    button.btn-ctrl {{
      background: var(--bg-surface);
      color: white;
      border: 1px solid var(--border);
      padding: 8px 16px;
      border-radius: var(--radius-md);
      cursor: pointer;
      font-weight: 600;
      font-size: 0.88rem;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}
    button.btn-ctrl:hover {{
      background: var(--bg-surface-hover);
      border-color: var(--border-strong);
    }}
    /* BOTÕES DE PLAY/PAUSE (DESIGN SYSTEM HERO ACTION) */
    button.btn-ctrl.primary {{
      background: linear-gradient(135deg, #3083FF 0%, #155DFC 100%);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      box-shadow: 0 4px 14px rgba(48, 131, 255, 0.38), inset 0 1px 0 rgba(255, 255, 255, 0.25);
      font-weight: 700;
      letter-spacing: 0.01em;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }}
    button.btn-ctrl.primary:hover {{
      background: linear-gradient(135deg, #4491FF 0%, #1F66FF 100%);
      border-color: rgba(255, 255, 255, 0.35);
      box-shadow: 0 6px 20px rgba(48, 131, 255, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.35);
      transform: translateY(-1px);
    }}
    button.btn-ctrl.primary:active {{
      transform: translateY(1px) scale(0.98);
      box-shadow: 0 2px 8px rgba(48, 131, 255, 0.4);
    }}

    /* ESTADO EM REPRODUÇÃO ATIVA (IS-PLAYING / PAUSAR) */
    button.btn-ctrl.primary.is-playing {{
      background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
      border-color: rgba(254, 243, 199, 0.3);
      box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.25);
      animation: audioPulse 2.4s infinite ease-in-out;
    }}
    button.btn-ctrl.primary.is-playing:hover {{
      background: linear-gradient(135deg, #fbbf24 0%, #b45309 100%);
      border-color: rgba(254, 243, 199, 0.45);
      box-shadow: 0 6px 22px rgba(245, 158, 11, 0.55);
      transform: translateY(-1px);
    }}

    @keyframes audioPulse {{
      0%, 100% {{
        box-shadow: 0 4px 14px rgba(245, 158, 11, 0.38);
      }}
      50% {{
        box-shadow: 0 4px 22px rgba(245, 158, 11, 0.65);
      }}
    }}
    /* CONTROLE AVANÇADO DE VELOCIDADE (TSM / DSP) */
    button.btn-speed {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: #93c5fd;
      padding: 6px 11px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.2s ease;
      user-select: none;
    }}
    button.btn-speed:hover,
    button.btn-speed.active {{
      background: var(--primary-light);
      border-color: var(--primary);
      color: #fff;
    }}
    button.btn-speed.speed-modified {{
      background: rgba(48, 131, 255, 0.16);
      border-color: rgba(48, 131, 255, 0.55);
      color: #60a5fa;
      box-shadow: 0 0 10px rgba(48, 131, 255, 0.2);
    }}
    .speed-chevron {{
      font-size: 0.65rem;
      opacity: 0.75;
      margin-left: 2px;
      transition: transform 0.2s ease;
    }}
    button.btn-speed.active .speed-chevron {{
      transform: rotate(180deg);
    }}

    /* BACKDROP DO MENU DE VELOCIDADE */
    .speed-menu-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 998;
      display: none;
      background: rgba(0, 0, 0, 0.45);
      backdrop-filter: blur(2px);
      -webkit-backdrop-filter: blur(2px);
    }}
    .speed-menu-backdrop.active {{
      display: block;
    }}

    /* POPOVER MENU DE VELOCIDADE */
    .speed-popover {{
      position: fixed;
      z-index: 1000;
      width: 280px;
      background: rgba(18, 19, 22, 0.96);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      padding: 14px 16px;
      box-shadow: 0 18px 48px rgba(0, 0, 0, 0.8), 0 0 20px rgba(48, 131, 255, 0.12);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
      transform: translateY(8px) scale(0.96);
      transition: opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1), transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.2s;
    }}
    .speed-popover.open {{
      opacity: 1;
      visibility: visible;
      pointer-events: auto;
      transform: translateY(0) scale(1);
    }}

    .speed-popover-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 9px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 11px;
    }}
    .speed-popover-title {{
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}
    .speed-popover-title span:first-child {{
      font-size: 0.84rem;
      font-weight: 700;
      color: var(--text-main);
    }}
    .pitch-badge {{
      font-size: 0.67rem;
      color: var(--brand-green);
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .speed-menu-close {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.95rem;
      padding: 4px 6px;
      border-radius: var(--radius-sm);
      line-height: 1;
      transition: all 0.15s;
    }}
    .speed-menu-close:hover {{
      color: #fff;
      background: rgba(255, 255, 255, 0.1);
    }}

    /* GRID DE PRESETS */
    .speed-presets-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      margin-bottom: 12px;
    }}
    .speed-preset-btn {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text-muted);
      font-weight: 600;
      font-size: 0.8rem;
      padding: 7px 4px;
      border-radius: var(--radius-sm);
      cursor: pointer;
      text-align: center;
      transition: all 0.15s ease;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }}
    .speed-preset-btn span {{
      display: block;
      font-size: 0.6rem;
      color: var(--text-dim);
      font-weight: 400;
      line-height: 1;
      margin-top: 2px;
    }}
    .speed-preset-btn:hover {{
      background: var(--bg-surface-hover);
      border-color: rgba(255, 255, 255, 0.22);
      color: #fff;
    }}
    .speed-preset-btn.active {{
      background: var(--primary);
      border-color: var(--primary);
      color: #fff;
      box-shadow: 0 2px 10px rgba(48, 131, 255, 0.45);
    }}
    .speed-preset-btn.active span {{
      color: rgba(255, 255, 255, 0.9);
    }}

    /* AJUSTE FINO (STEPPER + RANGE) */
    .speed-stepper-row {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 9px 11px;
      margin-bottom: 11px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .stepper-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.74rem;
      color: var(--text-muted);
    }}
    .fine-speed-display {{
      font-family: monospace;
      font-weight: 700;
      color: #93c5fd;
      font-size: 0.85rem;
    }}
    .stepper-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .stepper-btn {{
      width: 26px;
      height: 26px;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--text-main);
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 1rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
      transition: all 0.15s;
    }}
    .stepper-btn:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
      color: #fff;
    }}
    .speed-range-slider {{
      flex: 1;
      accent-color: var(--primary);
      cursor: pointer;
      height: 4px;
    }}

    /* RODAPÉ DO POPOVER */
    .speed-popover-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 8px;
      border-top: 1px solid var(--border);
      font-size: 0.72rem;
      color: var(--text-dim);
    }}
    .speed-shortcut-hint b {{
      color: var(--text-muted);
    }}
    .speed-reset-btn {{
      background: transparent;
      border: none;
      color: #93c5fd;
      font-size: 0.72rem;
      cursor: pointer;
      text-decoration: underline;
      padding: 2px 4px;
      transition: color 0.15s;
    }}
    .speed-reset-btn:hover {{
      color: #fff;
    }}

    /* OSD (ON-SCREEN DISPLAY) PARA FEEDBACK DE VELOCIDADE */
    .speed-osd {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.85);
      background: rgba(10, 10, 12, 0.9);
      border: 1px solid rgba(48, 131, 255, 0.5);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.75), 0 0 20px rgba(48, 131, 255, 0.25);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-radius: var(--radius-lg);
      padding: 14px 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 4px;
      color: #fff;
      z-index: 120;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.22s ease, transform 0.22s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .speed-osd.visible {{
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }}
    .speed-osd-val-row {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .speed-osd-icon {{
      font-size: 1.4rem;
      color: #fbbf24;
    }}
    .speed-osd-text {{
      font-size: 1.5rem;
      font-weight: 800;
      letter-spacing: -0.5px;
      color: #93c5fd;
      font-family: monospace;
    }}
    .speed-osd-sub {{
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--brand-green);
      font-weight: 700;
    }}

    /* FEEDBACK VISUAL DE PLAY/PAUSE EM TELA CHEIA */
    .fs-play-osd {{
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.65);
      background: rgba(10, 10, 12, 0.88);
      border: 1px solid rgba(255, 255, 255, 0.22);
      box-shadow: 0 10px 36px rgba(0, 0, 0, 0.82), 0 0 24px rgba(48, 131, 255, 0.35);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-radius: 50%;
      width: 88px;
      height: 88px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      z-index: 125;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease, transform 0.22s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    .fs-play-osd.visible {{
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }}
    .fs-play-osd-icon {{
      color: #93c5fd;
      line-height: 1;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .fs-play-osd.is-paused .fs-play-osd-icon {{
      color: #f3f4f6;
    }}

    /* PROGRESS BAR */
    .playback-info {{
      display: flex;
      align-items: center;
      gap: 14px;
      flex: 1;
    }}
    .time-display {{
      font-size: 0.82rem;
      color: var(--text-muted);
      font-family: monospace;
      min-width: 42px;
    }}
    .progress-bar-container {{
      flex: 1;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-pill);
      position: relative;
      cursor: pointer;
      transition: height 0.15s ease;
    }}
    .progress-bar-container:hover {{
      height: 8px;
    }}
    .progress-bar {{
      height: 100%;
      background: var(--primary);
      border-radius: var(--radius-pill);
      width: 0%;
      position: relative;
      transition: width 0.1s linear;
    }}
    .progress-bar::after {{
      content: "";
      position: absolute;
      right: -4px;
      top: 50%;
      transform: translateY(-50%);
      width: 10px;
      height: 10px;
      background: #fff;
      border-radius: 50%;
      opacity: 0;
      transition: opacity 0.15s ease;
    }}
    .progress-bar-container:hover .progress-bar::after {{
      opacity: 1;
    }}

    /* WHATSAPP CTA BUTTON */
    .whatsapp-cta-btn {{
      background: var(--brand-green);
      color: #fff;
      border: none;
      padding: 9px 18px;
      border-radius: var(--radius-pill);
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(40, 199, 101, 0.35);
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .whatsapp-cta-btn:hover {{
      background: var(--brand-green-hover);
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(40, 199, 101, 0.45);
    }}
    .whatsapp-cta-btn svg {{
      width: 18px;
      height: 18px;
      flex-shrink: 0;
    }}

    /* SWITCH TOGGLE */
    .toggle-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.82rem;
      color: var(--text-muted);
      white-space: nowrap;
    }}
    .switch {{
      position: relative;
      display: inline-block;
      width: 40px;
      height: 22px;
    }}
    .switch input {{ opacity: 0; width: 0; height: 0; }}
    .slider {{
      position: absolute;
      cursor: pointer;
      top: 0; left: 0; right: 0; bottom: 0;
      background-color: #334155;
      transition: .3s;
      border-radius: 22px;
    }}
    .slider:before {{
      position: absolute;
      content: "";
      height: 16px;
      width: 16px;
      left: 3px;
      bottom: 3px;
      background-color: white;
      transition: .3s;
      border-radius: 50%;
    }}
    input:checked + .slider {{ background-color: var(--primary); }}
    input:checked + .slider:before {{ transform: translateX(18px); }}

    /* MOBILE FLOATING CTA BAR */
    .mobile-floating-bar {{
      display: none;
      background: rgba(18, 19, 22, 0.95);
      border-top: 1px solid var(--border);
      padding: 10px 14px;
      backdrop-filter: blur(12px);
      z-index: 30;
      flex-shrink: 0;
    }}
    .mobile-floating-bar .whatsapp-cta-btn {{
      width: 100%;
      justify-content: center;
      padding: 12px 18px;
      font-size: 0.95rem;
    }}

    /* RESPONSIVIDADE MOBILE (SMARTPHONES E TABLETS VERTICAIS) */
    @media (max-width: 850px) {{
      header {{
        padding: 8px 12px;
      }}
      .brand-title {{
        display: flex;
        font-size: 0.78rem;
        padding-left: 8px;
        gap: 6px;
      }}
      .partner-tag {{
        font-size: 0.65rem;
        padding: 2px 6px;
      }}
      .brand-logo-img {{
        height: 26px;
      }}
      .badge-tiago {{
        font-size: 0.72rem;
        padding: 3px 8px;
      }}
      @media (max-width: 520px) {{
        .badge-tiago {{
          display: none;
        }}
      }}
      .btn-drawer-toggle {{
        display: inline-flex;
      }}

      /* SIDEBAR VIRA DRAWER OFF-CANVAS */
      .sidebar {{
        position: fixed;
        top: 0;
        left: 0;
        bottom: 0;
        width: 82%;
        max-width: 340px;
        box-shadow: 10px 0 30px rgba(0,0,0,0.8);
        transform: translateX(-100%);
      }}
      .sidebar.open {{
        transform: translateX(0);
      }}
      .sidebar-close-btn {{
        display: block;
      }}

      /* CONTENT AREA COMPACTA NO CELULAR */
      .content-area {{
        padding: 10px 10px 6px;
        gap: 8px;
      }}
      .visual-and-script {{
        display: flex;
        flex-direction: column;
        gap: 8px;
      }}

      /* SLIDE TRAVADO NO TOPO COM 16:9 PERFEITO */
      .visual-box {{
        width: 100%;
        aspect-ratio: 16 / 9;
        height: auto;
        max-height: 30vh;
        flex-shrink: 0;
        border-radius: var(--radius-md);
      }}
      .fullscreen-btn {{
        padding: 4px 8px;
        font-size: 0.72rem;
        top: 8px;
        right: 8px;
      }}

      /* CONTROLES MOBILE APARECEM */
      .mobile-player-bar {{
        display: flex;
      }}

      /* SCRIPT BOX NO CELULAR */
      .script-box {{
        padding: 12px 14px;
        border-radius: var(--radius-md);
      }}
      .script-header {{
        font-size: 0.75rem;
        margin-bottom: 8px;
      }}
      .script-text {{
        font-size: 0.95rem;
        line-height: 1.6;
        padding-right: 4px;
      }}

      /* AJUSTE RESPONSIVO DO MENU DE VELOCIDADE */
      .speed-popover {{
        position: fixed !important;
        left: 50% !important;
        right: auto !important;
        transform: translateX(-50%) translateY(12px) scale(0.97) !important;
        width: calc(100vw - 28px) !important;
        max-width: 340px !important;
        bottom: max(20px, env(safe-area-inset-bottom, 20px)) !important;
        top: auto !important;
      }}
      .speed-popover.open {{
        transform: translateX(-50%) translateY(0) scale(1) !important;
      }}

      /* FOOTER TRADICIONAL É SUBSTITUÍDO PELO FLOATING BAR */
      footer {{
        display: none;
      }}
      .mobile-floating-bar {{
        display: block;
      }}
    }}
  </style>
</head>
<body>
  <!-- HEADER COM LOGO OFICIAL BOTCONVERSA -->
  <header>
    <div class="brand-wrap">
      <img src="{logo_data_uri}" alt="BotConversa Logo" class="brand-logo-img">
      <div class="brand-title">
        <span>Apresentação 2026</span>
        <span class="partner-tag">Criado por Parceiro</span>
      </div>
    </div>
    <div class="header-actions">
      <button id="btnMobileDrawer" class="btn-drawer-toggle" title="Abrir Lista de Slides">
        📑 <span id="mobileSlideCount">Slide 1/84</span>
      </button>
      <div class="badge-tiago">
        🎙️ Voz: Tiago (BotConversa)
      </div>
    </div>
  </header>

  <!-- BACKDROP PARA FECHAR O MENU NO MOBILE -->
  <div id="drawerBackdrop" class="drawer-backdrop"></div>

  <main>
    <!-- LISTA LATERAL DE SLIDES (DESKTOP) / DRAWER (MOBILE) -->
    <div id="sidebar" class="sidebar">
      <div class="sidebar-header">
        <span>Slides da Apresentação (84)</span>
        <button id="btnCloseSidebar" class="sidebar-close-btn" title="Fechar menu">✕</button>
      </div>
      <div id="slideList" style="flex: 1; overflow-y: auto;"></div>
      <div class="sidebar-footer">
        Apresentação 2026 • Criado por Parceiro
      </div>
    </div>

    <!-- ÁREA PRINCIPAL -->
    <div class="content-area">
      <div class="visual-and-script">
        <!-- QUADRO DO SLIDE (TRAVADO E CENTRALIZADO) -->
        <div id="visualBox" class="visual-box">
          <button id="btnFsToggle" class="fullscreen-btn" title="Tela Cheia (F)">
            ⛶ Tela Cheia
          </button>
          <button id="btnFsSpeed" class="fs-speed-btn" title="Alternar Velocidade (Atalhos: < e >)">
            ⚡ <span id="fsSpeedVal">1.0x</span>
          </button>
          <button id="btnFsExit" class="fs-exit-btn" aria-label="Fechar tela cheia">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
          <div id="speedOsd" class="speed-osd" aria-live="polite">
            <div class="speed-osd-val-row">
              <span class="speed-osd-icon">⚡</span>
              <span id="speedOsdText" class="speed-osd-text">1.0x</span>
            </div>
            <span class="speed-osd-sub">Tom Preservado (TSM)</span>
          </div>
          <!-- FEEDBACK VISUAL DE PLAY/PAUSE EM TELA CHEIA (TOQUE NA TELA) -->
          <div id="fsPlayOsd" class="fs-play-osd" aria-hidden="true">
            <div id="fsPlayOsdIcon" class="fs-play-osd-icon">
              <svg width="34" height="34" viewBox="0 0 24 24" fill="currentColor">
                <polygon points="5 3 19 12 5 21 5 3"></polygon>
              </svg>
            </div>
          </div>
          <img id="slideImg" src="" alt="Slide da Apresentação">
        </div>

        <!-- CONTROLES MOBILE TOUCH (LOGO ABAIXO DO SLIDE) -->
        <div class="mobile-player-bar">
          <div class="mobile-controls-row">
            <div class="mobile-btn-group">
              <button id="btnMobPrev" class="btn-ctrl" title="Anterior">⏮️</button>
              <button id="btnMobPlay" class="btn-ctrl primary" title="Reproduzir">▶️ Play</button>
              <button id="btnMobNext" class="btn-ctrl" title="Próximo">⏭️</button>
            </div>
            <div class="mobile-btn-group">
              <button id="btnMobSpeed" class="btn-speed" title="Velocidade de reprodução (TSM)">⚡ <span id="mobSpeedVal">1.0x</span> <span class="speed-chevron">▾</span></button>
              <button id="btnMobFs" class="btn-ctrl" title="Tela Cheia">⛶</button>
            </div>
          </div>
          <div class="playback-info">
            <span id="mobTimeCurrent" class="time-display">00:00</span>
            <div id="mobProgressContainer" class="progress-bar-container">
              <div id="mobProgressBar" class="progress-bar"></div>
            </div>
            <span id="mobTimeDuration" class="time-display">00:00</span>
          </div>
        </div>

        <!-- QUADRO DA TRANSCRIÇÃO DA APRESENTAÇÃO (ROLAGEM INDEPENDENTE) -->
        <div class="script-box">
          <div class="script-header">
            <div class="script-header-badge">
              <span>Transcrição da Apresentação</span>
            </div>
            <span id="slideIndicatorHeader" style="color: var(--text-muted); font-size: 0.78rem;">1 / 84</span>
          </div>
          <div id="scriptContent" class="script-text"></div>
        </div>
      </div>
    </div>
  </main>

  <!-- FLOATING CTA BAR (MOBILE) -->
  <div class="mobile-floating-bar">
    <a id="btnMobWhatsApp" href="https://wa.me/554988110688?text=Ol%C3%A1!%20Assisti%20a%20apresenta%C3%A7%C3%A3o%20de%20vendas%20do%20BotConversa%20com%20o%20Tiago%20e%20gostaria%20de%20conversar%20sobre%20a%20minha%20decis%C3%A3o." target="_blank" class="whatsapp-cta-btn">
      <svg fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"></path></svg>
      <span>Responder no WhatsApp com Decisão</span>
    </a>
  </div>

  <!-- BACKDROP E POPOVER DE VELOCIDADE (0.75x, 1x, 1.25x, 1.5x) -->
  <div id="speedMenuBackdrop" class="speed-menu-backdrop"></div>
  <div id="speedMenu" class="speed-popover" role="dialog" aria-label="Opções de Velocidade de Reprodução">
    <div class="speed-popover-header">
      <div class="speed-popover-title">
        <span>Velocidade de Reprodução</span>
        <span class="pitch-badge" title="Time-Scale Modification (TSM): Preserva o tom natural da voz sem distorção">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9 18V5l12-2v13"></path><circle cx="6" cy="18" r="3"></circle><circle cx="18" cy="16" r="3"></circle></svg>
          Tom Natural Preservado
        </span>
      </div>
      <button id="btnCloseSpeedMenu" class="speed-menu-close" title="Fechar menu">✕</button>
    </div>

    <!-- PRESETS EXCLUSIVOS: 0.75x, 1x, 1.25x, 1.5x -->
    <div class="speed-presets-grid">
      <button type="button" class="speed-preset-btn" data-speed="0.75">0.75x</button>
      <button type="button" class="speed-preset-btn active" data-speed="1.0">1.0x <span>Normal</span></button>
      <button type="button" class="speed-preset-btn" data-speed="1.25">1.25x</button>
      <button type="button" class="speed-preset-btn" data-speed="1.5">1.5x</button>
    </div>

    <!-- RODAPÉ E ATALHOS -->
    <div class="speed-popover-footer">
      <span class="speed-shortcut-hint">Atalhos: <b>&lt;</b> e <b>&gt;</b></span>
      <button type="button" id="btnResetSpeed" class="speed-reset-btn" title="Redefinir para 1.0x">Padrão (1.0x)</button>
    </div>
  </div>

  <!-- FOOTER (DESKTOP) -->
  <footer>
    <div class="controls">
      <button id="btnPrev" class="btn-ctrl">⏮️ Anterior</button>
      <button id="btnPlay" class="btn-ctrl primary">▶️ Reproduzir Áudio</button>
      <button id="btnNext" class="btn-ctrl">⏭️ Próximo</button>
      <button id="btnSpeed" class="btn-speed" title="Velocidade de reprodução (Clique para menu ou use atalhos < e >)">
        <span>⚡</span>
        <span id="speedValue">1.0x</span>
        <span class="speed-chevron">▾</span>
      </button>
    </div>

    <div class="playback-info">
      <span id="timeCurrent" class="time-display">00:00</span>
      <div id="progressContainer" class="progress-bar-container">
        <div id="progressBar" class="progress-bar"></div>
      </div>
      <span id="timeDuration" class="time-display">00:00</span>
    </div>

    <div class="controls" style="gap: 16px;">
      <div class="toggle-group">
        <label class="switch">
          <input type="checkbox" id="autoAdvance" checked>
          <span class="slider"></span>
        </label>
        <span>Auto Avanço</span>
      </div>

      <span class="desk-partner-note">Criado por Parceiro</span>

      <a id="btnDeskWhatsApp" href="https://wa.me/554988110688?text=Ol%C3%A1!%20Assisti%20a%20apresenta%C3%A7%C3%A3o%20de%20vendas%20do%20BotConversa%20com%20o%20Tiago%20e%20gostaria%20de%20conversar%20sobre%20a%20minha%20decis%C3%A3o." target="_blank" class="whatsapp-cta-btn">
        <svg fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"></path></svg>
        <span>Falar no WhatsApp</span>
      </a>
    </div>
  </footer>

  <audio id="audioPlayer" preload="auto"></audio>

  <script>
    const slidesData = {slides_json};
    let currentIdx = 0;
    let currentSpeed = 1.0;
    try {{
      const savedSpeed = localStorage.getItem('botconversa_playback_speed');
      if (savedSpeed) {{
        const parsed = parseFloat(savedSpeed);
        if (speedPresets.includes(parsed)) {{
          currentSpeed = parsed;
        }}
      }}
    }} catch (e) {{}}

    const speedPresets = [0.75, 1.0, 1.25, 1.5];

    // Elementos DOM
    const audioPlayer = document.getElementById('audioPlayer');
    const slideImg = document.getElementById('slideImg');
    const scriptContent = document.getElementById('scriptContent');
    const slideList = document.getElementById('slideList');
    const sidebar = document.getElementById('sidebar');
    const drawerBackdrop = document.getElementById('drawerBackdrop');
    const visualBox = document.getElementById('visualBox');

    // Botões e textos Desktop
    const btnPlay = document.getElementById('btnPlay');
    const btnPrev = document.getElementById('btnPrev');
    const btnNext = document.getElementById('btnNext');
    const btnSpeed = document.getElementById('btnSpeed');
    const speedValue = document.getElementById('speedValue');
    const mobSpeedVal = document.getElementById('mobSpeedVal');
    const fsSpeedVal = document.getElementById('fsSpeedVal');
    const btnFsSpeed = document.getElementById('btnFsSpeed');
    const speedMenu = document.getElementById('speedMenu');
    const speedMenuBackdrop = document.getElementById('speedMenuBackdrop');
    const btnCloseSpeedMenu = document.getElementById('btnCloseSpeedMenu');
    const presetBtns = document.querySelectorAll('.speed-preset-btn');
    const speedSlider = document.getElementById('speedSlider');
    const fineSpeedDisplay = document.getElementById('fineSpeedDisplay');
    const btnSpeedMinus = document.getElementById('btnSpeedMinus');
    const btnSpeedPlus = document.getElementById('btnSpeedPlus');
    const btnResetSpeed = document.getElementById('btnResetSpeed');
    const speedOsd = document.getElementById('speedOsd');
    const speedOsdText = document.getElementById('speedOsdText');
    const fsPlayOsd = document.getElementById('fsPlayOsd');
    const fsPlayOsdIcon = document.getElementById('fsPlayOsdIcon');
    const btnFullscreen = document.getElementById('btnFullscreen');
    const autoAdvanceCheckbox = document.getElementById('autoAdvance');
    const progressBar = document.getElementById('progressBar');
    const progressContainer = document.getElementById('progressContainer');
    const timeCurrent = document.getElementById('timeCurrent');
    const timeDuration = document.getElementById('timeDuration');

    // Botões e textos Mobile
    const btnMobPlay = document.getElementById('btnMobPlay');
    const btnMobPrev = document.getElementById('btnMobPrev');
    const btnMobNext = document.getElementById('btnMobNext');
    const btnMobSpeed = document.getElementById('btnMobSpeed');
    const btnMobFs = document.getElementById('btnMobFs');
    const btnMobileDrawer = document.getElementById('btnMobileDrawer');
    const btnCloseSidebar = document.getElementById('btnCloseSidebar');
    const mobileSlideCount = document.getElementById('mobileSlideCount');
    const slideIndicatorHeader = document.getElementById('slideIndicatorHeader');
    const mobProgressBar = document.getElementById('mobProgressBar');
    const mobProgressContainer = document.getElementById('mobProgressContainer');
    const mobTimeCurrent = document.getElementById('mobTimeCurrent');
    const mobTimeDuration = document.getElementById('mobTimeDuration');

    // HUD Tela cheia
    const btnFsToggle = document.getElementById('btnFsToggle');
    const btnFsPrev = document.getElementById('btnFsPrev');
    const btnFsPlay = document.getElementById('btnFsPlay');
    const btnFsNext = document.getElementById('btnFsNext');
    const btnFsExit = document.getElementById('btnFsExit');
    const fsHudTitle = document.getElementById('fsHudTitle');

    function renderSlideList() {{
      slideList.innerHTML = '';
      slidesData.forEach((s, idx) => {{
        const item = document.createElement('div');
        item.className = `slide-item ${{idx === currentIdx ? 'active' : ''}}`;
        const titleText = s.title || ('Slide ' + s.slide_number);
        item.innerHTML = `
          <div class="slide-badge">${{s.slide_number}}</div>
          <div class="slide-info" title="${{titleText}}">${{titleText}}</div>
        `;
        item.onclick = () => {{
          loadSlide(idx, true);
          closeDrawer();
        }};
        slideList.appendChild(item);
      }});
    }}

    function loadSlide(idx, autoplay = false) {{
      currentIdx = idx;
      const s = slidesData[idx];
      const padNum = String(s.slide_number).padStart(3, '0');
      const padAudio = String(s.slide_number).padStart(2, '0');

      slideImg.src = `frames_2026/slide_${{padNum}}.png?v=11`;
      scriptContent.textContent = s.script_tiago;
      scriptContent.scrollTop = 0;

      const slideTitleStr = `${{s.slide_number}}/84 • ${{s.title || 'Slide ' + s.slide_number}}`;
      if (fsHudTitle) fsHudTitle.textContent = slideTitleStr;
      mobileSlideCount.textContent = `Slide ${{s.slide_number}}/84`;
      slideIndicatorHeader.textContent = `${{s.slide_number}} / 84`;

      audioPlayer.src = `audios_tiago_2026/Slide_${{padAudio}}.mp3?v=2`;
      audioPlayer.playbackRate = currentSpeed;
      enforcePitchPreservation();

      renderSlideList();
      const activeEl = slideList.children[idx];
      if (activeEl) activeEl.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});

      if (autoplay) {{
        audioPlayer.play().then(() => {{
          updatePlayButtonsState(true);
        }}).catch(() => {{
          updatePlayButtonsState(false);
        }});
      }} else {{
        updatePlayButtonsState(false);
      }}

      progressBar.style.width = '0%';
      if (mobProgressBar) mobProgressBar.style.width = '0%';
      timeCurrent.textContent = '00:00';
      if (mobTimeCurrent) mobTimeCurrent.textContent = '00:00';
    }}

    function updatePlayButtonsState(isPlaying) {{
      const playText = isPlaying ? '⏸️ Pausar' : '▶️ Reproduzir';
      const mobPlayText = isPlaying ? '⏸️ Pause' : '▶️ Play';
      btnPlay.textContent = playText;
      btnMobPlay.textContent = mobPlayText;
      if (btnFsPlay) btnFsPlay.textContent = isPlaying ? '⏸️' : '▶️';

      if (isPlaying) {{
        btnPlay.classList.add('is-playing');
        btnMobPlay.classList.add('is-playing');
        visualBox.classList.remove('is-paused');
        if (typeof closeSpeedMenu === 'function') closeSpeedMenu();
      }} else {{
        btnPlay.classList.remove('is-playing');
        btnMobPlay.classList.remove('is-playing');
        visualBox.classList.add('is-paused');
      }}
    }}

    function togglePlay() {{
      if (audioPlayer.paused) {{
        audioPlayer.play().then(() => {{
          updatePlayButtonsState(true);
        }}).catch(err => console.error(err));
      }} else {{
        audioPlayer.pause();
        updatePlayButtonsState(false);
      }}
    }}

    function nextSlide(autoplay = false) {{
      if (currentIdx < slidesData.length - 1) {{
        loadSlide(currentIdx + 1, autoplay);
      }}
    }}

    function prevSlide(autoplay = false) {{
      if (currentIdx > 0) {{
        loadSlide(currentIdx - 1, autoplay);
      }}
    }}

    // Feedback visual animado de Play / Pause no centro da tela cheia
    let fsPlayOsdTimeout = null;
    function showPlayPauseFeedback(isPlaying) {{
      if (!fsPlayOsd || !fsPlayOsdIcon) return;
      if (isPlaying) {{
        fsPlayOsd.classList.remove('is-paused');
        fsPlayOsdIcon.innerHTML = `
          <svg width="36" height="36" viewBox="0 0 24 24" fill="currentColor">
            <polygon points="6 4 20 12 6 20 6 4"></polygon>
          </svg>`;
      }} else {{
        fsPlayOsd.classList.add('is-paused');
        fsPlayOsdIcon.innerHTML = `
          <svg width="36" height="36" viewBox="0 0 24 24" fill="currentColor">
            <rect x="6" y="4" width="4" height="16" rx="1.5"></rect>
            <rect x="14" y="4" width="4" height="16" rx="1.5"></rect>
          </svg>`;
      }}
      fsPlayOsd.classList.add('visible');
      if (fsPlayOsdTimeout) clearTimeout(fsPlayOsdTimeout);
      fsPlayOsdTimeout = setTimeout(() => {{
        fsPlayOsd.classList.remove('visible');
      }}, 650);
    }}

    // Garantia de Preservação de Tom Digital (Time-Scale Modification - TSM)
    function enforcePitchPreservation() {{
      if (!audioPlayer) return;
      audioPlayer.preservesPitch = true;
      if ('webkitPreservesPitch' in audioPlayer) audioPlayer.webkitPreservesPitch = true;
      if ('mozPreservesPitch' in audioPlayer) audioPlayer.mozPreservesPitch = true;
    }}

    let osdTimeout = null;
    function triggerSpeedOsd(spd) {{
      if (!speedOsd) return;
      const formatted = spd.toFixed(spd % 1 === 0 ? 1 : 2) + 'x';
      if (speedOsdText) speedOsdText.textContent = formatted;
      speedOsd.classList.add('visible');
      if (osdTimeout) clearTimeout(osdTimeout);
      osdTimeout = setTimeout(() => {{
        speedOsd.classList.remove('visible');
      }}, 950);
    }}

    function applyPlaybackSpeed(speed, showOsd = true) {{
      if (!speedPresets.includes(speed)) {{
        speed = speedPresets.reduce((prev, curr) => Math.abs(curr - speed) < Math.abs(prev - speed) ? curr : prev);
      }}
      currentSpeed = speed;

      // 1. Aplicação nativa com Time-Scale Modification (TSM)
      audioPlayer.playbackRate = currentSpeed;
      enforcePitchPreservation();

      // 2. Persistência de preferência
      try {{
        localStorage.setItem('botconversa_playback_speed', currentSpeed.toString());
      }} catch (e) {{}}

      // 3. Atualização de todos os indicadores visuais
      updateSpeedUI(currentSpeed);

      // 4. Feedback OSD no slide
      if (showOsd) {{
        triggerSpeedOsd(currentSpeed);
      }}
    }}

    function updateSpeedUI(spd) {{
      const formatted = spd.toFixed(spd % 1 === 0 ? 1 : 2) + 'x';
      const fineFormatted = spd.toFixed(2) + 'x';

      if (speedValue) speedValue.textContent = formatted;
      if (mobSpeedVal) mobSpeedVal.textContent = formatted;
      if (fsSpeedVal) fsSpeedVal.textContent = formatted;
      if (fineSpeedDisplay) fineSpeedDisplay.textContent = fineFormatted;
      if (speedSlider) speedSlider.value = spd;

      presetBtns.forEach(btn => {{
        const bSpeed = parseFloat(btn.dataset.speed);
        if (Math.abs(bSpeed - spd) < 0.04) {{
          btn.classList.add('active');
        }} else {{
          btn.classList.remove('active');
        }}
      }});

      if (spd !== 1.0) {{
        btnSpeed.classList.add('speed-modified');
        if (btnMobSpeed) btnMobSpeed.classList.add('speed-modified');
        if (btnFsSpeed) btnFsSpeed.classList.add('speed-modified');
      }} else {{
        btnSpeed.classList.remove('speed-modified');
        if (btnMobSpeed) btnMobSpeed.classList.remove('speed-modified');
        if (btnFsSpeed) btnFsSpeed.classList.remove('speed-modified');
      }}
    }}

    function openSpeedMenu(anchorEl) {{
      if (anchorEl) {{
        const rect = anchorEl.getBoundingClientRect();
        const popoverWidth = 280;
        const isMobile = window.innerWidth <= 850;

        if (isMobile) {{
          speedMenu.style.left = '50%';
          speedMenu.style.transform = 'translateX(-50%)';
          speedMenu.style.bottom = 'max(20px, env(safe-area-inset-bottom, 20px))';
          speedMenu.style.top = 'auto';
        }} else {{
          let left = rect.left + (rect.width / 2) - (popoverWidth / 2);
          if (left < 16) left = 16;
          if (left + popoverWidth > window.innerWidth - 16) left = window.innerWidth - popoverWidth - 16;
          speedMenu.style.left = `${{left}}px`;
          speedMenu.style.bottom = `${{window.innerHeight - rect.top + 10}}px`;
          speedMenu.style.top = 'auto';
          speedMenu.style.transform = 'none';
        }}
      }}
      speedMenu.classList.add('open');
      speedMenuBackdrop.classList.add('active');
      btnSpeed.classList.add('active');
    }}

    function closeSpeedMenu() {{
      speedMenu.classList.remove('open');
      speedMenuBackdrop.classList.remove('active');
      btnSpeed.classList.remove('active');
    }}

    function toggleSpeedMenu(anchorEl) {{
      if (speedMenu.classList.contains('open')) {{
        closeSpeedMenu();
      }} else {{
        openSpeedMenu(anchorEl);
      }}
    }}

    function stepSpeedPreset(dir) {{
      const idx = speedPresets.indexOf(currentSpeed);
      let targetIdx;
      if (idx === -1) {{
        targetIdx = 1; // 1.0x
      }} else if (dir > 0) {{
        targetIdx = Math.min(speedPresets.length - 1, idx + 1);
      }} else {{
        targetIdx = Math.max(0, idx - 1);
      }}
      applyPlaybackSpeed(speedPresets[targetIdx], true);
    }}

    function cycleSpeed() {{
      const idx = speedPresets.indexOf(currentSpeed);
      const nextIdx = idx === -1 ? 1 : (idx + 1) % speedPresets.length;
      applyPlaybackSpeed(speedPresets[nextIdx], true);
    }}

    function openDrawer() {{
      sidebar.classList.add('open');
      drawerBackdrop.classList.add('active');
    }}

    function closeDrawer() {{
      sidebar.classList.remove('open');
      drawerBackdrop.classList.remove('active');
    }}

    // Formatação de tempo mm:ss
    function formatTime(sec) {{
      if (isNaN(sec) || sec === Infinity) return '00:00';
      const m = Math.floor(sec / 60);
      const s = Math.floor(sec % 60);
      return `${{String(m).padStart(2, '0')}}:${{String(s).padStart(2, '0')}}`;
    }}

    // Atualização de progresso do áudio
    audioPlayer.addEventListener('timeupdate', () => {{
      const cur = audioPlayer.currentTime;
      const dur = audioPlayer.duration;
      if (dur > 0) {{
        const pct = (cur / dur) * 100;
        progressBar.style.width = `${{pct}}%`;
        if (mobProgressBar) mobProgressBar.style.width = `${{pct}}%`;
        timeCurrent.textContent = formatTime(cur);
        timeDuration.textContent = formatTime(dur);
        if (mobTimeCurrent) mobTimeCurrent.textContent = formatTime(cur);
        if (mobTimeDuration) mobTimeDuration.textContent = formatTime(dur);
      }}
    }});

    audioPlayer.addEventListener('loadedmetadata', () => {{
      audioPlayer.playbackRate = currentSpeed;
      enforcePitchPreservation();
      timeDuration.textContent = formatTime(audioPlayer.duration);
      if (mobTimeDuration) mobTimeDuration.textContent = formatTime(audioPlayer.duration);
    }});

    audioPlayer.addEventListener('play', () => {{
      audioPlayer.playbackRate = currentSpeed;
      enforcePitchPreservation();
      updatePlayButtonsState(true);
    }});
    audioPlayer.addEventListener('pause', () => {{
      updatePlayButtonsState(false);
    }});

    audioPlayer.addEventListener('ended', () => {{
      updatePlayButtonsState(false);
      if (autoAdvanceCheckbox && autoAdvanceCheckbox.checked) {{
        if (currentIdx < slidesData.length - 1) {{
          nextSlide(true);
        }}
      }}
    }});

    // Scrub de progresso
    function handleSeek(e, container) {{
      const rect = container.getBoundingClientRect();
      const pos = (e.clientX - rect.left) / rect.width;
      if (audioPlayer.duration) {{
        audioPlayer.currentTime = pos * audioPlayer.duration;
      }}
    }}
    progressContainer.addEventListener('click', (e) => handleSeek(e, progressContainer));
    if (mobProgressContainer) {{
      mobProgressContainer.addEventListener('click', (e) => handleSeek(e, mobProgressContainer));
    }}

    // Eventos Desktop
    btnPlay.addEventListener('click', togglePlay);
    btnPrev.addEventListener('click', () => prevSlide(true));
    btnNext.addEventListener('click', () => nextSlide(true));
    
    btnSpeed.addEventListener('click', (e) => {{
      e.stopPropagation();
      toggleSpeedMenu(btnSpeed);
    }});
    btnSpeed.addEventListener('contextmenu', (e) => {{
      e.preventDefault();
      cycleSpeed();
    }});

    // Eventos Mobile
    btnMobPlay.addEventListener('click', togglePlay);
    btnMobPrev.addEventListener('click', () => prevSlide(true));
    btnMobNext.addEventListener('click', () => nextSlide(true));
    btnMobSpeed.addEventListener('click', (e) => {{
      e.stopPropagation();
      toggleSpeedMenu(btnMobSpeed);
    }});

    if (btnFsSpeed) {{
      btnFsSpeed.addEventListener('click', (e) => {{
        e.stopPropagation();
        cycleSpeed();
      }});
      btnFsSpeed.addEventListener('contextmenu', (e) => {{
        e.preventDefault();
        toggleSpeedMenu(btnFsSpeed);
      }});
    }}

    if (btnCloseSpeedMenu) btnCloseSpeedMenu.addEventListener('click', closeSpeedMenu);
    if (speedMenuBackdrop) speedMenuBackdrop.addEventListener('click', closeSpeedMenu);

    presetBtns.forEach(btn => {{
      btn.addEventListener('click', () => {{
        const spd = parseFloat(btn.dataset.speed);
        applyPlaybackSpeed(spd, true);
        closeSpeedMenu();
      }});
    }});

    if (speedSlider) {{
      speedSlider.addEventListener('input', (e) => {{
        const val = parseFloat(e.target.value);
        applyPlaybackSpeed(val, false);
      }});
      speedSlider.addEventListener('change', (e) => {{
        const val = parseFloat(e.target.value);
        applyPlaybackSpeed(val, true);
      }});
    }}

    if (btnSpeedMinus) {{
      btnSpeedMinus.addEventListener('click', () => {{
        stepSpeedPreset(-1);
      }});
    }}

    if (btnSpeedPlus) {{
      btnSpeedPlus.addEventListener('click', () => {{
        stepSpeedPreset(1);
      }});
    }}

    if (btnResetSpeed) {{
      btnResetSpeed.addEventListener('click', () => {{
        applyPlaybackSpeed(1.0, true);
        closeSpeedMenu();
      }});
    }}
    btnMobileDrawer.addEventListener('click', openDrawer);
    btnCloseSidebar.addEventListener('click', closeDrawer);
    drawerBackdrop.addEventListener('click', closeDrawer);

    // Fullscreen imersivo nativo com auto-rotação para paisagem (landscape) no mobile
    async function toggleFullscreen() {{
      const isFs = visualBox.classList.contains('is-fullscreen') || 
                   !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement);

      if (!isFs) {{
        visualBox.classList.add('is-fullscreen');

        // 1. Solicita tela cheia nativa para ocultar completamente a barra de endereço e controles do navegador
        try {{
          const req = visualBox.requestFullscreen || visualBox.webkitRequestFullscreen || visualBox.mozRequestFullScreen || visualBox.msRequestFullscreen || document.documentElement.requestFullscreen;
          if (req) {{
            const p = req.call(visualBox, {{ navigationUI: 'hide' }});
            if (p && p.then) await p.catch(() => {{}});
          }}
        }} catch (err) {{
          console.warn('Erro ao solicitar tela cheia nativa:', err);
        }}

        // 2. Gira e trava a tela automaticamente no modo paisagem (landscape) no mobile
        try {{
          if (screen.orientation && typeof screen.orientation.lock === 'function') {{
            await screen.orientation.lock('landscape').catch(() => {{}});
          }} else if (screen.lockOrientation) {{
            screen.lockOrientation('landscape');
          }} else if (screen.mozLockOrientation) {{
            screen.mozLockOrientation('landscape');
          }} else if (screen.msLockOrientation) {{
            screen.msLockOrientation('landscape');
          }}
        }} catch (err) {{
          console.warn('Orientação paisagem não suportada ou bloqueada pelo dispositivo:', err);
        }}
      }} else {{
        visualBox.classList.remove('is-fullscreen');

        // 1. Destrava a orientação para retornar ao modo padrão do dispositivo
        try {{
          if (screen.orientation && typeof screen.orientation.unlock === 'function') {{
            screen.orientation.unlock();
          }} else if (screen.unlockOrientation) {{
            screen.unlockOrientation();
          }} else if (screen.mozUnlockOrientation) {{
            screen.mozUnlockOrientation();
          }} else if (screen.msUnlockOrientation) {{
            screen.msUnlockOrientation();
          }}
        }} catch (err) {{}}

        // 2. Sai do modo de tela cheia nativo do navegador
        try {{
          if (document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement) {{
            const exit = document.exitFullscreen || document.webkitExitFullscreen || document.mozCancelFullScreen || document.msExitFullscreen;
            if (exit) {{
              const p = exit.call(document);
              if (p && p.then) await p.catch(() => {{}});
            }}
          }}
        }} catch (err) {{}}
      }}
    }}

    function handleFullscreenExit() {{
      const isFsNative = !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement);
      if (!isFsNative) {{
        visualBox.classList.remove('is-fullscreen');
        try {{
          if (screen.orientation && typeof screen.orientation.unlock === 'function') {{
            screen.orientation.unlock();
          }} else if (screen.unlockOrientation) {{
            screen.unlockOrientation();
          }}
        }} catch (e) {{}}
      }} else {{
        visualBox.classList.add('is-fullscreen');
      }}
    }}

    ['fullscreenchange', 'webkitfullscreenchange', 'mozfullscreenchange', 'MSFullscreenChange'].forEach(evt => {{
      document.addEventListener(evt, handleFullscreenExit);
    }});

    if (btnFullscreen) btnFullscreen.addEventListener('click', toggleFullscreen);
    btnFsToggle.addEventListener('click', toggleFullscreen);
    if (btnFsExit) btnFsExit.addEventListener('click', toggleFullscreen);
    if (btnMobFs) btnMobFs.addEventListener('click', toggleFullscreen);
    visualBox.addEventListener('dblclick', toggleFullscreen);

    if (btnFsPrev) btnFsPrev.addEventListener('click', () => prevSlide(true));
    if (btnFsNext) btnFsNext.addEventListener('click', () => nextSlide(true));
    if (btnFsPlay) btnFsPlay.addEventListener('click', togglePlay);

    // Navegação por gestos de deslize (swipe) e toque na tela para Pausar / Reproduzir em tela cheia
    let touchStartX = 0;
    let touchStartY = 0;
    let touchStartTime = 0;
    let isSwiping = false;
    let lastTouchTapTime = 0;

    visualBox.addEventListener('touchstart', (e) => {{
      if (e.touches.length === 1) {{
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        touchStartTime = Date.now();
        isSwiping = false;
      }}
    }}, {{ passive: true }});

    visualBox.addEventListener('touchmove', (e) => {{
      if (e.touches.length === 1) {{
        const diffX = Math.abs(e.touches[0].clientX - touchStartX);
        const diffY = Math.abs(e.touches[0].clientY - touchStartY);
        if (diffX > 15 || diffY > 15) {{
          isSwiping = true;
        }}
      }}
    }}, {{ passive: true }});

    visualBox.addEventListener('touchend', (e) => {{
      // Ignorar toques sobre botões de controle e menus interativos
      if (e.target.closest('#btnFsExit') || e.target.closest('#btnFsSpeed') || e.target.closest('#btnFsToggle') || e.target.closest('#speedMenu')) {{
        return;
      }}

      if (e.changedTouches.length === 1) {{
        const diffX = e.changedTouches[0].clientX - touchStartX;
        const diffY = e.changedTouches[0].clientY - touchStartY;
        const touchDuration = Date.now() - touchStartTime;

        // Se foi um deslize horizontal (> 40px), avança ou volta o slide
        if (Math.abs(diffX) > 40 && Math.abs(diffX) > Math.abs(diffY)) {{
          if (diffX < 0) {{
            nextSlide(true);
          }} else {{
            prevSlide(true);
          }}
          return;
        }}

        // Se foi um toque simples na tela (tap) sem arrasto E em Tela Cheia:
        const isFs = visualBox.classList.contains('is-fullscreen') || document.fullscreenElement || document.webkitFullscreenElement;
        if (isFs && !isSwiping && touchDuration < 380 && Math.abs(diffX) < 15 && Math.abs(diffY) < 15) {{
          lastTouchTapTime = Date.now();
          const willPlay = audioPlayer.paused;
          togglePlay();
          showPlayPauseFeedback(willPlay);
        }}
      }}
    }}, {{ passive: true }});

    // Clique com mouse / trackpad no desktop em tela cheia para Pausar / Reproduzir
    visualBox.addEventListener('click', (e) => {{
      if (e.target.closest('#btnFsExit') || e.target.closest('#btnFsSpeed') || e.target.closest('#btnFsToggle') || e.target.closest('#speedMenu')) {{
        return;
      }}
      // Evita duplo disparo provocado por emulação de clique após touch
      if (Date.now() - lastTouchTapTime < 500) {{
        return;
      }}

      const isFs = visualBox.classList.contains('is-fullscreen') || document.fullscreenElement || document.webkitFullscreenElement;
      if (isFs) {{
        const willPlay = audioPlayer.paused;
        togglePlay();
        showPlayPauseFeedback(willPlay);
      }}
    }});

    // Atalhos de Teclado Avançados
    window.addEventListener('keydown', (e) => {{
      // Ignorar se estiver interagindo com controles de formulário exceto teclas de atalho do player
      if (e.target.tagName === 'INPUT' && e.target.type !== 'range') return;
      if (e.target.tagName === 'TEXTAREA') return;

      if (e.code === 'Space') {{
        e.preventDefault();
        const willPlay = audioPlayer.paused;
        togglePlay();
        const isFs = visualBox.classList.contains('is-fullscreen') || document.fullscreenElement || document.webkitFullscreenElement;
        if (isFs) {{
          showPlayPauseFeedback(willPlay);
        }}
      }} else if (e.code === 'ArrowRight') {{
        e.preventDefault();
        nextSlide(true);
      }} else if (e.code === 'ArrowLeft') {{
        e.preventDefault();
        prevSlide(true);
      }} else if (e.code === 'KeyF') {{
        e.preventDefault();
        toggleFullscreen();
      }} else if (e.code === 'Escape' || e.key === 'Escape') {{
        if (speedMenu && speedMenu.classList.contains('open')) {{
          e.preventDefault();
          closeSpeedMenu();
          return;
        }}
        if (visualBox.classList.contains('is-fullscreen') || document.fullscreenElement) {{
          e.preventDefault();
          toggleFullscreen();
        }}
      }} else if (e.key === '>' || (e.shiftKey && (e.key === '.' || e.code === 'Period'))) {{
        e.preventDefault();
        stepSpeedPreset(1);
      }} else if (e.key === '<' || (e.shiftKey && (e.key === ',' || e.code === 'Comma'))) {{
        e.preventDefault();
        stepSpeedPreset(-1);
      }} else if (e.key === ']' || e.code === 'BracketRight') {{
        e.preventDefault();
        stepSpeedPreset(1);
      }} else if (e.key === '[' || e.code === 'BracketLeft') {{
        e.preventDefault();
        stepSpeedPreset(-1);
      }} else if (e.code === 'KeyS' && !e.ctrlKey && !e.metaKey) {{
        e.preventDefault();
        toggleSpeedMenu(btnSpeed);
      }} else if (e.code === 'KeyR' && !e.ctrlKey && !e.metaKey) {{
        e.preventDefault();
        applyPlaybackSpeed(1.0, true);
      }}
    }});

    // Inicialização com estado pausado e velocidade garantida
    visualBox.classList.add('is-paused');
    applyPlaybackSpeed(currentSpeed, false);
    loadSlide(0, false);
  </script>
</body>
</html>
'''

    with open('Player_Apresentacao_Tiago_2026.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print('Player_Apresentacao_Tiago_2026.html e index.html gerados com sucesso com velocidade TSM avançada!')

if __name__ == '__main__':
    generate_player_html()
