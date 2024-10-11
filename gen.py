
import argparse
import os
import sys
from src.pipeline import UncondLatentDiffusionPipeline
from tqdm import tqdm
# запуск python gen.py <dir_for_save> <number_images>

def main():

    
    dir_for_save = sys.argv[1]
    number_generation = int(sys.argv[2])


    print(f"Директория для сохранения изображений: {dir_for_save}, кол-во изображений: {number_generation}")
    if not os.path.exists(dir_for_save):
        os.makedirs(dir_for_save)
        print(f"Создана директория {dir_for_save}")
    model_id = "Yagorka/ddpm_ema_512"
    pipeline = UncondLatentDiffusionPipeline.from_pretrained(model_id).to('cuda')
    for i in tqdm(range(number_generation)):
        image = pipeline(num_inference_steps=100).images[0]
        image.save(os.path.join(dir_for_save, f'{i}.jpg'))


if __name__=="__main__":
    main()