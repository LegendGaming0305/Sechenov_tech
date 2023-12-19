from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.pagesizes import  A4
import json


async def counting_results(information: dict):
    info = json.loads(information)
    ndi = sum(info.get(key, 0) for key in ['neckpainintensity', 'selfcare', 'lifting', 
                                           'reading', 'headache', 'attention', 'workability', 
                                           'driving', 'sleep', 'leisure'])
    dn4 = sum(info.get(key, 0) for key in ['burning-sensation', 'painful-cold-sensation', 'electric-shock-sensation',
                                           'tingling-crawling-sensation', 'tingling-sensation', 'numbness-sensation',
                                           'itching-sensation', 'reduced-touch-sensitivity', 'reduced-tingling-sensitivity',
                                           'brushing-sensation'])
    keele = sum(info.get(key, 0) for key in ['pain-last-2-weeks', 'pain-limiting-walking', 'pain-affecting-dressing',
                                             'chronic-diseases', 'pain-affecting-movement', 'thoughts-about-danger',
                                             'pain-duration-belief', 'pain-affecting-enjoyment', 'pain-bother-level'])
    hads_alarm = sum(info.get(key, 0) for key in ['tension-discomfort-feeling', 'fear-of-something-horribles',
                                                  'restless-thoughts', 'ease-of-sitting-and-relaxing',
                                                  'internal-tension-or-trembling', 'restlessness-constant-need-to-move',
                                                  'sudden-panic'])
    hads_depression = sum(info.get(key, 0) for key in ['pleasure-maintained', 'ability-to-laugh', 'feeling-energetic',
                                                       'perception-of-slowing-down', 'attention-to-appearance',
                                                       'satisfaction-from-activities', 'pleasure-from-entertainment'])
    
    result = [ndi, dn4, keele, hads_alarm, hads_depression]
    await creating_pdfs(marks=result)

def ndi_counting(ndi: int) -> str:
    if ndi >= 0 and ndi <= 4:
        return "нет ограничения жизнедеятельности"
    elif ndi >= 5 and ndi <= 14:
        return "ограничение легкое"
    elif ndi >= 15 and ndi <= 24:
        return "умеренное ограничение"
    elif ndi >= 25 and ndi <= 34:
        return "сильное ограничение"
    elif ndi > 35:
        return "полное ограничение"
    
def dn4_counting(dn4: int) -> str:
    if dn4 >= 4:
        return "указывает на нейропатический компонент боли"
    else:
        return "указывает, что у вас нет существенной боли"

def keele_counting(keele: int) -> str:
    if keele <= 3:
        return "низкий риск хронизации"
    elif 4 <= keele <= 7:
        return "средний риск хронизации"
    else:
        return "высокий риск хронизации"
    
def hads_alarm_counting(hads_alarm: int) -> str:
    if hads_alarm <= 7:
        return "отсутствуют достоверно выраженные симптомы тревоги"
    elif 8 <= hads_alarm <= 10:
        return "субклинически выраженная тревога"
    else:
        return "клинически выраженная тревога"
    
def hads_depression_counting(hads_depression: int) -> str:
    if hads_depression <= 7:
        return "отсутствуют достоверно выраженные симптомы депрессии"
    elif 8 <= hads_depression <= 10:
        return "субклинически выраженная депрессия"
    else:
        return "клинически выраженная депрессия"

async def creating_pdfs(marks: list):
    ndi, dn4, keele, hads_alarm, hads_depression = marks
    result_ndi = ndi_counting(ndi)
    result_dn4 = dn4_counting(dn4)
    result_keele = keele_counting(keele)
    result_hads_alarm = hads_alarm_counting(hads_alarm)
    result_hads_depression = hads_depression_counting(hads_depression)
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    my_Style=ParagraphStyle('My Para style',
        fontName='DejaVuSerif',
        backColor='#F1F1F1',
        fontSize=16,
        borderColor='#FFFF00',
        borderWidth=2,
        borderPadding=(20,20,20),
        leading=20,
        alignment=0
        )
    width, height = A4
    pdf = canvas.Canvas('results.pdf', pagesize=A4)
    text_lines = Paragraph(f'''По шкале NDI вы набрали <b>{ndi}</b> балла/баллов.<BR/>
            Интерпретация результатов:<BR/>
            У вас {result_ndi}.<BR/>
            <BR/>
            По шкале DN4 вы набрали {dn4} балла/баллов.<BR/>
            Интерпретация результатов:<BR/>
            Тестирование {result_dn4}.<BR/>
            <BR/>
            По шкале TheKeeleSTarT MSK Tool вы набрали {keele} балла/баллов.<BR/>
            Интерпретация результатов:<BR/>
            У вас по результатам тестирования может наблюдаться {result_keele}.<BR/>
            <BR/>
            По шкале <b>HADS</b> вы набрали {hads_alarm} балла/баллов по части тревоги и {hads_depression} балла/баллов по части депресии<BR/>
            Интерпретация результатов:<BR/>
            Можно сделать вывод о том что у вас {result_hads_alarm}.<BR/>
            А также {result_hads_depression}''', my_Style)
    text_lines.wrapOn(pdf, 400, 100)
    text_lines.drawOn(pdf, width - 500, height - 600)
    pdf.save()