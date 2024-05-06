# -*- coding: utf-8 -*

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Preformatted, Image, Spacer
from reportlab.lib import utils


def create_PDF(text, map, table):
    # Создаем PDF-документ
    pdf_filename = "output.pdf"
    pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Устанавливаем кодировку UTF-8
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont

    pdfmetrics.registerFont(TTFont("OpenSans", "parsers\PDFCreators\OpenSans.ttf"))

    # Устанавливаем шрифт и кодировку для стиля
    style = ParagraphStyle(
        "Normal", fontName="OpenSans", fontSize=12, spaceAfter=12, leading=16
    )

    # Загружаем натальную карту
    img1 = utils.ImageReader("C:\\Users\\user\\umk\\map.png")
    img_width, img_height = img1.getSize()

    # Создаем Image и указываем размеры
    image1 = Image("C:\\Users\\user\\umk\\map.png", width=img_width, height=img_height)

    # Загружаем натальную таблицу
    img2 = utils.ImageReader("C:\\Users\\user\\umk\\table.png")
    img_width, img_height = img2.getSize()

    # Создаем Image и указываем размеры
    image2 = Image(
        "C:\\Users\\user\\umk\\table.png", width=img_width, height=img_height
    )
    # Создаем пустой абзац
    empty_paragraph = Preformatted("", style)

    # Создаем Paragraph с вашим длинным текстом
    paragraph = Preformatted(text, style, maxLineLength=70)

    # Собираем элементы для добавления в PDF
    elements = [
        image1,
        image2,
        empty_paragraph,
        empty_paragraph,
        paragraph,
    ]

    # Строим PDF-документ
    pdf.build(elements)
