# Projeto de Extensão - Aplic. de Cloud, Iot e Indústria 4.0 em Python.

## Objetivo
- Aplicação criada para um projeto de extensão da Faculdade UNESA (Universidade Estácio de Sá). O tema aborda a criação de uma aplicação que faz uso de algumas bibliotecas em Python para enviar documentos locais para um banco de dados PostgreSQL que está conectado a uma instância RDS na AWS através do Azure Data Studio. Quando os dados são enviados para a cloud, é administrada uma notificação via SNS Lambda para comunicar demais dispositivos IoT sobre a atualização do item anexado no banco de dados como exemplo.

- Observação: Este código, que tem a finalidade do projeto de extensão, teve como complemento inicial um outro projeto, que é este aqui: https://github.com/AntonielHUB/Analise_de_Dados_Fiscais_com_Python. Vale lembrar que este projeto, que se conecta à nuvem, funciona de forma independente daquele, mas acho importante ressaltar isso, pois abordei este fato durante a criação do projeto. Em particular, gostei bastante da objetividade dos dois projetos como um todo.

## Configuração
Nas fotos 1, 2, 3, 4 e 5, mostro sequencialmente os processos para criar uma instância RDS (Relational Database Service) na AWS que suporte PostgreSQL:
- Acesso o console da AWS e navego até o serviço RDS.
-	Clico em "Create database".
-	Escolho "Easy create" e seleciono "PostgreSQL" como o tipo de banco de dados.
-	Na etapa "Settings", defino o nome da instância identificadora como "Aplic-de-Cloud-Iot-e-Industria-4-em-Python".
-	Escolho a opção "Free tier" para garantir que a instância seja gratuita.
-	Configuro o master username como "estacio" e a senha como "estacio123".

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268612764113309746/1.png?ex=66ad0f34&is=66abbdb4&hm=faa2ac5dbfff3dec527cacb1a1dc74a7c1711c3e5ae63b47a718b6822505571f&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268613398136885381/2.png?ex=66ad0fcb&is=66abbe4b&hm=8bc28416a4fdb632a9365f77d17c3962ec7aca5ed67a7f5134895627751d8fd1&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268613545533378720/3.png?ex=66ad0fee&is=66abbe6e&hm=beb00ea059843e28d1f47bd611a78c3b122619d38e8ac7b940b1a2a36418b5e1&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268613688710140087/4.png?ex=66ad1011&is=66abbe91&hm=9359d136347f4d7143ed63983e762ae572d9ffed1fb7273c884d66179f4b0294&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268613783123656857/5.png?ex=66ad1027&is=66abbea7&hm=1ef24a05f39d37907efa6da97c09ed09b2cfff09fc60f244fe3b0115aea5eda9&" alt="Descrição da imagem">
</p>

Nas fotos 6 e 7, eu demonstro como configurar o acesso público. Na mesma página de criação da instância:
-	Rolo até a seção "Connectivity" e marco a opção "Publicly accessible".
-	Isso permitirá que a instância seja acessada publicamente.
  
<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268614243826270299/6.png?ex=66ad1095&is=66abbf15&hm=dbbdf8ee7dc2a7399950ee833e67ac11be1e3e12660684bcd1fe38ef340c5de9&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268614362583662654/7.png?ex=66ad10b1&is=66abbf31&hm=326d5389cf2ccb05dadd026071ced677322bf4ba79803bd521584883411821ae&" alt="Descrição da imagem">
</p>

Nas fotos 8 e 9, são demonstradas as configurações das regras do grupo de segurança. Ainda na seção "Connectivity":
•	Crio um novo grupo de segurança.
•	Para o grupo de segurança selecionado, adiciono uma regra que permita o tráfego de entrada de qualquer IP (0.0.0.0/0) na porta padrão do PostgreSQL (5432).
•	Isso garante que qualquer IP possa se conectar à sua instância PostgreSQL.

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268614700946428065/8.png?ex=66ad1102&is=66abbf82&hm=7175cef23ed042ce0d32d7170942d2626def440957bbe1992fab788931a39f95&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268614772379877426/9.png?ex=66ad1113&is=66abbf93&hm=282b6f0a7f504bee080461a1812e627f75993c825f252e05696f4d6d621c5da6&" alt="Descrição da imagem">
</p>

Nas fotos 10, 11 e 12, são demonstradas a instalação e configuração do Azure Data Studio para conectar-se ao banco de dados PostgreSQL criado na AWS, utilizando o Azure Data Studio.
-	Baixo e instalo o Azure Data Studio.
-	Após a instalação, abro o Azure Data Studio e instalo a extensão PostgreSQL através da visão "Extensions".
-	Com a extensão instalada, crio uma nova conexão com o banco de dados usando os detalhes da instância RDS criada anteriormente (endpoint, porta, nome de usuário e senha).

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268615101687009300/10.png?ex=66ad1161&is=66abbfe1&hm=8a165a51cb35e4d32f89ba29f2e8da2aaa6144cee833002ca562ff3689dc971c&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268615166287941762/11.png?ex=66ad1171&is=66abbff1&hm=e06fecfa0dd92b9496f05557ef5af6f7feea5f2d86ea24d34b1b069dc203945a&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268615231584604234/12.png?ex=66ad1180&is=66abc000&hm=cb236bc64907d1535f0cf5b42fc0bbcfcc85876b3cc8c19ffc06cd04cc739d1b&" alt="Descrição da imagem">
</p>

Dando sequência nas fotos 13, 14 e 15, demonstro como criar uma tabela no PostgreSQL após estabelecer a conexão com o banco de dados PostgreSQL na AWS através do Azure Data Studio.
Crio uma tabela chamada projeto_estacio_exemplo com duas colunas: id, um identificador único autoincrementado, e arquivo, que armazenará os arquivos como dados binários (BYTEA).

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268615617418756197/13.png?ex=66ad11dc&is=66abc05c&hm=a11923f6ac5045c523c3e33b64566dc9dd7eeadd69bd5e6add5f5935589150f8&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268615679821484216/14.png?ex=66ad11eb&is=66abc06b&hm=2316026012d03a474d81a81de3cee83615bae0a60fbf0dc7dceafb9c2336e735&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268615731688243330/15.png?ex=66ad11f8&is=66abc078&hm=1beb2fe968631256d3f7f30ce83b2c5b59c5f4c52384a9997782fbc7431aa224&" alt="Descrição da imagem">
</p>

E por fim, nas fotos 16, 17 e 18, são demonstradas as configurações do Amazon SNS.
- Observação: É neste ponto que entra o código do outro projeto que mencionei anteriormente, onde o "File_Path" é responsável por pegar os dados originados pelo projeto citado e conectá-los através do Azure Data Studio. Isso torna possível enviar os dados para o RDS na AWS utilizando o banco de dados PostgreSQL.

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268616286313775125/16.png?ex=66ad127c&is=66abc0fc&hm=5b968dbf6bad49770f4bc8c62d17719994f163003478afffae2d3606bf5ac3e3&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268616348251197550/17.png?ex=66ad128b&is=66abc10b&hm=b9a28dd4eae5f77480d52680173793df5aeec270766bdaf61360af4ed20980d7&" alt="Descrição da imagem">
</p>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1046815809227468832/1268616411488714908/18.png?ex=66ad129a&is=66abc11a&hm=cc6db786d798b85b47f8ce1babe257b3468c761251295e7837c9cf8144ac6f00&" alt="Descrição da imagem">
</p>
