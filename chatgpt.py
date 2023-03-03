import openai

openai.api_key = "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"

while True:

    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":

        break

    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=1000)

    print(completion.choices[0].text)
