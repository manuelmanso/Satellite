O objetivo do projeto é representar graficamente a órbita terrestre e os eixos do satélite que observa a estrela HD 7924 num espaço 3D. A informação necessária para esta representação está toda contida no ficheiro de texto satellite_data.txt. O projeto foi realizado com o Python e o module VPython para as representações em 3D.

O projeto está dividido em 3 ficheiros de código: satellite_main.py, get_info.py e sat_functions.py.

O ficheiro satellite_main.py é a partir do qual se corre o programa. Na função main() deste programa é inicialmente chamada a função get_info() do ficheiro get_info.py. Esta função obtém todos os 5799 conjuntos de informação contidos no ficheiro sattelite_data.txt, e ordena-os num dicionário de dicionários através da função create_sat_info_dict(). Cada conjunto do dicionário criado contém o nome do planeta HD 7924 b, o período de rotação do planeta HD 7924b, a declination e a right_ascension da estrela HD 7924, o tempo em formato de Julian Day desde 1/1/2000, a posição do satélite em km de acordo com o referencial J2000, e os quaternions que definem a rotação dos eixos do satélite.

Depois de obter toda a informação necessária, o programa desenha, através do module VPython, a janela de visualização, a Terra, o satélite, o tempo(em dia/hora/minuto) e os eixos do satélite.

De seguida, o programa entra no loop principal, em que, seguindo a ordem dos conjuntos de informação guardados no dicionário sat_info_dict, a posição do satélite e dos seus eixos vai sendo atualizada. Primeiro é obtida e atualizada a posição do satélite e a dos seus eixos. De seguida, obtém-se o quaternion, a declination e a right_ascension. Estes são usados como argumentos na função calc_sat_axis() do ficheiro sat_fucntions.py. Esta função calcula os eixos X, Y e Z do satélite. 

Primeiro é calculado o eixo Z, que representa o vetor que aponta para a estrela HD 7924, usando o vetor da declination e da right_ascension e depois adicionando-os um ao outro. 
O eixo X é calculado com a função vector_rotation_by_quaternion() e o quaternion e o vetor (1,0,0) como argumentos. Esta função utiliza o produto de Hamilton para devolver o vetor resultante da rotação, mas devido a um possível erro de cálculo, este vector não é ortogonal ao vetor do eixo Z, e por isso tem que ser chamada a função calc_x_axis(), com o vetor do eixo Z e o vetor resultante da rotação como argumentos, que devolve um vetor de para X que é ortogonal ao vetor do eixo Z.
Para calcular o eixo Y utiliza-se a função cross() do VPython para obter um vetor ortogonal ao eixo X e ao Z.
A função depois devolve os três eixos e estes são atualizados.

Por último, a função convert_julian_to_real_time() é chamada com a informação do tempo no formato de Julian Time como argumento, e devolve o tempo no formato dia/hora/minuto. A visualização do tempo no programa é depois atualizada.

Quando o programa chega ao fim da informação dada pelo ficheiro de texto satellite_data.txt, o satélite pára de orbitar a terra e a sua cor passa de vermelho para verde.
