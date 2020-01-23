# -*- coding: utf-8 -*-
from pyspark import SparkConf
from pyspark import SparkContext as sc
from operator import add

file_obj = open("./output.txt", "w")

def print_first_question(log_columns):
    hosts = log_columns.map(lambda column: (column[0], 1)).reduceByKey(add)
    print_result(hosts.collect(), "Numero de hosts Unicos")

def print_second_question(log_columns):
    http_status = hosts_values.map(lambda column: (column[len(column) - 2], 1)).reduceByKey(add)
    print_result(http_status.filter(lambda x: x[0] == '404').collect(), "Total de erros 404.")

def print_third_question(hosts_values):
    log = hosts_values.filter(lambda column: column[len(column) - 2] == '404')
    urls = log.map(lambda column: (column[len(column) - 4], 1)).reduceByKey(add).sortBy(lambda x: x[1], False).take(5)
    print_result(urls, "Os 5 URLs que mais causaram erro 404")

def print_fourth_question(hosts_values):
    log = hosts_values.filter(lambda column: column[len(column) - 2] == '404')
    timestamp = log.map(lambda column: column[0].split(":"))
    days = timestamp.map(lambda column: (column[0], 1)).reduceByKey(add)
    print_result(days.collect(), "Quantidade de erros 404 por dia.")

def print_fifth_question(hosts_values):
    total_bytes = hosts_values.map(lambda column: (column[len(column) - 1], 1)).values().sum()
    print_on_file("###### O total de bytes retornados ######")
    print_on_file(str(total_bytes))

def print_on_file(text):
    file_obj.write(text +'\n')

def print_result(output, msg):
    print_on_file("###### " + msg + "######")
    for (word, count) in output:
        print_on_file("%s: %i" % (word, count))
    print_on_file("\n \n \n")

if __name__ == '__main__':
    try:
        # Leitura dos dados.
        sc = sc.getOrCreate(SparkConf().setMaster("local[*]"))
        log_Jul95 = sc.textFile("./access_log_Jul95")
        log_Aug95 = sc.textFile("./access_log_Aug95")
        log = log_Jul95.union(log_Aug95)

        # Linhas do arquivo de log.
        lines = log.flatMap(lambda line: line.split("\n"))

        # Separa o nome dos hosts dos demais dados.
        log_columns = lines.map(lambda column: column.split(" - - "))
        log_columns.cache()

        # Imprime Número de hosts únicos
        print_first_question(log_columns)

        # Separa os dados de log para cada registro de host cadastrado.
        hosts_values = log_columns.map(lambda column: column[1].split(" ") if len(column) > 1 else [None] * 100)

        hosts_values.cache()
        log_columns.unpersist()

        # Imprime O total de erros 404.
        print_second_question(hosts_values)

        # Imprime Os 5 URLs que mais causaram erro 404.
        print_third_question(hosts_values)

        # Imprime Quantidade de erros 404 por dia.
        print_fourth_question(hosts_values)

        # Imprime O total de bytes retornados
        print_fifth_question(hosts_values)
    except Exception as ex:
        raise ex
    finally:
        print("Fim da execução.")


