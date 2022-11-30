import os
import streamlit as st
import openai
openai.api_key = os.environ['OPENAI_KEY']

st.header("Gerador de respostas de avaliações de restaurantes, baseado na GPT-3")
review = st.text_area("Entre com a avaliação do cliente")
button = st.button("Gerar resposta")

def generate_reply(review):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Escreva uma resposta para a seguinte avaliação.\n\nAvaliação: {review}\n\nResposta:",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response.choices[0].text

if button and review:
  with st.spinner("Gerando resposta..."):
    reply = generate_reply(review)
  st.write(reply)