# comics-to-pdf

Converts a nested folder of images to a collection of PDFs.

For example, a folder like this:

```shell
comics/
└── My Comic
    ├── 0001 - Prologue
    │   ├── 001.webp
    │   ├── 002.webp
    │   ├── 003.webp
    │   └── 004.webp
    └──── 0002 - Episode 1
        ├── 001.webp
        ├── 002.webp
        ├── 003.webp
        └── 004.webp
```

will be converted into PDFs like this:

```shell
pdf/
└── My Comic
    ├── 0001 - Prologue.pdf
    └── 0002 - Episode 1.pdf
```

by this command:

```shell
python convert_images_to_pdf.py "comics/My Comic"
```

## Lezhin

To back up comics from Lezhin.com: first, use https://github.com/ImSejin/lezhin-comics-downloader to download a comic.
Then run this script with the path to the comic folder, e.g.:

    python convert_images_to_pdf.py "L_Comic Title - Creator"

The PDFs will be created in a folder "pdf/L_Comic Title - Creator" alongside this
script's location.
