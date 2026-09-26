# 🛒 Ecossistema de Automação Comercial (SmartRetail Ecosystem)
### Otimização de Processos, Prevenção de Perdas e Eficiência Operacional
*Estudo de Caso Aplicado: Atacadão Dia a Dia (Unidade Sobradinho - DF)*

Este repositório reúne soluções lógicas, documentação de processos e simulações em código desenvolvidas para sanar gargalos operacionais e prejuízos invisíveis em atacarejos de alta volumetria.

---

## 📄 Proposta Executiva em PDF (Sumário de Alto Impacto)
Para apresentar este ecossistema a gerentes de loja, diretores regionais ou equipes de compras de forma rápida e visual, faça o download da nossa proposta executiva estruturada em modelo de negócios:
👉 **[Baixar Proposta Comercial em PDF](Ecossistema_SmartRetail_Vinicius_Moura.pdf)**
*(Nota: O arquivo PDF funciona como um sumário de alto impacto para tomada de decisão e possui direcionamento técnico para TI e gerência).*

---

## 💡 Conheça as 5 Grandes Ideias do Ecossistema (Leitura em Camadas)
*Se você for da gerência ou da equipe de TI, clique nas setas abaixo para expandir e ver o detalhamento técnico e operacional de cada solução:*

<details>
<summary><b>🚨 01 SmartCheckout - Frente de Caixa Sem Travamento</b></summary>
<br>

* **Gargalo Atendido:** Prevenção de Trancamento de Leitura e Filtro Lógico de Scanners
* **PROBLEMA DETECTADO:** Leitores ópticos capturam QR Codes promocionais presentes nas embalagens por engano. Isso gera telas de erro pouco perceptíveis e permite que novas leituras sejam realizadas antes da correção, dificultando a identificação dos produtos envolvidos.
* **SOLUÇÃO PROPOSTA:** Desenvolvimento de um filtro lógico que identifica leituras incompatíveis (padrão URL/link) antes do envio ao PDV. Ao detectar a falha, o sistema bloqueia temporariamente o checkout, exibe um alerta visual de alta visibilidade e emite sinal sonoro dedicado. Leituras realizadas durante o bloqueio são armazenadas temporariamente para conferência do operador até a liberação por tecla configurada.

<details>
<summary>🟢 CURTO PRAZO</summary>
<blockquote>
Configuração do scanner para desabilitar QR Codes não utilizados ou filtro simples de entrada no PDV. Baixo ou nenhum custo.
</blockquote>
</details>

<details>
<summary>🟡 MÉDIO PRAZO</summary>
<blockquote>
Camada de validação no software do checkout, bloqueando entradas incompatíveis e registrando temporariamente os itens capturados.
</blockquote>
</details>

<details>
<summary>🔵 LONGO PRAZO</summary>
<blockquote>
Integração multi-camada entre scanner, aplicação, backend e banco de dados, com alertas visuais, sonoros e liberação controlada.
<br><br>
🔗 <b>Ver código em Python:</b> <a href="caixa_inteligente.py#L25">Lógica de Tratamento do Bip e Alerta Visual</a>
</blockquote>
</details>

<br>

> 📌 **DETALHAMENTO TÉCNICO & ARQUITETURA DO FILTRO LÓGICO**
> Para mitigar paralisações no checkout sem troca de hardware, a solução opera em dois níveis:
> - **Validação Regex:** Intercepta a leitura antes do envio ao PDV. Padrões `http://`, `https://` ou QR Code NFC-e são descartados instantaneamente.
> - **Buffer de Leitura (Queue):** Leituras de EAN válidos em tela travada são salvas em fila temporária e processadas assim que o alerta for limpo.
> - **Métrica de Sucesso:** Fim dos travamentos silenciosos e redução no tempo de atendimento.

</details>

---

<details>
<summary><b>📋 02 Menu Flip - Controle Unificado de FLV e Açougue</b></summary>
<br>

* **Gargalo Atendido:** Controle Unificado para Etiquetas Danificadas e Agilização de Atendimento Operacional / Caixas
* **PROBLEMA DETECTADO:** Clientes chegam ao checkout com sacos de frutas ou bandejas de carne com etiquetas de pesagem rasgadas, molhadas ou ilegíveis. Isso exige o retorno ao setor de origem para identificação ou nova pesagem, paralisando a esteira, gerando gargalos e aumentando o tempo total de atendimento.
* **SOLUÇÃO PROPOSTA:** Fixação de tabelas físicas de consulta unificada diretamente nos caixas, reunindo fotos de identificação visual e códigos de barras legíveis para cortes de carne, frutas, FLV e itens sob pesagem. Quando a etiqueta estiver danificada, o operador identifica o item visualmente e registra o código no caixa instantaneamente, garantindo a continuidade do atendimento.

<details>
<summary>🟢 CURTO PRAZO</summary>
<blockquote>
Criação e impressão das tabelas físicas organizadas por categoria com fotos e códigos de barras para rápido acesso dos operadores.
</blockquote>
</details>

<details>
<summary>🟡 MÉDIO PRAZO</summary>
<blockquote>
Uso de pistolas leitoras portáteis dedicadas para realizar a leitura direta dos códigos presentes nas tabelas do caixa.
</blockquote>
</details>

<details>
<summary>🔵 LONGO PRAZO</summary>
<blockquote>
Integração direta entre balanças e sistema de checkout, permitindo o envio automático do código e peso ao PDV sem digitação manual.
<br><br>
🔗 <b>Ver código em Python:</b> <a href="caixa_inteligente.py#L52">Chaveamento e Comunicação com Balança</a>
</blockquote>
</details>

<br>

> 📌 **PADRÃO OPERACIONAL & ERGONOMIA DE ATENDIMENTO (POP)**
> A implantação do Menu Flip resolve um dos maiores pontos de fricção na frente de caixa sem exigir grandes investimentos iniciais em TI:
> - **Layout Visual Padronizado:** Organização do catálogo físico em abas rígidas de acrílico (Flip) fixadas ao lado do monitor, divididas por cores: Vermelho (Carnes/Açougue), Verde (Hortifruti) e Amarelo (Padaria/Pães Especiais).
> - **Resolução para Leitura Óptica:** Impressão dos códigos EAN-13 em alta definição laminada, permitindo que a pistola do caixa leia diretamente do menu sem necessidade de digitação manual de PLUs longos.
> - **Procedimento Operacional Padrão (POP):** Treinamento de rápida execução para caixas e fiscal de loja, reduzindo a devolução de clientes ao setor e eliminando o atrito no atendimento.
> - **Ganhos Estimados:** Economia média de 2 a 4 minutos por cliente afetado e diminuição drástica de abandono de sacolas de FLV no checkout.

</details>

---

<details>
<summary><b>📷 03 VisualCheckout - Identificação Inteligente de FLV</b></summary>
<br>

* **Gargalo Atendido:** Interface Visual e Visão Computacional para Hortifrúti (Tecnologia PDV)
* **PROBLEMA DETECTADO:** A identificação de frutas, verduras e legumes no checkout depende da localização e digitação manual de códigos PLU. Produtos visualmente semelhantes, como diferentes variedades de maçã, aumentam o tempo de atendimento e a possibilidade de erros.
* **SOLUÇÃO PROPOSTA:** Criar uma interface de identificação de FLV diretamente no checkout, permitindo que o operador encontre rapidamente o produto por categorias visuais. A solução evolui para o uso de visão computacional na balança (exemplo: Produto identificado: Maçã Gala 0,850 kg), onde o sistema sugere o item e o operador apenas confirma.

<details>
<summary>🟢 CURTO PRAZO</summary>
<blockquote>
Organização de um menu simples no touchscreen do checkout, dividido em categorias (Frutas, Verduras e Legumes) para seleção direta.
</blockquote>
</details>

<details>
<summary>🟡 MÉDIO PRAZO</summary>
<blockquote>
Avaliação das câmeras já disponíveis na loja e de sua compatibilidade com o sistema para testes de captura de imagens sem novos investimentos.
</blockquote>
</details>

<details>
<summary>🔵 LONGO PRAZO</summary>
<blockquote>
Utilização de visão computacional combinando identificação visual e peso, apresentando o produto reconhecido para confirmação no PDV.
<br><br>
🔗 <b>Ver lógica de IA:</b> <a href="caixa_inteligente.py#L65">Simulação do Limiar de Confiança da IA</a>
</blockquote>
</details>

<br>

> 📌 **ARQUITETURA DE VISÃO COMPUTACIONAL & INTEGRAÇÃO COM BALANÇA**
> A evolução do registro de hortifrúti visa zerar as trocas inadvertidas de itens caros por itens baratos (ex: Maçã Argentina por Maçã Gala):
> - **Câmeras Zenitais (Overhead):** Câmeras compactas instaladas acima da bandeja da balança capturam a imagem do item no momento em que ele é colocado sobre o prato de pesagem.
> - **Modelo de Classificação Local (Edge AI):** Um modelo leve de redes neurais (Convolutional Neural Network) processa a imagem localmente no PDV em menos de 200ms, apresentando os 3 produtos mais prováveis no topo da tela Touchscreen.
> - **Confirmação de 1 Clique:** O operador não precisa memorizar ou digitar códigos PLU de 4 dígitos — apenas toca na foto do produto sugerido para concluir a pesagem.
> - **Métricas de Impacto:** Redução do erro humano de registro em até 95% e acréscimo de precisão na margem de lucro de FLV.

</details>

---

<details>
<summary><b>📦 04 SmartValidity - Controle de Validade e Fluxo PVPS/FEFO</b></summary>
<br>

* **Gargalo Atendido:** Rastreabilidade de Lotes e Priorização da Cadeia de Vencimentos (Estoque & Prevenção)
* **PROBLEMA DETECTADO:** O controle manual de validade e a organização das mercadorias dificultam a identificação de produtos antigos no recebimento, estoque e gôndolas. Produtos mais novos podem bloquear lotes antigos, aumentando o risco de vencimentos e perdas financeiras.
* **SOLUÇÃO PROPOSTA:** Criar um sistema de rastreabilidade que acompanhe os produtos desde o recebimento, registrando lote, validade e localização no estoque e nas gôndolas. O sistema utiliza o conceito PVPS/FEFO (Primeiro que Vence, Primeiro que Sai), emitindo alertas para lotes com vencimento próximo e mercadorias antigas bloqueadas.

<details>
<summary>🟢 CURTO PRAZO</summary>
<blockquote>
Registro dos lotes e datas de validade no recebimento, permitindo que o sistema determine a prioridade de movimentação conforme a proximidade do vencimento.
</blockquote>
</details>

<details>
<summary>🟡 MÉDIO PRAZO</summary>
<blockquote>
Vinculação dos produtos às localizações do estoque e das gôndolas, alertando sobre itens antigos bloqueados e sugerindo ações promocionais.
</blockquote>
</details>

<details>
<summary>🔵 LONGO PRAZO</summary>
<blockquote>
Integração com RFID, leitores automáticos, sensores ou IoT para acompanhar a movimentação do produto sem a necessidade de conferências manuais.
<br><br>
🔗 <b>Ver modelo de dados:</b> <a href="banco_dados.sql#L35">Modelagem Lógica do Estoque por Posição</a>
</blockquote>
</details>

<br>

> 📌 **ALGORITMO DE PRIORIZAÇÃO FEFO & MATRIZ DE AÇÃO PREVENTIVA**
> O gerenciamento inteligente de validade transforma a auditoria passiva em ações proativas antes da ocorrência da perda:
> - **Janelas de Criticidade Automatizadas:**
>   - **Zona Amarela (30 dias para o vencimento):** Emissão de alerta no coletor do repositor para abastecimento prioritário na gôndola.
>   - **Zona Laranja (15 dias para o vencimento):** Notificação automática ao sistema comercial para aplicação de etiqueta de desconto dinâmico.
>   - **Zona Vermelha (7 dias para o vencimento):** Indicação para recolhimento e direcionamento imediato para a área de padaria/produção interna.
> - **Acurácia no Recebimento:** Bloqueio automático de Notas Fiscais no WMS caso os produtos entregues pelo fornecedor tenham shelf-life menor do que o acordo comercial da rede.

</details>

---

<details>
<summary><b>📲 05 ReverseFlow Mobile - Triagem Rastreável de Abandonos</b></summary>
<br>

* **Gargalo Atendido:** Gestão da Cadeia Fria, Rastreio de Devoluções e Engajamento (Logística Reversa)
* **PROBLEMA DETECTADO:** Produtos abandonados pelos clientes se acumulam nas frentes de caixa e permanecem fora dos setores por longos períodos. Perecíveis refrigerados ficam sujeitos à quebra da cadeia fria (perda total), enquanto outros itens se perdem ou misturam durante a triagem.
* **SOLUÇÃO PROPOSTA:** Aprimorar a triagem substituindo carrinhos comuns por uma estrutura dedicada com 6 carrinhos exclusivos por setor/categoria. O operador utiliza o coletor móvel para identificar e priorizar os refrigerados. A solução evolui para rastreamento via QR Code/RFID e um programa de incentivo para clientes que concluem compras sem abandonos.

<details>
<summary>🟢 CURTO PRAZO</summary>
<blockquote>
Destinar 6 carrinhos exclusivos para triagem por setor. Mapear gôndolas com as letras da loja e usar coletor móvel para resgate prioritário de perecíveis.
</blockquote>
</details>

<details>
<summary>🟡 MÉDIO PRAZO</summary>
<blockquote>
Identificar carrinhos por QR Code registrando produto, horário e setor de destino. Sistema emite alertas quando itens excedem o tempo de permanência fora do setor.
</blockquote>
</details>

<details>
<summary>🔵 LONGO PRAZO</summary>
<blockquote>
Carrinhos tecnológicos com conservação térmica e RFID. Criação de programa de incentivo para clientes que concluem a compra sem abandonar produtos.
<br><br>
🔗 <b>Ver controle móvel:</b> <a href="caixa_inteligente.py#L105">Lógica da Ronda e Alerta de Perecíveis</a>
</blockquote>
</details>

</details>

---

## 📊 06 Matriz de Impacto e Viabilidade Operacional

| Iniciativa | Gargalo Atendido | Complexidade | Ganhos Esperados |
| :--- | :--- | :--- | :--- |
| **SmartCheckout** | Trancamento por QR Code | Baixa (Fase 1) | Eliminação de travamentos e filas no checkout. |
| **Menu Flip** | Etiquetas de FLV/Açougue rasgadas | Baixa (Fase 1) | Redução do tempo de espera e eliminação do retrabalho. |
| **VisualCheckout** | Demora e erro na digitação de PLUs | Média | Registro ágil de hortifrúti com menor margem de erro. |
| **SmartValidity** | Perda de produtos por vencimento | Média | Garantia do fluxo PVPS/FEFO e redução de quebras. |
| **ReverseFlow** | Quebra da cadeia fria em abandonos | Média / Alta | Preservação de perecíveis e devolução organizada aos setores. |

---

## 🎯 OBJETIVO GERAL DO ECOSSISTEMA SMARTRETAIL
As cinco propostas seguem uma mesma lógica: começar com melhorias simples e aplicáveis à operação atual e evoluir gradualmente para soluções digitais e automatizadas[cite: 1]. O objetivo é reduzir falhas operacionais, tempo de atendimento, perdas de produtos e tarefas manuais, utilizando tecnologia de forma progressiva e compatível com a realidade da loja Sobradinho/DF[cite: 1].
