# 🧩 Onde São Usados os Padrões de Projeto (Prototype, Proxy e State)

---

## 🌀 Prototype

O **Prototype** é um padrão **criacional** que permite **clonar objetos existentes** em vez de criar do zero.

### ✨ Para que serve:
- Evita o custo de criar objetos complexos 🏗️  
- Permite copiar objetos com estado complexo 🔄  
- Criação dinâmica sem acoplar ao tipo concreto 🧩  

### 🛠️ Onde é usado:
- Jogos: duplicar personagens ou itens 🎮  
- Aplicações gráficas: copiar formas ou elementos visuais 🖌️  
- Sistemas com objetos complexos, templates ou documentos 📝  

---

## 🛡️ Proxy

O **Proxy** é um padrão **estrutural** que fornece um **substituto ou representante** de outro objeto para controlar o acesso a ele.

### ✨ Para que serve:
- Controlar acesso a objetos sensíveis 🔑  
- Adiar a criação de objetos pesados ⏳  
- Adicionar funcionalidades extras (log, cache, segurança) 📝  

### 🛠️ Onde é usado:
- Segurança: validar permissões antes de executar ações 🔐  
- Acesso remoto: objetos que estão em outro servidor 🌐  
- Cache e Lazy Loading: otimizar performance ⚡  

---

## 🔄 State

O **State** é um padrão **comportamental** que permite que um objeto **altere seu comportamento quando seu estado interno muda**.

### ✨ Para que serve:
- Evitar grandes blocos de `if/else` ou `switch` 🔀  
- Encapsular estados e transições de forma organizada 📦  
- Facilitar manutenção e extensibilidade do comportamento do objeto 🛠️  

### 🛠️ Onde é usado:
- Dispositivos eletrônicos: ligado, desligado, standby ⚡  
- Jogos: personagem em diferentes modos (correr, atacar, pular) 🎮  
- Sistemas de workflow ou máquinas de estado 🔄  

---

💡 **Observação:** Foi usado o **ChatGPT** para as escritas e o **PlantUML** para gerar os diagramas UML.  

📚 **Referência:**  
Conteúdo baseado e adaptado a partir do site [Refactoring Guru](https://refactoring.guru/pt-br/design-patterns).
