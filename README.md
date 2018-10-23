# LTMSimApi

## Requisitos principais
Para usar o LTMSimApi, é necessário instalar seus requisitos. O serviço roda em Python e se conecta ao MATLAB, por isso, ambos os programas devem ser instalados. Atenção nos detalhes da instalação do Python, pois é importante adicionar o mesmo ao PATH do Windows, para possibilitar o uso do pip de forma fácil.
* MATLAB
* [Python 3.6](https://www.python.org/downloads/release/python-367/) - Até o momento, a interface entre o MATLAB e o Python só é possível até a versão 3.6 do Python

## Instalação da API do MATLAB
Com o Python instalado, abra o Powershell em modo de administrador, vá para o diretório raiz do MATLAB e siga o caminho:
...
Matlab\extern\engines\python
...

Essa pasta contém um arquivo setup.py. Com Powershell dentro dessa pasta, digite o comando:
...
python setup.py install
...

Em caso de dúvidas, pode-se consultar a [documentação oficial](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html) do MATLAB.


## Requisitos secundários
Além do MATLAB e do Python, a aplicação ainda usa módulos prontos do Python que possibilitam diversos comportamentos importantes para o serviço. Para isso, usa-se a aplicação Powershell e o comando pip, que é responsável por buscar nos repositórios oficiais da linguagem Python e instalar os módulos necessários.
* flask
```
pip install flask
```
* flask_cors
```
pip install flask_cors
```
* requests
```
pip install requests
```

## Iniciando o serviço
* Faça o download do conteúdo desse repositório
* Execute o script "iniciar_servico.ps1"

Com isso, o serviço será exposto na porta 5000. Para que a tela web se conecte a esse serviço, é preciso que essa porta seja exposta para a internet. Durante a apresentação do projeto, usei a aplicação [ngrok](https://ngrok.com/), que por mais que sua versão gratuita seja limitada, a mesma ainda é bem simples. Tendo o endereço web no qual o serviço está exposto, só preciso que me enviem esse endereço para que possa apontar a tela Web para que possa acessa-lo, ou então, podem alterar manualmente a linha 2620 [desse arquivo](https://github.com/henriquekfmaia/henriquekfmaia.github.io/blob/master/main.bundle.js).

Caso ocorra erro por falta de alguma depenência, pode-se instalar a mesma usando o respectivo comando do pip.
