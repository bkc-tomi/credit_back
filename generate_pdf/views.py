from datetime import date
import json

from django.shortcuts import render
from django.urls      import reverse
from django.http      import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.db        import transaction

# PDF作成
from django.template.loader import get_template
from weasyprint             import HTML, CSS

def index(request):
    """
    ===========================================================================
    **履歴書生成**
    ===========================================================================
    """
    err_msg = ''
    try:
        # データ取得 ================================================
        # jsonデータを取得
        datas = json.loads(request.body)
        # データ整形 ================================================

        # テンプレート作成 ===========================================
        # 取得
        html_template = get_template('generate_pdf/resume.html')
        print_date = date.today()
        # コンテキスト埋め込み
        html_str = html_template.render({
            'basicInfo': datas['basicInfo'],
            'educationHistory': datas['educationHistory'],
            'workHistory': datas['workHistory'],
            'license': datas['license'],
            'hobby': datas['hobby'],
            'motivation': datas['motivation'],
            'print_date': print_date,
        }, request)

        # PDF作成 ===================================================
        pdf_file = HTML(string=html_str, base_url=request.build_absolute_uri()).write_pdf()

        # ページ遷移 =================================================
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Access-Control-Allow-Headers'] = 'Content-Type, Accept'
        response['Access-Control-Allow-Methods'] = 'POST'
        return response

    # エラー処理 =====================================================
    except Exception as err:
        print(err)
        response = HttpResponse(err)
        return response
        