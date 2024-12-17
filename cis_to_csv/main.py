import runpy

def main():
    archivo_original = "archivo.pdf"
    output = "output"
    args = [archivo_original, output]  # pasa solo los argumentos
    runpy.run_path('cis_converter.py', run_name="__main__", init_globals={'sys.argv': ['cis_converter.py'] + args})

if __name__ == "__main__":
    main()