Api em Python com Flask, para a devover dados de uma raspagem, no formato json.

Iniciando o projeto

Verifique sua versão do Python, esta aplicação foi feita com Python3, versão 3.7.4

    pip install pipenv

    pipenv shell

    pipenv install

Rodando o Projeto

    python run.py

Rotas

'/' -> Home, devolve animes lançados recentemente, no site alvo.
    São seriaziados em formato:
        "1" {
            "title",
            "image",
            "url" -> Url para ser enviada à rota do player.
            "episode",
            "timer"
        }
    Os "cards" se iniciam com 1 e não 0.
'/player/[id]' -> Devolve os links dos videos referente ao episódio na lista de Home, representado por um numero formatado como string.
    {
        "fhd",
        "hd",
        "sd"
    }
'/[id]' -> Pesquisa de animes no site alvo. [id] é uma string.
    Exemplo: "Naruto Shippuden"
'/anime_page/[id]' -> Cabeçalho da pagina do anime escolindo na lista de '/[id]'.
'/anime_page_eps/[id]' -> Dados dos episódios do anime escolhido de '/[id], serializados como os "cards" de Home.
'/player/page/[id]' -> Retorna os links do episodio escolhido.
