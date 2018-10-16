# CURSO ESP8266
## Especificações técnicas

### Modos de boot

O ESP8266 possui basicamente três métodos de inicialização:

1- **Modo UART**: O microcontrolador não inicia a leitura da memória flash para execução e aguarda recebimento de dados (como atualização de firmware) pela UART (TX/RX).

2- **Modo Flash**: É o modo onde o MCU realiza a leitura da memória flash e a executa as instruções.

3- **Modo SDIO**: Modo em que é lido de uma memória externa (SD card) as instruções a serem executadas. *Este modo não é interesse de estudo/aplicação do curso*.

|             | GPIO0      | GPIO2      |   GPIO15 |
|-------------|------------|------------|----------|
|   Modo UART | GND        | VCC        | GND      |
|  Modo Flash | VCC        | VCC        | GND      |
|  Modo SDIO  | DON'T CARE | DON'T CARE | VCC      |

## Micropython

### Instalação/Preparação (Windows WSL Ubuntu 18.04.1 LTS~)
  
1.  Tenha certeza de que você possui instalado
- Python3.6
```
python3 --version
```

- pip3 
```
sudo apt update
sudo apt install python3-pip
```

- virtualenv
```
pip3 install virtualenv
```

- virtualenvwrapper (facilita sua vida 😁))
```
pip3 install virtualenvwrapper
```

- Adicione-o no seu `PATH`. Para isso, adicione o seguinte código no seu `.bashrc` (~/.bashrc)

```
export VIRTUALENVWRAPPER\_PYTHON=/usr/bin/python3
export WORKON\_HOME=~/.virtualenvs
source '/home/SEU_USUÁRIO/.local/bin/virtualenvwrapper.sh'
```

> Certifique-se de alterar `SEU_USUARIO` pelo nome do seu usuário.

- Dê um source no `.bashrc`

```
source ~/.bashrc
```


2.  Clone esse repositório

```
git clone https://github.com/GabrielMMelo/esp8266_course
cd esp8266_course
```

3.  Conecte o ESP8266, via usb, no seu computador.

 > Tenha certeza que o dispositivo está em **MODO UART**.

4.  Confira se seu computador reconheceu o dispositivo:
  
```
ls /dev/ | grep ttyS{número da porta COM}$
```

Por exemplo, se minha porta é a `COM4`:

```
ls /dev/ | grep ttyS4$
```

>  A porta COM padrão é `USB0`, i.e. `/dev/ttyUSB0`

> Não é comum mas as portas podem se alterar a cada nova conexão estabelecida.

> **DICA**: Por usar o Linux como subsistema, identifiquei a porta através do Gerenciador de dispositivos do Windows.

5.  Dê permissões de leitura/escrita na porta:

```
sudo chmod 776 /dev/ttyS{número da porta COM}
```

6.  Crie uma virtualenv aqui 

```
mkvirtualenv esp8266-esptool
```

7.  Então instale a ferramenta esptool.py para upload e reset do firmware

```
pip install esptool
```

8.  Realize um teste para ler o `MAC ADDRESS` do dispositivo

```
esptool.py -p /dev/ttyS{número da porta COM} -b 115200 read_mac
```

> Caso o teste não seja bem sucedido, revise a porta utilizada e o procedimento de instalação

9.  Formate a FlashROM do dispositivo

```
esptool.py -p /dev/ttyS{número da porta COM} -b 115200 erase\_flash 
```

10. Faça o download do binário do firmware

```
wget http://micropython.org/resources/firmware/esp8266-20180718-v1.9.4-272-g46091b8a.bin -P ./bin
```

> Foi usada o último Daily build até a data atual (16/10/18), disponível na [fonte oficial](http://micropython.org/download#esp8266)

11. Instale o firmware
  
```
  esptool.py -p /dev/ttyS{número da porta COM} -b 115200 write\_flash --flash\_size=detect -fm qio 0 bin/esp8266-20180718-v1.9.4-272-g46091b8a.bin
```


12.  Criar outra virtualenv aqui

```
mkvirtualenv esp8266-mpfshell
```

13. Clone o projeto mpfshell

```
git clone https://github.com/GabrielMMelo/mpfshell 
cd mpfshell
```

14. Instale as dependências

```
pip install -r requirements.txt
```

15. Por fim, instale o mpfsheel

```
python setup.py install
```

 > Antes de iniciar o mpfshell, certifique-se de alterar o modo do dispositivo para **MODO FLASH**. Para isso, desligue o dispositivo, altere a conexão na `GPIO0` para um nível lógico **ALTO** e o ligue novamente.

### mpfshell
  
  É um explorador de arquivos, via shell, para dispositivos _ESP8266_ com Micropython. O módulo permite acesso ao `REPL`, que é um ambiente interativo de acesso ao Micropython.
    
  Para executá-lo, certifique-se de estar em **MODO FLASH** e digite:

```
mpfshell
```

#### Comandos básicos

- Abre dispositivo na porta especificada

```
open ttyS{porta\_com}
```
  
- Lista arquivos/diretórios do diretório corrente do dispositivo (ESP8266)

```
 ls
```

- Lista arquivos/diretórios do diretório corrente do seu computador

```
lls
```

- Upload de arquivo x.py para o dispositivo

```
put x.py
```

- Download de arquivo x.py do dispositivo

```
get x.py
```

- Delete o arquivo x.py do dispositivo

```
rm x.py
```

Inicia o `REPL`

```
repl
```

Saia do `REPL`

```
ctrl+k
```


## SDK (_esp-open-sdk_)
### Instalação e preparação do ambiente
1. Clone o repositório do projeto
```
git clone --recursive https://github.com/pfalcon/esp-open-sdk.git
```

2. Instale as dependências

```
sudo apt-get install make unrar-free autoconf automake libtool gcc g++ gperf \
    flex bison texinfo gawk ncurses-dev libexpat-dev python-dev python python-serial \
        sed git unzip bash help2man wget bzip2 libtool-bin
```

3. Construa o projeto (Deve levar de 40 ~ 60 minutos)

```
(sudo) make 
```

4. Defina xtensa-lx106-elf-gcc no seu `PATH`

> O exato comando para fazê-lo será exibido ao final da construção do projeto
