## Palm image generation images with unconditional latent diffusion

original repository for train ddpm [repository](https://github.com/zyinghua/uncond-image-generation-ldm.git)

### Cloning to local
```bash
git clone https://github.com/Yagorka/ddpm_ema_512.git
```
Then call:
```bash
cd ddpm_ema_512
```
### Installing the dependencies
Before running the scripts, make sure to install the library's training dependencies:
```bash
pip install -r requirements.txt
```

### Generate images
```bash
python gen.py dir_name number_image
```
dir_name - dir for save generated images

number_images - number images for generation


