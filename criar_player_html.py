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

    /* FULLSCREEN NATIVO */
    .visual-box:fullscreen,
    .visual-box:-webkit-full-screen {{
      width: 100vw;
      height: 100vh;
      border: none;
      border-radius: 0;
      background: #000;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .visual-box:fullscreen img,
    .visual-box:-webkit-full-screen img {{
      width: 100vw;
      height: 100vh;
      object-fit: contain;
    }}
    .fs-hud {{
      display: none;
      position: absolute;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(18, 19, 22, 0.92);
      border: 1px solid rgba(48, 131, 255, 0.3);
      padding: 8px 20px;
      border-radius: var(--radius-pill);
      backdrop-filter: blur(12px);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
      align-items: center;
      gap: 14px;
      z-index: 50;
    }}
    .visual-box:fullscreen .fs-hud,
    .visual-box:-webkit-full-screen .fs-hud {{
      display: flex;
    }}
    .fs-hud-title {{
      font-size: 0.85rem;
      font-weight: 600;
      color: #93c5fd;
      max-width: 260px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .fs-hud button {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: #fff;
      padding: 6px 12px;
      font-size: 0.82rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
    }}
    .fs-hud button:hover {{
      background: var(--primary);
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
    button.btn-ctrl.primary {{
      background: var(--primary);
      border-color: var(--primary);
    }}
    button.btn-ctrl.primary:hover {{
      background: var(--primary-hover);
    }}
    button.btn-speed {{
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: #93c5fd;
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
    }}
    button.btn-speed:hover {{
      background: var(--primary-light);
      border-color: var(--primary);
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
          <img id="slideImg" src="" alt="Slide da Apresentação" title="Clique duas vezes para Tela Cheia">
          
          <!-- HUD EM TELA CHEIA -->
          <div id="fsHud" class="fs-hud">
            <button id="btnFsPrev" title="Anterior">⏮️</button>
            <button id="btnFsPlay" title="Reproduzir / Pausar">▶️</button>
            <button id="btnFsNext" title="Próximo">⏭️</button>
            <span id="fsHudTitle" class="fs-hud-title">Slide 1 / 84</span>
            <button id="btnFsExit" title="Sair">✕ Sair</button>
          </div>
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
              <button id="btnMobSpeed" class="btn-speed" title="Velocidade da fala">1.0x</button>
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

        <!-- QUADRO DO ROTEIRO DO TIAGO (ROLAGEM INDEPENDENTE) -->
        <div class="script-box">
          <div class="script-header">
            <div class="script-header-badge">
              <span>🎙️ ROTEIRO DO TIAGO (1ª PESSOA • FALA DINÂMICA)</span>
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
    <a id="btnMobWhatsApp" href="https://wa.me/?text=Ol%C3%A1!%20Assisti%20a%20apresenta%C3%A7%C3%A3o%20de%20vendas%20do%20BotConversa%20com%20o%20Tiago%20e%20gostaria%20de%20conversar%20sobre%20a%20minha%20decis%C3%A3o." target="_blank" class="whatsapp-cta-btn">
      <svg fill="currentColor" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"></path></svg>
      <span>Responder no WhatsApp com Decisão</span>
    </a>
  </div>

  <!-- FOOTER (DESKTOP) -->
  <footer>
    <div class="controls">
      <button id="btnPrev" class="btn-ctrl">⏮️ Anterior</button>
      <button id="btnPlay" class="btn-ctrl primary">▶️ Reproduzir Áudio</button>
      <button id="btnNext" class="btn-ctrl">⏭️ Próximo</button>
      <button id="btnSpeed" class="btn-speed" title="Alternar velocidade de fala">1.0x</button>
      <button id="btnFullscreen" class="btn-ctrl" title="Expandir em Tela Cheia (F)">⛶ Tela Cheia</button>
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

      <a id="btnDeskWhatsApp" href="https://wa.me/?text=Ol%C3%A1!%20Assisti%20a%20apresenta%C3%A7%C3%A3o%20de%20vendas%20do%20BotConversa%20com%20o%20Tiago%20e%20gostaria%20de%20conversar%20sobre%20a%20minha%20decis%C3%A3o." target="_blank" class="whatsapp-cta-btn">
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
    const speeds = [1.0, 1.25, 1.5, 2.0];

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
      fsHudTitle.textContent = slideTitleStr;
      mobileSlideCount.textContent = `Slide ${{s.slide_number}}/84`;
      slideIndicatorHeader.textContent = `${{s.slide_number}} / 84`;

      audioPlayer.src = `audios_tiago_2026/Slide_${{padAudio}}.mp3?v=2`;
      audioPlayer.playbackRate = currentSpeed;

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
      btnFsPlay.textContent = isPlaying ? '⏸️' : '▶️';
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

    function cycleSpeed() {{
      const currentSpeedIdx = speeds.indexOf(currentSpeed);
      const nextIdx = (currentSpeedIdx + 1) % speeds.length;
      currentSpeed = speeds[nextIdx];
      audioPlayer.playbackRate = currentSpeed;
      const speedStr = `${{currentSpeed.toFixed(currentSpeed === 1.0 ? 1 : 2)}}x`;
      btnSpeed.textContent = speedStr;
      btnMobSpeed.textContent = speedStr;
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
      timeDuration.textContent = formatTime(audioPlayer.duration);
      if (mobTimeDuration) mobTimeDuration.textContent = formatTime(audioPlayer.duration);
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
    btnSpeed.addEventListener('click', cycleSpeed);

    // Eventos Mobile
    btnMobPlay.addEventListener('click', togglePlay);
    btnMobPrev.addEventListener('click', () => prevSlide(true));
    btnMobNext.addEventListener('click', () => nextSlide(true));
    btnMobSpeed.addEventListener('click', cycleSpeed);
    btnMobileDrawer.addEventListener('click', openDrawer);
    btnCloseSidebar.addEventListener('click', closeDrawer);
    drawerBackdrop.addEventListener('click', closeDrawer);

    // Fullscreen Handlers
    function toggleFullscreen() {{
      if (!document.fullscreenElement && !document.webkitFullscreenElement) {{
        if (visualBox.requestFullscreen) {{
          visualBox.requestFullscreen();
        }} else if (visualBox.webkitRequestFullscreen) {{
          visualBox.webkitRequestFullscreen();
        }}
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }} else if (document.webkitExitFullscreen) {{
          document.webkitExitFullscreen();
        }}
      }}
    }}

    btnFullscreen.addEventListener('click', toggleFullscreen);
    btnFsToggle.addEventListener('click', toggleFullscreen);
    btnFsExit.addEventListener('click', toggleFullscreen);
    if (btnMobFs) btnMobFs.addEventListener('click', toggleFullscreen);
    visualBox.addEventListener('dblclick', toggleFullscreen);

    btnFsPrev.addEventListener('click', () => prevSlide(true));
    btnFsNext.addEventListener('click', () => nextSlide(true));
    btnFsPlay.addEventListener('click', togglePlay);

    // Atalhos de Teclado
    window.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.code === 'Space') {{
        e.preventDefault();
        togglePlay();
      }} else if (e.code === 'ArrowRight') {{
        e.preventDefault();
        nextSlide(true);
      }} else if (e.code === 'ArrowLeft') {{
        e.preventDefault();
        prevSlide(true);
      }} else if (e.code === 'KeyF') {{
        e.preventDefault();
        toggleFullscreen();
      }}
    }});

    // Inicialização
    loadSlide(0, false);
  </script>
</body>
</html>
'''

    with open('Player_Apresentacao_Tiago_2026.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print('Player_Apresentacao_Tiago_2026.html gerado com sucesso com visual BotConversa oficial e suporte Mobile!')

if __name__ == '__main__':
    generate_player_html()
