import socket, ssl, json, time
import mytokens

HOST  = "api.telegram.org"
PORT  = 443

def conn_to(host, port):
    #lobal sock_tcp

    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.connect((host, port))

    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose)
    return context.wrap_socket(sock_tcp, server_hostname=HOST)


SERVICES = { "gemini"   : { "model" : "gemini-2.5-flash",  # ou gemini-1.5-pro, etc.
                            "host": "generativelanguage.googleapis.com",
                            "endpoint" : "/v1beta/openai/chat/completions",
                            "token": mytokens.GEMINI_TOKEN  },
             "deepseek" : { "model" : "deepseek-chat",  # ou "deepseek-coder" se preferir 
                            "host" : "api.deepseek.com", 
                            "endpoint" : "/v1/chat/completions",
                            "token": mytokens.DEEPSEEK_TOKEN  },
             "openai"   : { "gpt-3.5-turbo"   # Ou "gpt-4", "gpt-4o", etc.
                            "host" : "api.openai.com",
                            "endpoint" : "/v1/chat/completions",
                            "token": mytokens.OPENAI_TOKEN  }
   }

headers = {
    "Authorization": "",
    "Content-Type": "application/json"
   }

payload =  {   "model" : "", 
               "messages"   : [ 
                  {"role": "system", "content": "Você é um assistente."},
                  {"role": "user", "content": ""} ],
               "temperature": 0.7,
               "max_tokens" : 10000
   }

def set_model (service):
   payload ["model"] = SERVICES[service]["model"]
   headers ["Authorization"] = f'Bearer {SERVICES[service]["token"]}'
   
def set_prompt (prompt):
   payload["messages"][1]["content"] = prompt
    
def extrair_resultado (data):
   try: 
      response = data["choices"][0]["message"]["content"].strip()
   except Exception as e:
      print ("Erro na resposta do modelo ", e)
      response = ""
   
   return response


def send_get (sock_tcp, resource, headers):
    
    sock_tcp.send("GET "+resource+" HTTP/1.1\r\n"+
                    headers+
                    "\r\n").encode("utf-8")

def send_post (sock_tcp, resource, headers, body): 
    body = body.encode("utf-8")
    sock_tcp.send (("POST "+resource+" HTTP/1.1\r\n"+
                   "Content-Length: "+str(len(body))+"\r\n"+headers+
                   "\r\n").encode("utf-8"))
    sock_tcp.send(body)

    print(body)
         

def select_service():
   for id, service in enumerate(SERVICES):
      print (f"{id+1} - {service}")

   try:
      service = SERVICES.items()[int(input("Selecione um serviço: "))-1][1]
   except:
      service = 'gemini'
   
   return service

def perguntar(service, strPrompt: str) -> str:
   
      set_prompt (strPrompt)
      
      reqEnvio = send_post("https://api.telegram.org/bot8309699898:AAHTezRjFzK7PPr1I7Hc81H9RqR099KlsEg/sendMessage"+ 
                               SERVICES[service]["host"]+
                               SERVICES[service]["endpoint"], 
                               headers=headers, json=payload)
      reqEnvio.raise_for_status()
      data = reqEnvio.json()
      return extrair_resultado(data)
  
    
def get_response(sock_tcp):
    answer = sock_tcp.recv(4096)
    header_body = answer.split(b"\r\n\r\n")
    headers, body = header_body[0].decode().split("\r\n"), header_body[1]

    print(answer)

    status_line = headers[0]
    if status_line.split()[1] == "200":
        for header in headers[1:]:
            field_value = header.split(":")
            if field_value[0] == "Content-Length":
                to_read = int (field_value[1])
                break
    
        to_read -= len(body)
        while to_read > 0:
            segment = sock_tcp.recv(4096)
            body += segment
            to_read -= len(segment)


def answer_update(update):
    sock_tcp = conn_to(HOST, PORT)
    chat_id  = update["message"]["chat"]["id"]

    answer = input ("Sua resposta: ")
    body = '{"chat_id":'+str(chat_id)+', "text":"'+answer+'"}'
    print(answer)
    
    cmd = "/sendMessage"
    resource = "/bot"+mytokens.TELEGRAM_TOKEN+cmd
    headers = ("Content-Type: application/json\r\n"+
               "Host: "+HOST+"\r\n")
    send_post(sock_tcp, resource, headers, body)
    get_response(sock_tcp)
    sock_tcp.close()
   
    return update["update_id"]
# ----------------------------------------------------------------------

def main():
   service = select_service()
   set_model(service)
   
   while True:
      str_texto = input("\nDigite sua pergunta (SAIR - Encerra): ").lower()
      if str_texto == "sair":
         print("\nSaindo do Programa...")
         break

      str_resposta = perguntar(service, str_texto)
      print(f"\nResposta:\n{str_resposta}")

# ----------------------------------------------------------------------
if __name__ == "__main__":
   main()