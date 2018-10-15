# CURSO ESP8266

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

- virtualenvwrapper (opcional, mas facilita sua vida :) )
```
pip 3 install virtualenvwrapper
```

2.  Clone esse repositório

```
git clone https://github.com/GabrielMMelo/esp8266_course
cd esp8266_course
```

3.  Conecte o ESP8266, via usb, no seu computador.

 > Tenha certeza que o dispositivo está em **modo flash**.

4.  Confira se seu computador reconheceu o dispositivo:
  
```
ls /dev/ | grep ttyS{número da porta COM}$
```

Por exemplo, se minha porta é a COM4:

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
mkvirtualenv esp8266    #se estiver usando virtualenvwrapper
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
esptool.py -p /dev/ttyS{número da porta COM} -b 115200 erase\_flash -> para limpar a flash
```

10. Instale o firmware (demais imagens podem ser acessadas em: http://micropython.org/download#esp8266)
  
```
  esptool.py -p /dev/ttyS{número da porta COM} -b 115200 write\_flash --flash\_size=detect -fm qio 0 bin/esp8266-20180718-v1.9.4-272-g46091b8a.bin
```

> É altamente recomendado baixar o binário diretamente da [fonte oficial] (http://micropython.org/download#esp8266)

11.  Criar outra virtualenv aqui

```
mkvirtualenv esp8266-mpfshell
```

12. Clone o projeto mpfshell

```
git clone https://github.com/wendlers/mpfshell 
cd mpfshell
```

13. Instale as dependências

```
pip install -r requirements.txt
```

14. Altere a versão do módulo `pyserial` para a `3.1`

```
pip install pyserial==3.1
```

15. Por fim, instale o mpfsheel

```
pip install mpfshell
```

### mpfshell
  
  É um explorador de arquivos, via shell, para dispositivos _ESP8266_ com Micropython. O módulo permite acesso ao `REPL`, que é um ambiente interativo de acesso ao Micropython.

#### Comandos básicos

- Abre dispositivo na porta especificada

```
open ttyS{porta\_com}
```
  
- Lista arquivos/diretórios do diretório corrente do seu computador

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
