import sqlite3
from getpass import getpass
import hashlib
import random

#Centrañ pregunta
def main():
    conn = sqlite3.connect('DaTa.db')
    Askb  = input('To create an account put "y", To start session "n" :  ')
    Ask =  Askb.lower()

    if Ask == "y":
        # Recompilacion de datos
        UsernameNew= input("Username : ")
        EmailNew = input("Email : ")
        print("Enter a password with 1 capital letter, 1 number and 4 characters minimum")
        PasswordNew = getpass("Pasword : ")
        #Contraseña seguridad Contar letras , Contar mayusculas ,verificar si hay un numero
        Mayus = False
        contadorLetras = len(PasswordNew)
        has_number = False
        for char in PasswordNew:
            if char.isupper():
                Mayus = True
                break
        for char in  PasswordNew:
            if char.isdigit():
                has_number = True
                break
        if contadorLetras > 4 and Mayus == True and  has_number == True and contadorLetras <= 10:
            random_salt = int(random.randint(1,5529528876326326))
            Salida_Obj = hashlib.sha256()
            Salida_Obj.update((PasswordNew+ str(random_salt)).encode('utf-8'))
            salida= Salida_Obj.hexdigest()
        else:
            print("Add more characters, or a capital letter")
        # Verificacion de  unicidad
        # Username
        cursor = conn.cursor()
        query = 'SELECT * FROM accounts WHERE Username = ?'
        cursor.execute(query,(UsernameNew,))
        result = cursor.fetchone()
        if result:
            print("The user name is exist")
        cursor.close()
        #Email
        cursor = conn.cursor()
        query2 = 'SELECT * FROM accounts WHERE Email = ?'
        cursor.execute(query2,(EmailNew,))
        result2 = cursor.fetchone()
        if result2:
            print("The email is exist")
        cursor.close()

        # Aumento de datos ala base de datos
        cursor = conn.cursor()
        query='INSERT INTO accounts (Username,Email,Password,Salt) VALUES (?,?,?,?)'
        cursor.execute(query,(UsernameNew,EmailNew,salida,random_salt))
        conn.commit()
        cursor.close()
        conn.close()
        ###########################################
        ###########################################
    elif Ask == "n":
        CorreoIS= input("Enter your email ")
        PasswordIS=getpass("Enter your password ")

        EmailCoM= False
        PassCoM= False
        #comprobacion de email
        conn = sqlite3.connect("DaTa.db")
        cursor= conn.cursor()

        query11 = "SELECT Email FROM accounts WHERE Email=?"
        cursor.execute(query11,(CorreoIS,))
        result = cursor.fetchone()

        if result:
            EmailCoM = True
        else:
            print("The email is wrong")
        cursor.close()
        #Comprobacion de contraseña
        conn= sqlite3.connect("DaTa.db")
        if EmailCoM == True:
            cursor = conn.cursor()
            query12 = "SELECT Salt FROM accounts WHERE Email = ?"
            cursor.execute(query12,(CorreoIS,))

            salt2 = cursor.fetchone()[0]
            Salida_Obj2 = hashlib.sha256()
            Salida_Obj2.update((PasswordIS+ str(salt2)).encode('utf-8'))
            salida2= Salida_Obj2.hexdigest()
            cursor.close()
            # pedir contraseña a base de datos
            cursor = conn.cursor()
            query13 = "SELECT Password FROM accounts WHERE  Email =  ?"
            cursor.execute(query13,(CorreoIS,))
            result3 = cursor.fetchone()
            cursor.close()
            #salida2 contraseña con hash  y salt inisio de sesion
            if salida2 == result3[0]:
                cursor =  conn.cursor()
                queryFinal = "SELECT Username FROM accounts WHERE Email = ?"
                cursor.execute(queryFinal,(CorreoIS,))
                resultFin = cursor.fetchone()
                cursor.close()
                #Transformar la  tupla a un string
                def TuplaAstr(a):
                    return ' '.join(map(str,a))
                UsernameClean =TuplaAstr(resultFin)
                print("Welcome!!  " + UsernameClean)

        conn.close()

if __name__ == "__main__":
    main()
