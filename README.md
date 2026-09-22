# 📊 Pesquisa de Opinião - TudoWeb

Programa desenvolvido em Python para realizar uma pesquisa de opinião sobre o grau de satisfação dos clientes da empresa fictícia **TudoWeb**.

## 🎯 Objetivo

O programa realiza uma pesquisa com **50 entrevistados**, coletando:

- Nome do entrevistado;
- Idade;
- Opinião sobre o atendimento.

As opções de atendimento são:

- `1` - ⭐ Excelente
- `2` - 👍 Bom
- `3` - 😞 Ruim

Ao final da pesquisa, o programa informa a quantidade de respostas **Excelente** e **Ruim**.

## 🛠️ Tecnologias utilizadas

- 🐍 Python
- 💻 Visual Studio Code

## 🔄 Funcionamento

O programa utiliza uma estrutura de repetição `for` para realizar a pesquisa com 50 pessoas.

Para cada entrevistado, são solicitados o nome, a idade e a opinião sobre o atendimento.

A estrutura `if` é utilizada para verificar a resposta:

```python
if opiniao == 1:
    opiniao_excelente += 1

if opiniao == 3:
    opiniao_ruim += 1
```
---

👩‍💻 **Desenvolvido por Gabriely Cezario**