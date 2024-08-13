import win32cred
import sys

def get_single_credential(target):
    try:
        cred = win32cred.CredRead(target, win32cred.CRED_TYPE_GENERIC, 0)
        username = cred['UserName']
        password = cred['CredentialBlob']
        return username, password
    except Exception as e:
        print(f"No se pudo obtener la credencial: {e}")
        return None

def Credenciales_buk():
    target_name = "CORREO_BUK_COL"
    credential = get_single_credential(target_name)

    if credential:
        username, password = credential
        print(f"{username}", f"{password.decode('utf-16-le')}")

def Credenciales_pagina():
    target_name = "BUK_IBR_COL"
    credential = get_single_credential(target_name)

    if credential:
        username, password = credential
        print(f"{username}", f"{password.decode('utf-16-le')}")



def main():
    opcion = sys.argv[1]
    
    if opcion == "Credenciales_buk":
        Credenciales_buk()
    elif opcion == "Credenciales_pagina":
        Credenciales_pagina()

if __name__ == "__main__":
    main()
