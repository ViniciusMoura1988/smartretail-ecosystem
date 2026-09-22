# 🛒 Ecossistema de Automação Comercial (SmartRetail Ecosystem)
### Otimização de Processos, Prevenção de Perdas e Eficiência Operacional
*Estudo de Caso Aplicado: Atacadão Dia a Dia (Unidade Sobradinho - DF)*

Este repositório reúne soluções lógicas, documentação de processos e simulações em código desenvolvidas para sanar gargalos operacionais e prejuízos invisíveis em atacarejos de alta volumetria.

---

## 📄 Proposta Executiva em PDF (Sumário de Alto Impacto)
Para apresentar este ecossistema a gerentes de loja, diretores regionais ou equipes de compras de forma rápida e visual, faça o download da nossa proposta executiva estruturada em modelo de negócios:
👉 **[Baixar Proposta Comercial em PDF](Ecossistema_SmartRetail_Vinicius_Moura.pdf)**
*(Nota: O arquivo PDF funciona como um sumário de alto impacto para tomada de decisão e possui links ativos que redirecionam o leitor técnico de volta para as linhas de código deste repositório).*

---

## 💡 Conheça as 5 Grandes Ideias do Ecossistema (Leitura em Camadas)
*Se você for da gerência ou da equipe de TI, clique nas setas abaixo para expandir e ver o detalhamento técnico e operacional de cada solução:*

<details>
<summary><b>🚨 1. SmartCheckout (Frente de Caixa Sem Travamento e Alerta Periférico)</b></summary>
<br>

*   **O Problema:** Leitores ópticos capturam QR Codes promocionais de embalagens por engano. O software antigo tenta processar o link como produto, gerando a "tela branca" de erro genérica que interrompe o foco do operador e gera filas.
*   **A Solução de TI:** Um filtro lógico via Expressões Regulares (Regex) que intercepta a URL em milissegundos antes de enviar o dado inválido ao banco central.

<details>
<summary>🟢 CLIQUE PARA VER: Proposta de Curto Prazo (Imediato - Custo R$ 0,00)</summary>
<blockquote>
Modificação na interface do PDV atual. Em vez de travar o sistema, o fundo da tela muda instantaneamente para PRETO ou VERMELHO (ajudando a visão periférica do operador), emite bipes graves diferentes do padrão e avisa o nome do produto que deu erro para você repassar.
<br><br>
🔗 <b>Ver código em Python:</b> <a href="caixa_inteligente.py#L25">Lógica de Tratamento do Bip e Alerta Visual</a>
</blockquote>
</details>

<details>
<summary>🟡 CLIQUE PARA VER: Proposta de Médio Prazo</summary>
<blockquote>
Criação de uma tabela de cache local (`de_para_qrcodes`). Se o link já tiver sido bipado por qualquer caixa da loja, o sistema deduz o nome do item na hora sem precisar de conexão externa com a internet, operando em menos de 50ms.
<br><br>
🔗 <b>Ver banco de dados:</b> <a href="banco_dados.sql#L12">Estrutura de Cache Local para URLs</a>
</blockquote>
</details>

<details>
<summary>🔵 CLIQUE PARA VER: Proposta de Longo Prazo (Automação Avançada)</summary>
<blockquote>
Integração de uma API assíncrona que faz uma busca e raspagem relâmpago do link na internet para trazer o nome do produto em tempo real na tela do caixa se ele não estiver no cache da loja.
<br><br>
🔗 <b>Ver script Python:</b> <a href="caixa_inteligente.py#L38">Integração Sênior com Expressões Regulares</a>
</blockquote>
</details>

</details>

---

<details>
<summary><b>📋 2. Menu Flip (Controle Unificado de FLV e Açougue)</b></summary>
<br>

*   **O Problema:** Clientes chegam ao checkout com produtos de pesagem sem etiqueta ou com o código rasgado/molhado. O cliente precisa voltar para o açougue ou FLV para pesar de novo, travando todo o checkout.
*   **A Solução Prática:** Uma placa física impressa fixada em cada caixa com os códigos de barras de todas as carnes e frutas da loja.

<details>
<summary>🟢 CLIQUE PARA VER: Proposta de Curto Prazo (Imediato - Custo R$ 0,00)</summary>
<blockquote>
Modo Manual Tolerante a Falhas. O operador bipa o produto na placa e o sistema abre um campo na tela: "Digite o peso do visor". O operador digita o peso da balança atual isolada, o sistema faz o cálculo multiplicador no SQL e registra a venda sem o cliente sair da fila.
<br><br>
🔗 <b>Ver código em Python:</b> <a href="caixa_inteligente.py#L52">Chaveamento para Entrada Manual de Peso</a>
</blockquote>
</details>

<details>
<summary>🟡 CLIQUE PARA VER: Proposta de Médio Prazo</summary>
<blockquote>
Aquisição de pistolas leitoras portáteis de código de barras (R$ 130 a R$ 180 por caixa). O operador passa a conseguir bipar a placa de controle de qualquer ângulo da cadeira, sem precisar esticar o braço ou sair de sua posição ergonômica.
</blockquote>
</details>

<details>
<summary>🔵 CLIQUE PARA VER: Proposta de Longo Prazo (Automação Avançada)</summary>
<blockquote>
Automação e Integração Total. O software backend é conectado diretamente às balanças físicas dos caixas via portas de comunicação (`pyserial`). Ao bipar o produto na placa, o sistema captura o peso de forma 100% automática, eliminando a digitação e o risco de erro humano.
<br><br>
🔗 <b>Ver queries SQL:</b> <a href="banco_dados.sql#L25">Tabela de Preço por Quilo e Consultas</a>
</blockquote>
</details>

</details>

---

<details>
<summary><b>📷 3. VisualCheckout (Identificação de FLV via Câmera e IA)</b></summary>
<br>

*   **O Problema:** Operadores perdem tempo precioso digitando códigos ou procurando em listas o nome exato de verduras e frutas para não errar a variedade (ex: diferenciar Maçã Gala de Maçã Argentina).
*   **A Solução de TI:** Uso de uma câmera digital comum instalada sobre o prato de pesagem rodando Inteligência Artificial e Visão Computacional (via framework `OpenCV`).

<details>
<summary>🟢 CLIQUE PARA VER: Proposta de Curto Prazo (Imediato - Custo R$ 0,00)</summary>
<blockquote>
Menu Touchscreen Dinâmico no PDV. Em vez de digitar códigos, o operador clica no botão "Frutas" e o sistema exibe fotos grandes das variedades na tela do caixa (Exige apenas atualização no design do software atual).
</blockquote>
</details>

<details>
<summary>🟡 CLIQUE PARA VER: Proposta de Médio Prazo</summary>
<blockquote>
Instalação de webcams HD baratas focadas no prato de pesagem. O sistema passa a coletar e salvar as imagens para treinar o banco de dados de reconhecimento da própria loja de Sobradinho.
</blockquote>
</details>

<details>
<summary>🔵 CLIQUE PARA VER: Proposta de Longo Prazo (Automação Avançada)</summary>
<blockquote>
Ativação da IA em Tempo Real. Ao colocar o produto na balança, a IA identifica a fruta por formato e cor (ex: "Maçã Gala - Confiança 96%"), busca o preço vigente no banco SQL e o operador registra tudo com apenas 1 clique de confirmação.
<br><br>
🔗 <b>Ver lógica de IA:</b> <a href="caixa_inteligente.py#L65">Simulação do Limiar de Confiança da IA</a>
</blockquote>
</details>

</details>

---

<details>
<summary><b>📦 4. SmartValidity (Fim do Vencimento Oculto no Depósito)</b></summary>
<br>

*   **O Problema:** A batida de validade manual gera estresse e erros. Em estoques profundos, paletes novos bloqueiam os paletes velhos no fundo da estrutura. Produtos vencem escondidos no depósito causando grandes quebras financeiras.
*   **A Solução Logística:** Reestruturação do banco de dados para gerenciar o depósito através de coordenadas tridimensionais estritas (Rua, Módulo, Nível e Posição: Frente/Fundo).

<details>
<summary>🟢 CLIQUE PARA VER: Proposta de Curto Prazo (Imediato - Custo R$ 0,00)</summary>
<blockquote>
Uso obrigatório da leitura do código GS1-128 (caixa fechada) no recebimento pelos coletores que a loja já tem. O sistema extrai a data de validade de fábrica nativamente para o SQL e dita as regras para a empilhadeira: Lote novo vai para o FUNDO; lote velho fica na FRENTE. Repositores recebem listas automáticas diárias indicando quais paletes devem abastecer as gôndolas primeiro (Fluxo PEPS/FIFO).
<br><br>
🔗 <b>Ver modelo de dados:</b> <a href="banco_dados.sql#L35">Modelagem Lógica do Estoque por Posição</a>
</blockquote>
</details>

<details>
<summary>🟡 CLIQUE PARA VER: Proposta de Médio Prazo</summary>
<blockquote>
Alertas automáticos de conflito. Se por erro operacional um palete novo bloquear um velho, um gatilho (`TRIGGER`) no banco de dados detecta o erro e avisa o gerente da loja para fazer a inversão física antes do vencimento.
<br><br>
🔗 <b>Ver regras em Python:</b> <a href="caixa_inteligente.py#L80">Ordenação e Relatório de Validades (PEPS)</a>
</blockquote>
</details>

<details>
<summary>🔵 CLIQUE PARA VER: Proposta de Longo Prazo (Automação Avançada)</summary>
<blockquote>
Automação com RFID / IoT. Implementação de etiquetas de radiofrequência nos paletes e portais leitores nas zonas do depósito. O sistema realiza o inventário das datas de vencimento em segundos em background, sem necessidade de bipagem manual.
</blockquote>
</details>

</details>

---

<details>
<summary><b>📲 5. ReverseFlow Mobile (Triagem Rastreável de Abandonos)</b></summary>
<br>

*   **O Problema:** Produtos abandonados acumulam nos caixas. Itens perecíveis gelados estragam ali mesmo e geram perdas. Forçar o operador a registrar isso tira o foco do atendimento e aumenta as filas.
*   **A Solução Prática:** O operador apenas joga os abandonos em uma cesta ao lado (esforço zero). Um funcionário volante passa fazendo a ronda com um coletor de dados portátil ou celular.

<details>
<summary>🟢 CLIQUE PARA VER: Proposta de Curto Prazo (Imediato - Custo R$ 0,00)</summary>
<blockquote>
Aplicativo Móvel de Ronda. O funcionário volante bipa os itens da cesta. Se detectar um item perecível gelado, o aparelho pisca um alerta de prioridade visual: "🚨 ITEM GELADO: Devolver à geladeira imediatamente". Os carrinhos recebem códigos de barras próprios (ex: `CARRINHO-DPH-01`) para organizar a triagem por setor e carrinho no ato do bipe.
<br><br>
🔗 <b>Ver controle móvel:</b> <a href="caixa_inteligente.py#L105">Lógica da Ronda e Alerta de Perecíveis</a>
</blockquote>
</details>

<details>
<summary>🟡 CLIQUE PARA VER: Proposta de Médio Prazo</summary>
<blockquote>
