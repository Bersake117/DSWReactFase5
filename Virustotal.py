import time
import requests
import pandas as pd

# Tu API Key configurada
API_KEY = "3985fd7d0388b26dec65171489d03d953910fc40d49bff0f73fae84fd67033cb"

# Lista completa de 179 IoCs
iocs = [
    "104.243.43.115", "108.61.0.122", "109.207.200.42", "128.14.95.210", 
    "13.40.84.221", "135.148.150.100", "139.45.197.227", "139.45.197.228", 
    "139.45.197.252", "139.45.197.253", "139.45.197.254", "142.250.180.142", 
    "142.91.159.227", "147.79.120.254", "152.70.209.71", "162.251.116.106", 
    "163.172.84.84", "172.253.122.104", "172.67.196.80", "181.69.208.203", 
    "18.231.61.122", "185.109.91.126", "185.241.208.172", "186.1.190.51", 
    "198.50.191.95", "199.91.155.15", "224.0.0.251", "224.0.0.252", 
    "239.255.255.250", "38.154.239.250", "4pjoxehw.com", "51.222.105.83", 
    "51.79.21.62", "61.167.119.195", "64.233.167.84", "66ckgyq4hs4stfrr53mrbnjpe.com", 
    "69.167.10.104", "74.50.84.181", "8.243.161.13", "89.58.54.129", 
    "92.112.198.26", "93.185.99.205", "94.23.76.52", "9.9.9.9", 
    "acorturl.com", "aeneasclosure.website", "agora.io", "aluve.rdgqkfxio.com", 
    "amgglobal.ca", "animezeno.sbs", "api.buzarr.com", "api.hapi.trade", 
    "app.abctvbv222.com", "armenia2024.duckdns.org", "backend.svcenter.xyz", 
    "banamyi.vb1kivdlvc.com", "benchsuited.com", "bissonprevoid.website", 
    "biterstraiky.life", "brutico2025aprende.kozow.com", "bstgms4y.com", 
    "buried.av380.net", "cellaragog.top", "chho1ilgf.xyz", "click.onedigitsolutions.com", 
    "cohawaut.com", "cojudgeasbolan.top", "compasswhitest.top", "content.dft-cdn42.net", 
    "coogoanu.net", "cukuyx.lig1cfhw.xyz", "cv.refeelparolee.top", "cyxruzen.08193kadf.xyz", 
    "cyxruzen.chho1ilgf.xyz", "dashnet.actmobile.com", "delivery---1000.cdn-stack.com", 
    "dns.quad9.net", "dt244.kokiuyar.xyz", "eaudigonal.top", "emisorasenvivo.com.co", 
    "ewr1.vultrobjects.com", "famdamnlyman.one", "fedapush.net", "ferrelkines.top", 
    "fondlescany.top", "freeconvert.com", "frothirenews.top", "fs20.uploadrar.com", 
    "futbollibreonline.com", "futbollibreonline.org", "galeateflagged.guru", 
    "galepush.net", "gd34fdldh.xyz", "gfg.xgw3sdzoac.com", "go1.monetizemyapp.net", 
    "grindhousekodi.tk", "guigebichir.website", "gummersleban.top", "hamfatbuxeous.guru", 
    "haolebenshi.cyou", "hfcx.hqfemoapw.com", "imps.rollads.live", "isospinsubsets.top", 
    "jagnoans.com", "jmhgeyc.3h8hnjfbf.com", "kali.vdopanel.com", "kamtridit.cz", 
    "kaurisunsawn.top", "lecapush.net", "list-manage.agle1.cc", "loogreem.xyz", 
    "makeupschaise.life", "masiv3.s3.amazonaws.com", "me3x.online", "mediafire.com", 
    "medimnbream.top", "mega.co.nz", "monetizemyapp.net", "neozadhow.top", 
    "nmbde.ornmwqyup.com", "noshwsmkm.com", "nts.embluemail.com", "nunletevulge.top", 
    "om.chancarosied.top", "omnatuor.com", "outsiftfictor.top", "pelota-libre.com.co", 
    "pepepush.net", "perficut.at", "perr.hola.org", "perr.kbz0pwvxmv.com", 
    "pokerlive-production-gameserver-http.casualpluspoker.com", "pool-nyc.supportxmr.com", 
    "ptccloud.lsdwedsfsc.site", "qx5norivem.qx5norivem.shop", "ramrodsmorals.top", 
    "rapepush.net", "re-captha-version-2-13.top", "regearlophiid.top", "reseizeunrainy.top", 
    "rm8zcvk3.fubohd.com", "rnfb.dwjfbxuac.com", "rojadirecta.org.pe", "rt.cdnmedia.tv", 
    "rtsyx.higgsyx.com", "s0-gr3at3.com", "s162-isny.freeconvert.com", "satinayapii.top", 
    "seko.vipers.pw", "serviconimonitoreo.ddns.net", "srvidores132.dynuddns.com", 
    "sucursaldinamicadministrativo.ru", "superteg.co", "taxismaned.top", "tbmdcnd.xyz", 
    "ticehikers.top", "ti.meliarokey.top", "treitrehagdin.top", "trololopush2023push.com", 
    "tv.purdahpapern.top", "tv.soccerplus.link", "ultimatebonus.life", "upburstunfence.guru", 
    "update.filesupdating.com", "update.itopupdate.com", "*ursaldinamicadministrativo.ru", 
    "utorrent.com", "vddgcoud02.gd34fdldh.xyz", "vdgloall01.hhf123dcd.com", "viewyentreat.guru", 
    "weagc.dhbgjv37e.com", "www.6hqydemrhfe2izbx.com", "www.ingeniolacabana.com", 
    "www.lr7pxmz6w4ta.com", "www.rojadirectatv3.pl", "www.tax-individual.com.co", 
    "www.xoz6rhd.com", "xy123my.xervcwfsk.com", "zabanit.xyz"
]

resultados = []
headers = {"x-apikey": API_KEY}

def es_ip(item):
    return item.replace(".", "").isdigit()

print(f"Iniciando análisis de {len(iocs)} IoCs...")
print("NOTA: Este proceso tomará aproximadamente 45 minutos debido al límite de 4 peticiones por minuto de la API gratuita.\n")

for idx, ioc in enumerate(iocs, 1):
    # Limpiar el IoC de esquemas HTTP/HTTPS y asteriscos inválidos
    ioc_limpio = ioc.replace("://", "").replace("http://", "").replace("https://", "").replace("*", "").strip()
    
    # Si el IoC queda vacío tras limpiar (por error en la lista), saltarlo
    if not ioc_limpio:
        continue

    tipo = "ip_addresses" if es_ip(ioc_limpio) else "domains"
    url = f"https://www.virustotal.com/api/v3/{tipo}/{ioc_limpio}"

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get("data", {})
            attributes = data.get("attributes", {})
            stats = attributes.get("last_analysis_stats", {})
            results = attributes.get("last_analysis_results", {})

            maliciosos = stats.get("malicious", 0)
            sospechosos = stats.get("suspicious", 0)
            total_detectan = maliciosos + sospechosos
            total_motores = sum(stats.values())

            if total_detectan > 0:
                detecciones_set = set()
                vendors = []

                for motor, res in results.items():
                    categoria = res.get("category")
                    if categoria in ["malicious", "suspicious"]:
                        vendors.append(motor)
                        resultado_txt = res.get("result")
                        if resultado_txt:
                            detecciones_set.add(resultado_txt.capitalize())

                det_str = ", ".join(list(detecciones_set))
                ven_str = ", ".join(vendors)
                
                texto_reporte = f"{total_detectan}/{total_motores} motores lo detectan. Detecciones observadas: {det_str}. Vendors visibles: {ven_str}."
            else:
                texto_reporte = f"0/{total_motores} motores lo detectan. No se observaron detecciones maliciosas."

        elif response.status_code == 404:
            texto_reporte = "No encontrado en la base de datos de VirusTotal."
        elif response.status_code == 401:
            texto_reporte = "Error: API Key inválida o sin permisos."
        elif response.status_code == 429:
            texto_reporte = "Error: Límite de cuota de la API excedido. Aumenta el tiempo de espera (time.sleep)."
        else:
            texto_reporte = f"Error en consulta (Código {response.status_code})."

    except Exception as e:
        texto_reporte = f"Error de conexión: {str(e)}"

    resultados.append({
        "IOC": ioc_limpio,
        "Reporte": texto_reporte
    })

    print(f"[{idx}/{len(iocs)}] Escaneado: {ioc_limpio} -> {texto_reporte[:50]}...")
    
    # Pausa de 15.5 segundos para asegurar que no se rebase el límite de 4 por minuto (60s / 4 = 15s)
    time.sleep(15.5)

# Generar DataFrame
df = pd.DataFrame(resultados)

# Imprimir la tabla en la terminal
print("\n--- RESULTADO DEL ANÁLISIS ---")
print(df.to_markdown(index=False, tablefmt="grid"))

# Exportar a Excel
df.to_excel("Reporte_VT_Formateado.xlsx", index=False)
print("\nEl análisis ha finalizado. Se ha generado el archivo 'Reporte_VT_Formateado.xlsx'.")
