import json
import re
import sys

# Script para carregar o roteiro original da Apresentação de Vendas 2026 e
# converter a perspectiva de 3ª pessoa ("o fundador", "o Thiago", "ele começou")
# para a 1ª pessoa ("eu criei", "eu comecei", "eu descobri"), além de limpar
# marcações de palco e instruções do PowerPoint.

def main():
    with open('slides_script_raw.json', 'r', encoding='utf-8') as f:
        raw_slides = json.load(f)

    print(f"Processando {len(raw_slides)} slides...")

    def clean_and_transform(notes: str, num: int) -> str:
        text = notes

        # Remover comandos de palco / clique do orador / setas unicode
        text = re.sub(r'\(Clique[^\)]*\)', '', text, flags=re.I)
        text = re.sub(r'\(CLIQUE[^\)]*\)', '', text, flags=re.I)
        text = re.sub(r'\(FINALIZANDO[^\)]*\)', '', text, flags=re.I)
        text = re.sub(r'[—\-–\u2014\u2013\u2192>]+\s*PR[ÓO]XIMO\s*SLIDE', '', text, flags=re.I)
        text = re.sub(r'[—\-–\u2014\u2013\u2192>]+\s*PULE\s+PARA[^\n]*', '', text, flags=re.I)
        text = re.sub(r'[—\-–\u2014\u2013]+\s*\(Script ap[oó]s retornar[^\)]*\)\s*[—\-–\u2014\u2013]+', '', text, flags=re.I)
        text = re.sub(r'[—\-–\u2014\u2013]+\s*\(Voltar ao slide[^\)]*\)\s*[—\-–\u2014\u2013]+', '', text, flags=re.I)

        # Tratar placeholders de parceiros
        text = re.sub(r'\[Nome cliente\]', 'você', text, flags=re.I)
        text = re.sub(r'\[NOME CLIENTE\]', 'você', text, flags=re.I)
        text = re.sub(r'\[Nicho\]', 'seu nicho', text, flags=re.I)
        text = re.sub(r'\[NICHO CLIENTE\]', 'seu nicho', text, flags=re.I)
        text = re.sub(r'no seu negócio de seu nicho', 'no seu negócio', text, flags=re.I)
        text = re.sub(r'no seu negócio de \[Nicho\]', 'no seu negócio', text, flags=re.I)

        # Ajustes pontuais nos slides para a voz do Tiago em 1ª pessoa
        if num == 5:
            text = text.replace('quando nosso fundador criou', 'quando eu criei')
            text = text.replace('em que ele descobriu esse negócio de atendimento automático.', 'em que eu descobri esse negócio de atendimento automático.')
            text = text.replace('Foi nesse negócio online que ele descobriu', 'Foi nesse negócio online que eu descobri')
            text = text.replace(
                'Ele começou a trabalhar com isso e a vender os serviços para os negócios da cidade dele. Ele é de Nova Friburgo, na região Serrana do Rio de Janeiro. Começou vendendo primeiro para uma imobiliária, depois vendeu para um curso, e depois ele vendeu para clientes fora do Brasil',
                'Eu comecei a trabalhar com isso e a vender os serviços para os negócios da minha cidade. Eu sou de Nova Friburgo, na região Serrana do Rio de Janeiro. Comecei vendendo primeiro para uma imobiliária, depois vendi para um curso, e depois vendi para clientes fora do Brasil'
            )
            text = text.replace('Até que...\n\nAté que eu cheguei', 'Até que eu cheguei')
            text = text.replace('Ele chegou em um momento em que falou:', 'Até que eu cheguei em um momento em que pensei:')
            text = text.replace(
                'E então ele fez uma das coisas mais doidas: conheceu um programador em um site de freelancer americano, fez uma reunião com esse programador e falou para ele — que é esse cara mais alto da esquerda, o nome dele é Illya Borodin, ele é nosso co-fundador e nosso CTO da empresa — e disse:',
                'E então eu fiz uma das coisas mais doidas: conheci um programador em um site de freelancer americano, fiz uma reunião com ele — que é esse cara mais alto da esquerda, o nome dele é Illya Borodin, ele é meu co-fundador e o CTO da nossa empresa — e falei pra ele:'
            )
            text = text.replace(
                'O Illya aceitou. O Thiago, que é o nosso CEO, foi para a Bielorrússia e ficou lá 1 mês. O Illya chamou alguns amigos da faculdade dele e o nosso negócio iniciou em 2020. O Thiago foi para a Bielorrússia em 2020.',
                'O Illya aceitou. Eu fui para a Bielorrússia e fiquei lá 1 mês. O Illya chamou alguns amigos da faculdade dele e o nosso negócio começou em 2020. Eu fui para a Bielorrússia em 2020.'
            )
        elif num == 6:
            text = text.replace('ele começou a vida dele neste negócio Fitness', 'eu comecei a minha vida neste negócio Fitness')
        elif num == 7:
            text = text.replace('ele descobriu como que fazia a geração de lead com comentários', 'eu descobri como fazia a geração de leads com comentários')
            text = text.replace(
                'O que ele fazia? Lá no Facebook, ele criava as postagens da plataforma fitness dele:',
                'O que eu fazia? Lá no Facebook, eu criava as postagens da minha plataforma fitness:'
            )
            text = text.replace(
                'E ele descobriu que esse formato para gerar lead era incrível. Ele começou a usar isso demais.',
                'E eu descobri que esse formato para gerar lead era incrível. Comecei a usar isso demais.'
            )
        elif num == 8:
            text = text.replace('Depois ele aprimorou isso, começou a utilizar isso para fluxo de vendas.', 'Depois eu aprimorei isso, comecei a utilizar para fluxos de vendas.')
            text = text.replace('O Thiago começou a utilizar este funil.', 'Eu comecei a utilizar este funil.')
        elif num == 14:
            text = text.replace('aqui, você, você vai ter um atalho', 'aqui, você vai ter um atalho')
            text = text.replace('aqui, você,', 'aqui,')
        elif num == 20:
            text = text.replace('E você, você', 'E você?')
            text = text.replace(
                'fez no WhatsApp dele, tá atendendo todo mundo que manda mensagem no seu nicho dele',
                'fez no WhatsApp da empresa, tá atendendo todo mundo que manda mensagem no negócio'
            )
        elif num == 22:
            text = text.replace('Quando o Thiago mostrou essa conta no palco do Adaptar Summit', 'Quando eu mostrei essa conta no palco do Adaptar Summit')
            text = text.replace(
                'Então, o BotConversa foi patrocinador master do evento. O Thiago palestrou nesse evento.',
                'O BotConversa foi o patrocinador master do evento, e eu palestrei nesse evento.'
            )
        elif num == 24:
            text = text.replace('O chatbot, você, ele resolveu', 'O chatbot, ele resolveu')
        elif num == 26:
            text = text.replace('o Thiago mandou um “olá” e recebeu uma mensagem dizendo:', 'eu mandei um “olá” e recebi uma mensagem dizendo:')
            text = text.replace('o Thiago mandou um "olá" e recebeu uma mensagem dizendo:', 'eu mandei um "olá" e recebi uma mensagem dizendo:')
            text = text.replace('O Thiago digitou “É Thiago”.', 'Eu digitei “É Thiago”.')
            text = text.replace('O Thiago digitou "É Thiago".', 'Eu digitei "É Thiago".')
            text = text.replace(
                'O nome da pessoa não é “É Thiago”. Ele digitou “É Thiago”, mas o nome dele é só Thiago.',
                'O meu nome não é “É Thiago”. Eu digitei “É Thiago”, mas o meu nome é só Thiago.'
            )
            text = text.replace(
                'O nome da pessoa não é "É Thiago". Ele digitou "É Thiago", mas o nome dele é só Thiago.',
                'O meu nome não é "É Thiago". Eu digitei "É Thiago", mas o meu nome é só Thiago.'
            )
            text = text.replace('E aqui no segundo exemplo, ele digitou o “É Thiago”', 'E aqui no segundo exemplo, eu digitei “É Thiago”')
            text = text.replace('E aqui no segundo exemplo, ele digitou o "É Thiago"', 'E aqui no segundo exemplo, eu digitei "É Thiago"')
        elif num == 41:
            text = "Eu tenho um depoimento aqui de um cliente nosso, o Cláudio da Adapta, que comprova exatamente o poder dessa transformação no WhatsApp."
        elif num == 44:
            text = text.replace('por exemplo, você. Imagina', 'por exemplo. Imagina')
        elif num == 51:
            text = text.replace('que era o que o Thiago fazia lá em 2018.', 'que era o que eu fazia lá em 2018.')
        elif num == 55:
            # Manter introdução limpa
            text = "Existem 7 partes para um assistente de inteligência artificial.\n\nSe você entender isso aqui, você consegue criar um assistente para qualquer coisa, e eu vou passar parte por parte agora para que você entenda exatamente o que é esperado de cada uma."
        elif num == 69:
            # Adicionar a conclusão das 7 partes aqui
            conclusao = "\n\nEntão, essas aqui são as 7 partes de um assistente de IA. Se você entende cada uma dessas partes, você consegue criar o assistente que você quiser para fazer o que você quiser no seu negócio: o qualificador, o resolutivo para tirar dúvidas, o transacional e o especialista."
            text = text + conclusao
        elif num == 76:
            text = text.replace('aqui, você.\n', 'aqui.\n')
            text = text.replace('aqui, você.', 'aqui.')
        elif num == 83:
            text = text.replace('aqui, você, eu tenho certeza', 'aqui, eu tenho certeza')

        # Normalizar espaçamentos e parágrafos
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        cleaned = '\n\n'.join(lines)
        return cleaned

    processed = []
    for s in raw_slides:
        num = s['slide_number']
        c = clean_and_transform(s['notes'], num)
        processed.append({
            'slide_number': num,
            'title': s['title'],
            'slide_text': s['slide_text'],
            'script_tiago': c
        })

    with open('slides_roteiro_tiago_2026.json', 'w', encoding='utf-8') as f:
        json.dump(processed, f, ensure_ascii=False, indent=2)

    print(f"Sucesso! {len(processed)} slides salvos em slides_roteiro_tiago_2026.json.")

if __name__ == '__main__':
    main()
