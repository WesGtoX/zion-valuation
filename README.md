# Zion Valuation

Simple "Crawler/Spider" to collecting some information from a specific website.

Website: [Martinelli Imobiliária](https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&finalidade=0&dormitorio=0&garagem=0&vmi=&vma=)

## Run the Crawler

- To run the crawler install Pipenv:
> `pip install pipenv`

- Install the dependencies:
> `pipenv install`

- Active the virtual environment:
> `pipenv shell`

- Run the crawler:
> `cd imoveismartinelli/`
> `scrapy crawl imoveis -o crawler_imoveis.csv`


Extracted Items:
> - Preço [price] (decimal);
> - Área [area] (decimal);
> - Cód [id] (string);


## Author

- [Wesley Mendes](https://github.com/WesGtoX)

## License

[MIT](LICENSE)