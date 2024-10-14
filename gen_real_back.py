
import argparse
import os
import sys
from diffusers import StableDiffusionPipeline
import torch
from tqdm import tqdm

# запуск python gen_real_back.py <dir_for_save> <number_images>

def get_inputs(prompt, batch_size=1, start_seed=13):                                                                                                                                                                                                                 
    generator = [torch.Generator("cuda").manual_seed(i+start_seed) for i in range(batch_size)]                                                                                                                                             
    prompts = batch_size * [prompt]                                                                                                                                                                                                                                                                                                                                                                                                                     
    return {"prompt": prompts, "generator": generator } 

def generate_images(pipeline, prompt, directory, n, batch_size, start_seed=1000):

    num = n//batch_size

    for j in tqdm(range(num)):
        images_all = pipeline(**get_inputs(prompt=prompt, batch_size=batch_size, start_seed=start_seed))
        for k, image in enumerate(images_all.images):
            image.save(os.path.join(directory, f'{j}_{k}.jpg'))
        start_seed+=batch_size
    if n-num*batch_size>0:
        images_all = pipeline(**get_inputs(prompt=prompt, batch_size=n-num*batch_size, start_seed=start_seed))
        for k, image in enumerate(images_all.images):
            image.save(os.path.join(directory, f'{num}_{k}.jpg')) 

def main():

    dir_for_save = sys.argv[1]
    number_generation = int(sys.argv[2])
    try:
        batch_size = int(sys.argv[3])
    except:
        batch_size = 4


    print(f"Директория для сохранения изображений: {dir_for_save}, кол-во изображений: {number_generation}")

    dir_for_save
    if not os.path.exists(dir_for_save):
        os.makedirs(dir_for_save)
        print(f"Создана директория {dir_for_save}")
    prompt="realystic photo palmer with fingers, white background, only five realystic fingers"
    model_id = "Yagorka/sd_palm_finetune_plus_lora"
    pipeline = StableDiffusionPipeline.from_pretrained(model_id, safety_checker = None,torch_dtype=torch.float16).to("cuda")
    # pipeline.load_lora_weights("lora2", weight_name="pytorch_lora_weights.safetensors")
    generate_images(pipeline, prompt, dir_for_save, number_generation, batch_size, start_seed=1000)


if __name__=="__main__":
    main()

