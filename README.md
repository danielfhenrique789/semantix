##Desafio Semantix <br /><br />
Autor: Daniel Fernandes Henrique<br />
Data: 23/01/2020



Passos para executar o desafio.

1 - Clonar o repositório ou fazer o download do projeto.
2 - Fazer o download dos arquivos access_log_Jul95 e access_log_Aug95 e mover para o diretório raíz do projeto.
(Esse processo é necessário pois os arquivos são grandes e não podem ser transferidos para o repositório GitHub.)
3 - Executar o programa main.py abrindo o terminal e digitando o comando: $ python main.py.
4 - Concluída a execução será gerado um arquivo output.txt, com as respostas do desafio.

PS: Se deseja apenas ver o resultado do desafio o mesmo se encontra no diretório do projeto com o nome "output.txt".





Resposta das questões dissertativas:

Qual o objetivo do comando cache em Spark?
Resp: O comando cache, tem como objetivo guardar informações de acesso à RDDs na memória para aumentar a velocidade de retorno de um processo em caso de reuso.

O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em
MapReduce. Por quê?
Resp: Há muitas razões que explicam a performace superior do Spark em relação ao MR. 
O Spark armazena seus dados em memória durante sua operação, enquanto MR necessita armazenar seus dados no HDFS durante o processo.
O Spark utiliza "lazy evaluation", que permite trafegar apenas a quantidade de dados necessária para uma determinada operação, enquanto o MR sempre carrega todos os dados.
O Spark mantem uma JVM rodando em cada node, permitindo uma execução direta de cada tarefa. Já o MR inicia uma JVM para cada tarefa, o que demanda tempo devido à carga dos JARs.

Qual é a função do SparkContext?
Resp: O SparkContext permite a visualização do status atual da aplicação, assim como configurar os atributos para variadas funcionalidades do Spark. É através dele que se gerencia os Jobs, acesso a serviços, listeners e persistência de RDDs.

Explique com suas palavras o que é Resilient Distributed Datasets? (RDD).
Resp: RDD é uma abreviação de Resilient Distributed Datasets e a principal forma de trabalhar com dados de forma distribuída nos clusters.

GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?
Resp: O GroupByKey faz a junção de dados de diferentes partições em um outro RDD, trafegando muitos dados no processo. Já o reduceByKey jaz a junção dos dados em uma mesma máquina, diminuindo o custo de processamento.

Explique o que o código Scala abaixo faz.

Resp: Lê um arquivo texto de um repositório do HDFS, agrupa e conta quantas vezes cada palavra aparece no texto. Em seguida guarda o resultado em outro arquivo no HDFS.


