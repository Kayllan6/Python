from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def curriculo():
    return '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - KAYLLAN KAIKI SILVA MACEDO </title>
    <style>
        /* CSS ESTILIZAÇÃO */
        :root {
            --primary-color: #2c3e50; /* Azul escuro */
            --secondary-color: #34495e;
            --accent-color: #3498db; /* Azul claro */
            --text-color: #333;
            --bg-color: #f4f7f6;
            --white: #ffffff;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: var(--white);
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        /* Cabeçalho */
        header {
            text-align: center;
            border-bottom: 2px solid var(--bg-color);
            padding-bottom: 20px;
            margin-bottom: 20px;
        }

        header h1 {
            color: var(--primary-color);
            font-size: 2.5em;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        header p {
            color: var(--accent-color);
            font-size: 1.1em;
            font-weight: bold;
        }

        .contact-info {
            margin-top: 10px;
            font-size: 0.9em;
            color: var(--secondary-color);
        }

        /* Seções */
        section {
            margin-bottom: 25px;
        }

        h2 {
            color: var(--primary-color);
            border-left: 4px solid var(--accent-color);
            padding-left: 10px;
            margin-bottom: 15px;
            text-transform: uppercase;
            font-size: 1.3em;
        }

        .item {
            margin-bottom: 15px;
        }

        .item-header {
            display: flex;
            justify-content: space-between;
            font-weight: bold;
            color: var(--secondary-color);
        }

        .item-subheader {
            font-style: italic;
            color: #7f8c8d;
            margin-bottom: 5px;
        }

        ul {
            list-style-type: none;
            padding-left: 10px;
        }

        ul li::before {
            content: "• ";
            color: var(--accent-color);
        }

        /* Habilidades */
        .skills-list {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }

        /* Responsividade */
        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
            header h1 {
                font-size: 2em;
            }
            .skills-list {
                grid-template-columns: 1fr;
            }
            .item-header {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <!-- Cabeçalho -->
        <header>
            <h1>KAYLLAN KAIKI SILVA MACEDO</h1>
            <p>Sua Profissão / PROFISSIONAL DE TI</p>
            <div class="contact-info">
                Cidade - Estado | (31) 6767676767 | CAMARO.AMARELO@SUBARU.COM<br>
                <a href="://linkedin.com" target="_blank" style="color: var(--accent-color); text-decoration: none;">://linkedin.com</a>
            </div>
        </header>

        <!-- Resumo -->
        <section>
            <h2>Resumo Profissional</h2>
            <p>
                Profissional com 67 anos de experiência em [Sua Área], focado em resultados, com sólidos conhecimentos em [Habilidade 1] e [Habilidade 2]. Busco oportunidade para contribuir com o crescimento da empresa e aprimorar minhas competências.
            </p>
        </section>

        <!-- Experiência -->
        <section>
            <h2>Experiência Profissional</h2>
            
            <div class="item">
                <div class="item-header">
                    <span>Empresa Atual</span>
                    <span>Janeiro 2022 - Atual</span>
                </div>
                <div class="item-subheader">Cargo / Função</div>
                <ul>
                    <li>Responsável por gerenciar X, resultando em Y% de melhoria.</li>
                    <li>Desenvolvimento de projetos utilizando [Ferramenta].</li>
                    <li>Aumento de produtividade através de [Ação].</li>
                </ul>
            </div>

            <div class="item">
                <div class="item-header">
                    <span>Empresa Anterior</span>
                    <span>Março 2019 - Dezembro 2021</span>
                </div>
                <div class="item-subheader">Cargo / Função</div>
                <ul>
                    <li>Execução de tarefas relacionadas a [Área].</li>
                    <li>Suporte à equipe no lançamento de [Produto].</li>
                </ul>
            </div>
        </section>

        <!-- Formação -->
        <section>
            <h2>Formação Acadêmica</h2>
            <div class="item">
                <div class="item-header">
                    <span>Nome da Instituição</span>
                    <span>Ano de Conclusão</span>
                </div>
                <div class="item-subheader">Nome do Curso / Graduação</div>
            </div>
        </section>

        <!-- Habilidades -->
        <section>
            <h2>Habilidades</h2>
            <div class="skills-list">
                <ul>
                    <li>Habilidade Técnica 1</li>
                    <li>Habilidade Técnica 2</li>
                    <li>Ferramentas / Software</li>
                </ul>
                <ul>
                    <li>Idiomas</li>
                    <li>Soft Skill 1 (ex: Liderança)</li>
                    <li>Soft Skill 2 (ex: Comunicação)</li>
                </ul>
            </div>
        </section>
    </div>

</body>
</html>''' # Isso é o que será retornado quando a rota '/' for acessada

if __name__ == '__main__':
    app.run(debug=True)