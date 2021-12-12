from oop_parse_sin import *


def parse():
    x = str(input("Enter:"))

    Obj_sinoptik = get_html_s(x)
    s_sinoptik = Obj_sinoptik.poiskpres_sinoptik()

    Obj_pogoda = get_html_p(x)
    s_pogoda = Obj_pogoda.poiskpres_pogoda()

    html_sinoptik = Obj_sinoptik.g_html_sinoptik(s_sinoptik)
    print(html_sinoptik)
    html_pogoda = Obj_pogoda.g_html_pogoda(s_pogoda)
    print(html_pogoda)

    if html_sinoptik.status_code == 200:
        Obj_sin_proc = show_content_sin(html_sinoptik.text, x)
        Obj_sin_proc.find_elem()
        Obj_sin_proc.show()

    if html_pogoda.status_code == 200:
        Obj_pog_proc = show_content_pog(html_pogoda.text, x)
        Obj_pog_proc.find_elem()
        Obj_pog_proc.show()
    else:
        print("\nError")


parse()
