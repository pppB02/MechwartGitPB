from TextToImageModule import TextToImage

def main():
    text = input("Text: ")
    concerter = TextToImage()

    binary_str = concerter.text_to_binary(text)
    print(binary_str)
    convert.create_image(concerter.image_datas(binary_string,0))
    