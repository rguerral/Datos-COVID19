'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

"""
Utilidades genéricas
"""
import pandas as pd


def regionName(df):
    df["Region"] = df["Region"].replace({"Tarapaca": "Tarapacá", "Valparaiso": "Valparaíso",
                                         "Del Libertador General Bernardo O’Higgins": "O’Higgins", "Nuble": "Ñuble",
                                         "Biobio": "Biobío", "La Araucania": "Araucanía", "Los Rios": "Los Ríos",
                                         "Aysen": "Aysén", "Magallanes y la Antartica": "Magallanes"
                                         })

def comunaName(df):
    df["Comuna"] = df["Comuna"].replace({"Camina": "Camiña", "Ollague": "Ollagüe", "Maria Elena": "María Elena",
                                         "Copiapo": "Copiapó", "Chanaral": "Chañaral", "Vicuna": "Vicuña",
                                         "Combarbala": "Combarbalá", "Rio Hurtado": "Río Hurtado",
                                         "Valparaiso": "Valparaíso", "Concon": "Concón",
                                         "Juan Fernandez": "Juan Fernández", "Puchuncavi": "Puchuncaví",
                                         "Vina del Mar": "Viña del Mar", "Santa Maria": "Santa María",
                                         "Quilpue": "Quilpué", "Olmue": "Olmué", "Donihue": "Doñihue",
                                         "Machali": "Machalí", "Requinoa": "Requínoa", "Chepica": "Chépica",
                                         "Constitucion": "Constitución", "Rio Claro": "Río Claro", "Curico": "Curicó",
                                         "Hualane": "Hualañé", "Licanten": "Licantén", "Vichuquen": "Vichuquén",
                                         "Colbun": "Colbún", "Longavi": "Longaví", "Concepcion": "Concepción",
                                         "Tome": "Tomé", "Canete": "Cañete", "Tirua": "Tirúa", "Mulchen": "Mulchén",
                                         "Santa Barbara": "Santa Bárbara", "Alto Biobio": "Alto Biobío",
                                         "Pitrufquen": "Pitrufquén", "Pucon": "Pucón", "Tolten": "Toltén",
                                         "Vilcun": "Vilcún", "Curacautin": "Curacautín", "Puren": "Purén",
                                         "Traiguen": "Traiguén", "Cochamo": "Cochamó", "Maullin": "Maullín",
                                         "Curaco de Velez": "Curaco de Vélez", "Puqueldon": "Puqueldón",
                                         "Queilen": "Queilén", "Quellon": "Quellón", "Rio Negro": "Río Negro",
                                         "Chaiten": "Chaitén", "Futaleufu": "Futaleufú", "Hualaihue": "Hualaihué",
                                         "Aisen": "Aisén", "Aysen": "Aisén", "OHiggins": "O'Higgins", 
                                         "Rio Ibanez": "Río Ibáñez", "Rio Verde": "Río Verde", "Antartica": "Antártica",
                                         "Conchali": "Conchalí", "Estacion Central": "Estación Central",
                                         "Maipu": "Maipú", "Nunoa": "Ñuñoa", "Penalolen": "Peñalolén",
                                         "San Joaquin": "San Joaquín", "San Ramon": "San Ramón",
                                         "San Jose de Maipo": "San José de Maipo", "Alhue": "Alhué", 
                                         "Curacavi": "Curacaví", "Maria Pinto": "María Pinto", "Penaflor": "Peñaflor",
                                         "Mafil": "Máfil", "La Union": "La Unión", "Rio Bueno": "Río Bueno",
                                         "Chillan": "Chillán", "Chillan Viejo": "Chillán Viejo", "Quillon": "Quillón",
                                         "Niquen": "Ñiquén", "San Fabian": "San Fabián", "San Nicolas": "San Nicolás"
                                         })

def transpone_csv(csvfile):
    df = pd.read_csv(csvfile)
    return(df.T)

