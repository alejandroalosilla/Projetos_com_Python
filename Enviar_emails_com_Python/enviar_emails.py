import smtplib
import email.message


def enviar_email():
    # Local onde a mensagem será escrita (podem ser utilizadas as tags de HTML):
    corpo_email = """
    <p>Apenas um exemplo de mensagem...</p>
    <p>Apenas rodando o projeto <b>"Enviando email com Python"</b>!</p>
    <p>Att <i>Alejandro Alosilla</i></p>
    """

    msg = email.message.Message()
    # O assunto abordado (*substitua*)
    msg['Subject'] = "Título"
    # Remetente ( seu email)(*substitua*): 
    msg['From'] = 'Seu email'
    # Destinatário para onde vai o email(*substitua*):
    msg['To'] = 'Email do destinatário'
    
    # Senha descartável que pode ser gerada na sua conta do gmail na aba "Senhas de App" (Apenas pesquisar por "Senhas de App" nas suas configurações de conta):
    # Exemplo de senha gerada -> hxnhegofnkkwlkmo
    # (*Subistitua*)
    password = 'Senha descartável criada no gmail (Senhas de App)'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Credenciais de login para enviar o e-mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

# Agora é só chamar a função e pronto...
enviar_email()
