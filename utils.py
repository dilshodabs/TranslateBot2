from googletrans import Translator, LANGCODES


tr = Translator()


async def translate_text(text: str, lang: str):
    # print(LANGCODES)на этом можно посмотреть языки uz, ru, и так далее
    return tr.translate(text, dest=lang).text
