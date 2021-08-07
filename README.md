         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 

Geração da Chave SSH

-Cria a chave
ssh-keygen -t rsa

-Gera valor da Chave
cat ~/.ssh/id_rsa.pub

-Cria Ambiente Virtual Python
python3 -m venv ~/.venv
source ~/venv/bin/activate

-Executa Código
python <nomeArquivo>.py