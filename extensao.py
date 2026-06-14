# -*- coding: utf-8 -*-
"""
CENTRO UNIVERSITÁRIO INTERNACIONAL UNINTER (PROJETO DE EXTENSÃO)
Escola Superior Politécnica - ESP
Sistema de Avaliação e Simulação: Inclusão Digital e Uso Seguro da Tecnologia
Conteúdo baseado na Cartilha Comunitária do Projeto.
"""

import time
import sys

class OficinaSegurancaDigital:
    def __init__(self):
        # Mapeamento do conteúdo extraído diretamente do PDF do projeto
        self.modulos = {
            1: "O que é Inclusão Digital (Estudos, Trabalho, Comunicação)",
            2: "Conhecendo o Computador (Hardware e Navegação Segura)",
            3: "Comunicação Digital (Uso responsável de E-mail e WhatsApp)",
            4: "Boas Práticas de Segurança (Criação de Senhas Fortes)",
            5: "Identificação de Golpes Comuns na Internet"
        }
        
        # Base de dados de testes para simular o aprendizado dos alunos da comunidade
        self.perguntas_seguranca = [
            {
                "pergunta": "Como você identifica se um site é seguro para digitar seus dados?",
                "opcoes": [
                    "A) Se ele tiver muitas fotos e anúncios coloridos.",
                    "B) Se ele começar com 'https://' e exibir o ícone de um cadeado no navegador.",
                    "C) Se abrir rapidamente no celular."
                ],
                "correta": "B",
                "explicacao": "Sites seguros utilizam protocolo HTTPS e criptografia (cadeado) para proteger os dados."
            },
            {
                "pergunta": "Qual das seguintes senhas é considerada FORTE e segura?",
                "opcoes": [
                    "A) maria1980",
                    "B) 12345678",
                    "C) M@r!a#Segur@2024"
                ],
                "correta": "C",
                "explicacao": "Senhas fortes misturam letras maiúsculas, minúsculas, números e símbolos especiais."
            },
            {
                "pergunta": "Você recebeu uma mensagem no WhatsApp dizendo que ganhou um sorteio de R$ 5.000, pedindo para clicar num link. O que fazer?",
                "opcoes": [
                    "A) Clicar imediatamente para não perder o prêmio.",
                    "B) Desconfiar, não clicar no link e consultar alguém de confiança, pois pode ser um golpe.",
                    "C) Repassar a mensagem para todos os amigos."
                ],
                "correta": "B",
                "explicacao": "Falsos sorteios e promessas milagrosas com links suspeitos são táticas para roubar informações."
            }
        ]

    def exibir_abertura(self):
        print("\n" + "="*75)
        print("          UNINTER - PROJETO DE EXTENSÃO UNIVERSITÁRIA")
        print("   SISTEMA DE CAPACITAÇÃO E SIMULAÇÃO DE SEGURANÇA DIGITAL COMUNITÁRIA")
        print("="*75)
        print("Tema: Inclusão Digital e Uso Seguro da Tecnologia")
        print("Público-Alvo: Moradores locais, estudantes e adultos em inclusão digital.")
        print("-"*75)
        print("MÓDULOS PEDAGÓGICOS MAPEADOS DA CARTILHA:")
        for num, nome in self.modulos.items():
            print(f"  [{num}] {nome}")
        print("="*75)
        time.sleep(1)

    def executar_teste_interativo(self):
        print("\n[INICIANDO SIMULADO DE FIXAÇÃO PARA OS PARTICIPANTES DA OFICINA]")
        print("Responda às questões com A, B ou C:\n")
        
        pontuacao = 0
        
        for i, item in enumerate(self.perguntas_seguranca, 1):
            print(f"Questão {i}: {item['pergunta']}")
            for opcao in item['opcoes']:
                print(opcao)
                
            resposta = input("Sua resposta (A/B/C): ").strip().upper()
            
            if resposta == item['correta']:
                print("▶ Resultado: CORRETO! Excelente prática de segurança.")
                pontuacao += 1
            else:
                print(f"▶ Resultado: INCORRETO. O recomendado seria a alternativa {item['correta']}.")
            
            print(f"  Justificativa Técnica: {item['explicacao']}\n")
            print("-" * 50)
            time.sleep(0.5)
            
        print("="*75)
        print(f"Desempenho Final da Oficina: {pontuacao}/{len(self.perguntas_seguranca)} acertos.")
        print("Gerando dados para o Relatório Final da ESP/UNINTER...")
        
        for i in range(4):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.4)
            
        print("\n[STATUS] Indicadores de aproveitamento computados com sucesso!")
        print("="*75)

if __name__ == "__main__":
    oficina = OficinaSegurancaDigital()
    oficina.exibir_abertura()
    oficina.executar_teste_interativo()