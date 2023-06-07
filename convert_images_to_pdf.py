import gc
import os
import sys

from PIL import Image


def convert_images_to_pdf(book_path):
    chapter_list = sorted(os.listdir(book_path))
    pdf_dir = os.path.join("pdf", book_path)

    if not os.path.isdir(pdf_dir):
        os.makedirs(pdf_dir)

    for i in range(len(chapter_list)):
        print(chapter_list[i])

        # https://stackoverflow.com/a/47283224
        images = [
            Image.open(os.path.join(os.path.join(book_path, chapter_list[i]), f))
            for f in sorted(os.listdir(os.path.join(book_path, chapter_list[i])))
        ]
        pdf_path = os.path.join(pdf_dir, chapter_list[i] + ".pdf")
        images[0].save(
            pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
        )

        # Clear up Image objects that eat up a lot of memory
        gc.collect()


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "help":
        print(
            """
Converts a downloaded Lezhin comic from folders of images to a collection of PDFs,
one PDF per episode.

First, use https://github.com/ImSejin/lezhin-comics-downloader to download a comic.
Then run this script with the path to the comic folder, e.g.:

    python convert_images_to_pdf.py "L_Comic Title - Creator"
    
The PDFs will be created in a folder "pdf/L_Comic Title - Creator" alongside this
script's location.
"""
        )
        sys.exit()

    if not os.path.isdir(sys.argv[1]):
        print("Can't find a folder at {}, try again?".format(sys.argv[1]))
        sys.exit()

    convert_images_to_pdf(sys.argv[1])

    print("Finished!")
    sys.exit()
