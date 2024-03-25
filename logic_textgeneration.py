from transformers import pipeline, set_seed

class TextGenerate:

    def __init__(self) -> None:
        self.generator = pipeline('text-generation', model='gpt2')
        set_seed(42)

    def run(self, text):
        result = self.generator(text,
                              max_length=30,
                              num_return_sequences=5)

        return result[1]['generated_text']


# text = "Hello, I'm a language model,"
# result = translate(text)
# print(type(result))
# print(result)