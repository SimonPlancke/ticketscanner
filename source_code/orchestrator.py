# https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
# https://pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/
# https://pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/

from image_reader import ImageReader

def run_program():
    # Step 1: Build a model that can scan the contents from a ticket and turn them into a text file
    image = ImageReader("images\\test_image_2.jpg")
    print(image.file_name)
    image.load_image()
    # # Step 2: Classify the contents from the text file into product types

    # Step 3: Store your data and produce an overview of your expenses 

if __name__ == '__main__':
    run_program()