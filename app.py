from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        datos = request.form
        vuelo = datos['no_vuelo']
        gi = datos['agente_gi']
        matricula = datos['matricula']
        capitan = datos['capitan']
        etd = datos['etd']
        puerta = datos['puerta']
        mx = int(datos['mx'])
        uk = int(datos['uk'])
        fm = int(datos['fm'])
        dip = int(datos['dip'])
        inf_mx = int(datos['inf_mx'])
        inf_ext = int(datos['inf_ext'])
        cnx_mx = int(datos['cnx_mx'])
        cnx_ext = int(datos['cnx_ext'])
        total = int(datos['total'])
        wch_llegada = int(datos['wch_llegada'])
        wch_salida = int(datos['wch_salida'])
        cobs = int(datos['cobs'])

        inf = inf_mx + inf_ext
        cnx = cnx_mx + cnx_ext
        uks_totales = mx + uk + fm + dip + inf + cnx
        uks_finales = total - uks_totales
        mexicanos = mx + inf_mx + cnx_mx
        extranjeros = total - mexicanos

        return render_template("reporte.html", vuelo=vuelo, gi=gi, matricula=matricula, capitan=capitan,
                               etd=etd, puerta=puerta, mx=mx, uk=uk, fm=fm, dip=dip,
                               inf_mx=inf_mx, inf_ext=inf_ext, cnx_mx=cnx_mx, cnx_ext=cnx_ext,
                               total=total, uks_finales=uks_finales, mexicanos=mexicanos,
                               extranjeros=extranjeros, wch_llegada=wch_llegada,
                               wch_salida=wch_salida, cobs=cobs)
    return render_template("formulario.html")
