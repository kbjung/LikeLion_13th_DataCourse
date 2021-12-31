from googletrans import Translator

translator = Translator()

# sentence = "안녕하세요"
sentence = input("번역을 원하는 문장을 입력하세요 : ")
dest = input("어떤 언어로 번역을 원하는지 입력하세요 : ")

result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

# print(result) 결과 : Translated(src=ko, dest=en, text=Hello, pronunciation=None, extra_data="{'confiden...")
# print(detected) 결과 : Detected(lang=ko, confidence=None)

print("============== 출 력 결 과 ==============")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("========================================")