import js2py, requests, json, sys
if len(sys.argv) < 2 :
    print("error")
    exit()
dd = {"ry":"ja", "en":"en","zh":"zh-CN"}
old = sys.argv[1]
if len(sys.argv) == 3:
    to = dd.get(sys.argv[-1])
    if not to:
        to = "en"
else:
    to = "en"

context = js2py.EvalJs()
TKK = "432973.3594529252"

js = r'''var b = function (a, b) {
    for (var d = 0; d < b.length - 2; d += 3) {
        var c = b.charAt(d + 2),
            c = "a" <= c ? c.charCodeAt(0) - 87 : Number(c),
            c = "+" == b.charAt(d + 1) ? a >>> c : a << c;
        a = "+" == b.charAt(d) ? a + c & 4294967295 : a ^ c
    }
    return a
}

var tk =  function (a,TKK) {
    for (var e = TKK.split("."), h = Number(e[0]) || 0, g = [], d = 0, f = 0; f < a.length; f++) {
        var c = a.charCodeAt(f);
        128 > c ? g[d++] = c : (2048 > c ? g[d++] = c >> 6 | 192 : (55296 == (c & 64512) && f + 1 < a.length && 56320 == (a.charCodeAt(f + 1) & 64512) ? (c = 65536 + ((c & 1023) << 10) + (a.charCodeAt(++f) & 1023), g[d++] = c >> 18 | 240, g[d++] = c >> 12 & 63 | 128) : g[d++] = c >> 12 | 224, g[d++] = c >> 6 & 63 | 128), g[d++] = c & 63 | 128)
    }
    a = h;
    for (d = 0; d < g.length; d++) a += g[d], a = b(a, "+-a^+6");
    a = b(a, "+-3^+b+-f");
    a ^= Number(e[1]) || 0;
    0 > a && (a = (a & 2147483647) + 2147483648);
    a %= 1E6;
    return a.toString() + "." + (a ^ h)
}'''

context.execute(js)
tk = context.tk(old, TKK)
print(tk)

headers = {
"Cookie": "_ga=GA1.3.1235249873.1558506152; NID=184=vV90J2I5e4-ZUE8gFZ6Ypw4zUygKptEcfgsr49eHKT4TALIVDfV3I4hO7dSgyY36-XgzZZY3JnDLd5tKYT_VE_nYspbmMoRb7rcti3woHNrEkiySpiK-3yvdhGYVUqs1IsHQXyvBp-Y61e6t8s6IY_0fMAlmArX-V5IDLoEvI8s; _gid=GA1.3.1332929399.1558620938; 1P_JAR=2019-5-24-13; _gat=1","User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"}

params = {
"client": "webapp",
"sl": "auto",
"tl": to,
"hl": "zh-CN",
"dt": "at",
"dt": "bd",
"dt": "ex",
"dt": "ld",
"dt": "md",
"dt": "qca",
"dt": "rw",
"dt": "rm",
"dt": "ss",
"dt": "t",
'source': "bh",
"ssel": 0,
"tsel": 0,
"kc": 1,
"tk": tk,
"q": old
}

response = requests.get("https://translate.google.cn/translate_a/single", headers=headers, params=params)

ret = response.content.decode()
print(json.loads(ret)[0][0][0])



