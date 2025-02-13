#Antes de executar esse código, é necessário instalar as seguintes bibliotecas via pip:
#pip install rembg
#pip install Pillow
#pip install colorama

from rembg import remove
from PIL import Image
from colorama import Fore, Back, Style, init
import os

init()

input_dir = r'D:\removerFundo\comFundo' # Caminho da pasta de imagens para tirar o fundo
output_dir = r'D:\removerFundo\semFundo' # Caminho da pasta de imagens sem fundo

os.makedirs(output_dir, exist_ok=True)
error_files = []

os.system('cls' if os.name == 'nt' else 'clear')

image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpeg', '.png'))]
total_images = len(image_files)

if total_images == 0:
   print(f"{Fore.RED}-> Nenhuma imagem encontrada no diretório: {Fore.YELLOW}{input_dir}{Style.RESET_ALL}\n")
   exit()
else:
   print(f"{Fore.CYAN}{total_images:02d} {'IMAGENS ENCONTRADAS' if total_images > 1 else 'IMAGEM ENCONTRADA'}{Style.RESET_ALL}")

for index, filename in enumerate(image_files, 1):
   input_path = os.path.join(input_dir, filename)
   output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + ".png")
   try:
      with Image.open(input_path) as img:
         output_img = remove(img)

         new_size = (500, 500)
         resized_img = output_img.resize(new_size)

         output_img.save(output_path, 'PNG')

         print(f"{Fore.GREEN}[{index:02d}/{total_images:02d}]{Style.RESET_ALL} Fundo de {Fore.GREEN}({filename}){Style.RESET_ALL} removido com sucesso!")
   except Exception as e:
      print(f"{Fore.RED}[{index:02d}/{total_images:02d}]{Style.RESET_ALL} Erro ao processar {Fore.RED}({filename}){Style.RESET_ALL}: {e}")
      error_files.append(filename)
if len(error_files) == total_images:
   print(f"\n{Fore.RED}-> Todas as imagens tiveram erro ao serem processadas!{Style.RESET_ALL}\n")
elif error_files:
   print(f"\n{Fore.CYAN}{len(error_files):02d} {'IMAGENS COM ERRO' if len(error_files) > 1 else 'IMAGEM COM ERRO'} {Style.RESET_ALL}")
   for file in error_files:
      print(f"{Fore.RED}-> {file}{Style.RESET_ALL}")
   print(f"\nAs imagens processadas podem ser encontradas em: {Fore.YELLOW}{output_dir}{Style.RESET_ALL}\n")
   os.startfile(output_dir)
else:
   print(f"\n{Fore.GREEN}-> Todas as imagens foram processadas com sucesso!{Style.RESET_ALL}")
   print(f"\nAs imagens processadas podem ser encontradas em: {Fore.YELLOW}{output_dir}{Style.RESET_ALL}\n")
   os.startfile(output_dir)
