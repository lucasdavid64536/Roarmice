import time
import os

def main():
    data = os.system("Source.py")
    if data == 1:
        print "[ERROR] Erro nas portas, Reiniciando servidor em 10 Segundos"
        time.sleep(10)
        os.system("cls")
        main()
    elif data in [5,1280]:
        print "[INFO] Servidor desligado!"
        raw_input("")
    elif data in [11,2816]:
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 10 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 9 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 8 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 7 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 6 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 5 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 4 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 3 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 2 segundos"
        time.sleep(1)
        print "[ERROR] Erro nas Portas server. Reiniciar servidor em 1 segundo"
        time.sleep(1)
        os.system("cls")
        main()
    else:
        print "[ERROR] Server Caiu, Reiniciar servidor 20 segundos"
        time.sleep(20)
        os.system("cls")
        main()

if __name__=="__main__":
    main()
