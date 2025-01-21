import statistics
from lxml import html
from bs4 import BeautifulSoup, Comment
import pandas as pd
import requests

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import plotly.graph_objects as go



teams_adress_A = {'palmeiras' : 'palmeiras/1963', 'internacional' : 'internacional/1966', 'flamengo' : 'flamengo/5981', 'fluminense' : 'fluminense/1961',
'corinthians' : 'corinthians/1957', 'athletico paranaense' : 'athletico/1967', 'atletico mineiro' : 'atletico-mineiro/1977',
'america mineiro' : 'america-mineiro/1973', 'fortaleza' : 'fortaleza/2020', 'botafogo' : 'botafogo/1958', 'santos' : 'santos/1968',
'sao paulo' : 'sao-paulo/1981', 'bragantino' : 'red-bull-bragantino/1999', 'goias' : 'goias/1960', 'coritiba' : 'coritiba/1982',
'ceara' : 'ceara/2001', 'cuiaba' : 'cuiaba/49202', 'atletico goianiense' : 'atletico-goianiense/7314', 'avai' : 'avai/7315', 'juventude' : 'juventude/1980'}

teams_adress_B = {'cruzeiro' : 'cruzeiro/1954', 'gremio' : 'gremio/5926', 'vasco' : 'vasco-da-gama/1974', 'bahia' : 'bahia/1955', 'ituano' : 'ituano/2025',
'londrina' : 'londrina/2022', 'sport' : 'sport-recife/1959', 'sampaio correa' : 'sampaio-correa/2005', 'criciuma' : 'criciuma/1984', 'crb' : 'crb/22032',
'guarani' : 'guarani/1972', 'vila nova' : 'vila-nova/2021',  'ponte preta' : 'ponte-preta/1969', 'tombense' : 'tombense/87202', 'chapecoense' : 'chapecoense/21845',
'csa' : 'csa/2010', 'novorizontino' : 'novorizontino/135514', 'brusque' : 'brusque-fc/21884', 'operario' : 'operario/39634', 'nautico' : 'nautico/2011'}

browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \(KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}

base_api = 'https://api.sofascore.com/api/v1/team/'
end_api = '/statistics/overall'

def choose_team(time: str):
    data_list = []
    cont_url_list = 0

    division = input('Em qual divisao esta o time?').upper()

    if division == 'A':
        serie = '325'
        id_time = teams_adress_A[time.lower()][-4:]
        enpoint_17 = '13100'
        enpoint_18 = '16183'
        enpoint_19 = '22931'
        enpoint_20 = '27591'
        enpoint_21 = '36166'
        enpoint_22 = '40557'
    elif division == 'B':
        serie = '390'
        id_time = teams_adress_B[time.lower()][-4:]
        enpoint_17 = ''
        enpoint_18 = '16184'
        enpoint_19 = '22932'
        enpoint_20 = '27593'
        enpoint_21 = '36162'
        enpoint_22 = '40560'
    
    middle_api = f'/unique-tournament/{serie}/season/'

    urls_list = [
        base_api + id_time + middle_api + enpoint_17 + end_api,
        base_api + id_time + middle_api + enpoint_18 + end_api,
        base_api + id_time + middle_api + enpoint_19 + end_api,
        base_api + id_time + middle_api + enpoint_20 + end_api,
        base_api + id_time + middle_api + enpoint_21 + end_api,
        base_api + id_time + middle_api + enpoint_22 + end_api
    ]

    for url in urls_list:
        api_link = requests.get(url, headers=browsers).json()  # Correção aqui, adicione os parênteses
        if 'error' not in api_link:
            data = api_link['statistics']
            data['ano'] = 2017 + cont_url_list  # Define o ano baseado no índice
            data_list.append(data)
        cont_url_list += 1

    return data_list

