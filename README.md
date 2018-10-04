# CURSO ESP8266

## Micropython

### Instalação/Preparação (Windows WSL Ubuntu 18.04.1 LTS~)
  
  Tenha certeza de que você possui instalado
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

- virtualenvwrapper (optional)
```
pip 3 install virtualenvwrapper
```

  Clone esse repositório

```
git clone https://github.com/GabrielMMelo/esp8266_course
cd esp8266_course
```

  Conecte o ESP8266, via usb, no seu computador.

  Tenha certeza que o dispositivo está em **modo flash**.

  Confira se seu computador reconheceu o dispositivo:
  
```
ls /dev/ | grep tty{porta_com}
```

  A porta COM padrão é `USB0`, i.e. `/dev/ttyUSB0`

> Não é commum mas as portas podem se alterar a cada nova conexão estabelecida.

  Dê permissões de leitura/escrita na porta:

```
sudo chmod 776 /dev/tty{porta_com}
```

  descobri no gerenciador de dispositivos do Windows, no caso na porta COM3 (O número da porta pode alterar por alguns motivos a cada nova conexão)
  Alterar a porta pode resolver os problemas de conexão 

  Crie uma virtualenv aqui 
```
  mkvirtualenv esp8266    #se estiver usando virtualenvwrapper
```

  Então instale a ferramenta esptool.py para upload e reset do firmware

```
pip install esptool
```

  Realize um teste para ler o `MAC ADDRESS` do dispositivo

```
esptool.py -p /dev/tty{porta_com} -b 115200 read_mac
```

  Caso o teste não seja bem sucedido, revise a porta utilizada e o procedimento de instalação

  Formate a FlashROM do dispositivo

```
esptool.py -p /dev/ttyS{porta_com} -b 115200 erase\_flash -> para limpar a flash
```

  Instale o firmware (demais imagens podem ser acessadas em: http://micropython.org/download#esp8266)
  
```
  esptool.py -p /dev/ttyS# -b 115200 write\_flash --flash\_size=detect -fm qio 0 bin/esp8266-20180718-v1.9.4-272-g46091b8a.bin
```

  conectar no REPL (interface com python) com o picocom
  picocom /dev/ttyS# -b115200 (tudo junto)

  criar outra virtualenv aqui (esp8266-mpfshell)
  ~  pip install rshell -> it's a interface terminal to access esp files ~
  https://github.com/wendlers/mpfshell mpfshell ao invés do rshell
  pip install -r requirements.txt
  alterar o pyserial para a versão 3.1 (pip install pyserial==3.1)
  pip install mpfshell


  mpfshell

  mpfshell> open ttyS#
  mpfshell> ls
  mpfshell> put file.py (upload file)
  mpfshell> get file.py (download file)

  *boot.py script executado no boot do esp (possui configurações iniciais da placa, principalmente sobre comunicação)

  *main.py script executado após o boot.py. Inicializa a árvore de execução do projeto


