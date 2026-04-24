# English Agent

Um agente conversacional com IA que ajuda pessoas a praticar e melhorar o inglês por meio de interação de voz em tempo real.

Atualmente, este projeto usa Azure VoiceLive para áudio e conversação em tempo real.

## Visão Geral

O English Agent combina modelos de linguagem de grande porte (LLMs) com bibliotecas de text-to-speech (TTS) e speech-to-text (STT) para criar um assistente de prática de inglês em tempo real. Os usuários podem falar ou digitar em inglês, e o agente responde de forma natural, corrige erros e ajuda a desenvolver melhores habilidades de comunicação.

## Funcionalidades

- **Interação de voz em tempo real** - Fale com o agente e receba respostas faladas usando pipelines de TTS/STT
- **Correção ortográfica** - Detecta e corrige automaticamente palavras digitadas incorretamente na entrada do usuário
- **Correção gramatical e de frases** - Reescreve frases mal estruturadas em inglês natural e fluente
- **Perguntas e respostas gerais** - Pergunte qualquer coisa ao agente; ele responde usando um backend com LLM
- **Feedback conversacional** - Explica as correções para que o usuário aprenda com os próprios erros

## Como Funciona

```
Usuário fala / digita
        ↓
 Speech-to-Text (STT)
        ↓
  LLM processa a entrada
  - Responde a pergunta
  - Corrige erros de ortografia
  - Corrige gramática
        ↓
  Text-to-Speech (TTS)
        ↓
   Agente responde em voz alta
```

1. A voz do usuário é capturada e transcrita por meio de uma biblioteca de STT.
2. O texto transcrito é enviado para um LLM com um prompt que o instrui a responder à pergunta do usuário, corrigir erros de ortografia e gramática e fornecer a versão corrigida quando relevante.
3. A resposta do LLM é convertida novamente em fala e reproduzida para o usuário em tempo real.

## Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Modelo de Linguagem | Modelo Azure VoiceLive (padrão: `gpt-realtime`) |
| Speech-to-Text | Pipeline de áudio de entrada do Azure VoiceLive |
| Text-to-Speech | Pipeline de áudio de saída do Azure VoiceLive |
| Backend | Python + asyncio |
| Empacotamento/Instalador | `uv` |

## Casos de Uso

- Falantes não nativos de inglês que querem praticar inglês conversacional
- Estudantes que desejam feedback imediato sobre pronúncia e gramática
- Qualquer pessoa em busca de um tutor de IA interativo disponível a qualquer momento

## Como Começar

### 1) Pré-requisitos

- Python 3.11+
- `uv` instalado: https://docs.astral.sh/uv/getting-started/installation/
- Azure CLI instalado e autenticado (`az login`)
- Endpoint Azure VoiceLive válido e agente Foundry

### 2) Configurar credenciais

Atualize o `.env` com suas credenciais:

```env
AZURE_VOICELIVE_ENDPOINT="https://<your-resource>.services.ai.azure.com/"
AZURE_VOICELIVE_PROJECT_NAME="<your-foundry-project-name>"
AZURE_VOICELIVE_AGENT_ID="<your-agent-name-or-name:version>"
AZURE_VOICELIVE_AGENT_VERSION=""
AZURE_VOICELIVE_VOICE="en-US-Ava:DragonHDLatestNeural"
AZURE_VOICELIVE_MUTE_MIC_WHILE_SPEAKING="true"
AZURE_VOICELIVE_ENABLE_INTERIM_RESPONSES="false"
AZURE_VOICELIVE_AUTO_LANGUAGE_VOICE="true"
AZURE_VOICELIVE_VOICE_EN="en-US-Ava:DragonHDLatestNeural"
AZURE_VOICELIVE_VOICE_PT="pt-BR-FranciscaNeural"
```

Você pode copiar essa informação diretamente do Foundry Portal.

Se o seu agente for versionado, defina `AZURE_VOICELIVE_AGENT_ID` como `name:version` ou configure `AZURE_VOICELIVE_AGENT_VERSION` separadamente.

Defina `AZURE_VOICELIVE_ENABLE_INTERIM_RESPONSES` como `false` para evitar que o agente fale respostas parciais e finais (o que pode soar como respostas duplicadas).

Defina `AZURE_VOICELIVE_AUTO_LANGUAGE_VOICE` como `true` para alternar automaticamente a voz com base no idioma detectado do usuário e melhorar a naturalidade do sotaque. A alternância automática é restrita a inglês (`en`) e português (`pt`).

Defina `AZURE_VOICELIVE_MUTE_MIC_WHILE_SPEAKING` como `true` para impedir que o agente ouça a própria voz enquanto responde.

### 3) Executar

```powershell
uv run english-agent
```

### 4) Flags opcionais de execução

```powershell
uv run english-agent --verbose
uv run english-agent --voice "en-US-GuyNeural"
uv run english-agent --model "gpt-realtime"
```

Os logs são gravados na pasta `logs/`.

## Contribuição

Contribuições são bem-vindas. Abra uma issue ou envie um pull request com as alterações propostas.

## Licença

MIT
