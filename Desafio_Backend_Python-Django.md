
# Desafio - Pessoa Desenvolvedora de Software Backend

Na Portal Telemedicina trabalhamos com dados de saúde de milhares de pessoas. Alguns dos grandes desafios que encontramos diariamente são a modelagem, limpeza e garantia de qualidade dos dados. Com o uso do *framework* Django, muitas regras de negócio, validações automáticas na entrada do dado e *pipelines* automatizados com a filosofia TDD, conseguimos criar um *data warehouse* com boa usabilidade, integridade e fácil desenvolvimento. Dentre a enorme quantidade de dados de saúde produzidos diariamente, existem os exames clínicos. Exames são arquivos que podem estar em diferentes formatos, os mais comuns são: .dcm, .png, .pdf, .jpg.

### Proposta

Este teste tem o objetivo de avaliar sua experiência com Django, o uso de boas práticas e a capacidade de construir modelagens de dados coerentes e robustas.

O desafio consiste na criação de um *data warehouse* baseado em Django que acomode as seguintes informações:

* exames;
* paciente que realizou o exame;
* laudos destes exames;
* médicos que laudaram o exame;
* pacientes.

Um laudo, além das demais informações, deve possuir os seguintes campos:

* "report": é um texto contendo a avaliação médica. A escrita pode variar, simulando a forma não-padronizada com que os médicos escrevem seus laudos. Possíveis laudos indicando exames normais podem conter: "O Exame está normal", "exame normal", "conclusão: normal". Para exames com achados detectados, os médicos podem escrever laudos contendo "o exame esta alterado.", "o exame não esta normal", "exame nao normal", "exame alterado".
* "altered": indica se o médico detectou algum achado no exame. Este campo deve ser populado com base no "report" e não deve ser preenchido como valor de entrada do usuário.

### Requisitos

* Eu, como desenvolvedor gostaria de poder gerenciar os dados através de uma interface gráfica
* Eu, como usuário, desejo adicionar um novo laudo em forma de texto livre e receber o resultado em forma estruturada no seguinte formato: "{"altered": True}"
* Eu, como usuário, desejo editar ou excluir determinado exame;
* Eu, como usuário, desejo poder ver apenas os exames alterados e os exames não-alterados (e seus detalhes).

### Definição de Pronto

* A aplicação deve conter testes unitários automatizados (pytest ou outro), provando que os requisitos foram implementados e que é feita a cobertura dos problemas que podem ocorrer;
* Todas as rotas devem exigir autenticação, feita utilizando preferencialmente o DRF (Django Rest Framework);
* O código deve ter testes de qualidade de código (flake8) que rodam automaticamente ao se abrir um *pull-request* para branch principal (main ou master) no repositório;
* Adicionar ao README.md explicando como rodar o projeto, a explicação das tomadas de decisões que você fez;
* Usar um banco de dados do tipo SQlite e publicar o arquivo do banco, contendo alguns exemplos de dados, no repositório. Com isso, o avaliador poderá rodar seu projeto Django e verificar alguns cadastros.
 
### Critérios de Avaliação

* Organização do projeto: Avalia a estrutura do projeto, documentação e uso de controle de versão;
* Coerência: Avalia se os requisitos foram atendidos;
* Boas práticas: Avalia se o projeto segue boas práticas de desenvolvimento, incluindo segurança e otimização;
* Controle de Qualidade: Avalia se o projeto possui qualidade assegurada por testes automatizados e integração contínua;
* Qualidade da modelagem de dados;
* Qualidade da cobertura de testes unitários;
* Qualidade das validações automáticas de dados para garantia de que dados sujos não entrem no sistema;
* Uso de boas práticas de Django: índices, serializers, relacionamentos de dados, uso do clean, full_clean, @on_delete, select_related, prefetch_related, e outros;
* Qualidade de apresentação dos dados na interface gráfica: contém as informações necessárias? é possível filtrar pelos valores relevantes? utilizou o Django Template Language?

### Observações

* Todo o código deve ser em inglês;
* Preze pela simplicidade e resolução do problema com objetividade;
* Rodar seu código com o mínimo de interação é considerado importante;
* O uso de Docker é considerado um diferencial;
* Publicar o sistema na *cloud* é considerado um diferencial;
* Caso opte por utilizar um banco diferente do SQlite, faça o setup do mesmo utilizando o *docker-compose*;
* Use padrões REST e nomenclatura consistente nas rotas;
* A performance e a construção de funções simples e pequenas também serão avaliadas em todos os elementos do projeto;
* Utilizar o Django Model Form é considerado um diferencial;
* Confirme por e-mail o recebimento do teste técnico;
* Se desistir da realização do teste, por favor nos informe por e-mail;
* Não esqueça de colocar um arquivo README.md bem estruturado.

### Processo de submissão

* O desafio deve ser entregue pelo [GitHub](http://github.com/), [Bitbucket](http://bitbucket.org/) ou [GitLab](http://gitlab.com/). As URLs (do código fonte e do projeto acessível) devem ser enviada por e-mail.
* Qualquer dúvida em relação ao desafio, responderemos por e-mail. Nicholas Drabowski - nicholas@portaltelemedicina.com.br ou Luiz Roberto Lethang Rodolpho - luiz@portaltelemedicina.com.br

Você tem 5 dias úteis, contando a partir de amanhã, para concluir e enviar o endereço do repositório com a solução. Por favor, nos avise se precisar de mais tempo.

Bom trabalho!